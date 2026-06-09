from fastapi import FastAPI, HTTPException, Request
from fastapi import Response
from pydantic import BaseModel
from pathlib import Path
from library_basics import CodingVideo
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Get the directory where simple_api.py lives
APP_DIR = Path(__file__).parent

# Go up one level to the root, then to the resources folder
VIDEOS: dict[str, Path] = {
    "demo": APP_DIR.parent / "resources" / "oop.mp4"
}

# Templates directory
templates = Jinja2Templates(directory=str(APP_DIR.parent / "templates"))

# Tell FastAPI where to serve JS files when the browser asks for it
# Basically, when HTML files have something like: <script src="/js/app.js"></script>
# FastAPI needs to step in and know where to get that JS files to serve it back to the HTML/ browser

app.mount("/js", StaticFiles(directory=str(APP_DIR.parent / "js")), name="js")


class VideoMetaData(BaseModel):
    fps: float
    frame_count: int
    duration_seconds: float
    _links: dict | None = None

# @app.get("/video")
# def list_videos():
#     """List all available videos with HATEOAS-style links."""
#     return {
#         "count": len(VIDEOS),
#         "videos": [
#             {
#                 "id": vid,
#                 "path": str(path), # Not standard for debug only
#                 "_links": {
#                     "self": f"/video/{vid}",
#                     "frame_example": f"/video/{vid}/frame/1.0"
#                 }
#             }
#             for vid, path in VIDEOS.items()
#         ]
#     }

def _open_vid_or_404(vid: str) -> CodingVideo:
    path = VIDEOS.get(vid)
    if not path or not path.is_file():
        raise HTTPException(status_code=404, detail="Video not found")
    try:
        return CodingVideo(path)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Could not open video {e}")

def _meta(video: CodingVideo) -> VideoMetaData:
    return VideoMetaData(
            fps=video.fps,
            frame_count=video.frame_count,
            duration_seconds=video.duration
    )


@app.get("/video/{vid}", response_model=VideoMetaData)
def video(vid: str):
    video = _open_vid_or_404(vid)
    try:
            meta = _meta(video)
            meta._links = {
                "self": f"/video/{vid}",
                "frames": f"/video/{vid}/frame/{{seconds}}"
            }
            return meta
    finally:
        video.capture.release()


@app.get("/video/{vid}/frame/{t}", response_class=Response)
def video_frame(vid: str, t: float):
    video = _open_vid_or_404(vid)
    try:
        return Response(content=video.get_image_as_bytes(t), media_type="image/png")
    finally:
      video.capture.release()


@app.get("/video/{vid}/frame/{t}/ocr")
def video_frame_ocr(vid: str, t: float):
    video = _open_vid_or_404(vid)
    try:
        text = video.get_text_at_time(t)
        return {"text": text}
    finally:
        video.capture.release()

@app.get("/")
def index():
    return FileResponse(APP_DIR.parent/"templates/index.html")

@app.get("/videos", response_class=HTMLResponse)
def list_videos(request: Request, video_id: str = None):
    # This endpoint takes 'video_id' as a query parameter (e.g. /videos?video_id=demo)
    context = {
        "request": request,
        "count": len(VIDEOS),
        "videos": [{"id": vid, "path": str(path)} for vid, path in VIDEOS.items()],
        "active_video": video_id
    }
    return templates.TemplateResponse(request=request, name="browse.html", context=context)

@app.get("/stream_video")
def stream_video(video_id: str):

    #Actual streaming endpoint for the <video> tag
    #It returns the file back to whichever HTML page with the <video> tag that requested it
    #In this case, it is the player.html

    video_path = VIDEOS.get(video_id)
    return FileResponse(video_path, media_type="video/mp4")

@app.get("/play")
def videos(request: Request, video_id: str | None = None):
    video_url = None
    if video_id:
        # This URL will be loaded into the <video> tag
        video_url = f"/stream_video?video_id={video_id}"

    context = {
            "request": request,
            "videos": [{"id": vid, "path": VIDEOS[vid]} for vid in VIDEOS],
            "count": len(VIDEOS),
            "video_url": video_url,
            "video_id" : video_id
        }

    return templates.TemplateResponse(request=request, name="player.html", context=context)