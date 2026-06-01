from pathlib import Path
import cv2
import numpy as np
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\dinhq\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

class CodingVideo:
    capture: cv2.VideoCapture

    def __init__(self, video: Path | str):
        self.capture = cv2.VideoCapture(video)
        if not self.capture.isOpened():
            raise ValueError(f"Cannot open {video}")

        self.fps = self.capture.get(cv2.CAP_PROP_FPS)
        self.frame_count = self.capture.get(cv2.CAP_PROP_FRAME_COUNT)
        self.duration = self.frame_count / self.fps


    def __str__(self) -> str:
        """Displays key metadata from the video

        Specifically, the following information is shown:
            FPS - Number of frames per second rounded to two decimal points
            FRAME COUNT - The total number of frames in the video
            DURATION (minutes) - Calculated total duration of the video given FPS and FRAME COUNT

        Reference
        ----------
        https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d
        """

        return f'Video metadata: Frame count: {int(self.frame_count)},  Frame rate: {round(self.fps,2)} fps, Length: {round(self.duration/60,2)} minutes'

    def get_frame_number_at_time(self, seconds: int) -> int:
        """Given a time in seconds, returns the value of the nearest frame"""
        return int(self.fps * seconds)

    def get_frame_rgb_array(self, frame_number: int) -> np.ndarray:
        """Returns a numpy N-dimensional array (ndarray)

        The array represents the RGB values of each pixel in a given frame

        Note: cv2 defaults to BGR format, so this function converts the color space to RGB
        """

        # Set the next frame to be decoded to frame_number
        # How to use SET() and CAP_PROP_POS_FRAMES:
        # https://docs.opencv.org/4.x/d8/dfe/classcv_1_1VideoCapture.html
        # https://docs.opencv.org/4.x/d4/d15/group__videoio__flags__base.html

        self.capture.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

        # Read() the given frame
        # How to use READ(): https://docs.opencv.org/4.x/d8/dfe/classcv_1_1VideoCapture.html
        success, frame = self.capture.read()
        if not success:
            raise ValueError(f"Could not read frame")

        # Convert from BGR to RGB
        # Tutorial: https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        return rgb_frame

    def get_image_as_bytes(self, seconds: int) -> bytes:
        self.capture.set(cv2.CAP_PROP_POS_FRAMES, self.get_frame_number_at_time(seconds))
        ok, frame = self.capture.read()
        if not ok or frame is None:
            raise ValueError("Invalid frame in target location")
        ok, buf = cv2.imencode(".png", frame)
        if not ok:
            raise ValueError("Failed to encode frame")
        return buf.tobytes()




    def save_as_image(self, seconds: int, output_path: Path | str = 'output.png') -> None:
        """Saves the given frame as a png image

        """

        # Convert the timestamp to a frame number
        frame = self.get_frame_number_at_time(seconds)

        # Get RGB array using the method built earlier
        rgb_array = self.get_frame_rgb_array(frame)

        # Use Pillow to convert the array to an Image object
        # How to: https://pillow.readthedocs.io/en/stable/reference/Image.html
        image = Image.fromarray(rgb_array)

        # Save the image to the specified path
        image.save(output_path)

    def get_text_at_time(self, seconds: int) -> str:
        """Extracts text from the video at the given timestamp using Tesseract OCR.

        Reference
        ---------
        https://github.com/madmaze/pytesseract
        """
        # 1. Convert seconds to frame number
        frame = self.get_frame_number_at_time(seconds)

        # 2. Get the RGB array for that frame
        rgb_array = self.get_frame_rgb_array(frame)

        # 3. Extract the text using pytesseract
        text = pytesseract.image_to_string(rgb_array)

        return text

def test():
    oop = CodingVideo("../resources/oop.mp4")
    print(oop)
    oop.save_as_image(42)
    extracted_text = oop.get_text_at_time(42)
    print(extracted_text)

if __name__ == '__main__':
    test()
