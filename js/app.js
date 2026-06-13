const generateBtn = document.getElementById('btn-texts');
const videoPlayer = document.getElementById('video-player');

let videoId = null;
const output = document.getElementById('text-output');

//Key-value pair to store timestamps in sessionStorage
//timeStampKey is the key
//timeStamp is the value


const timeStampKey = `${videoId}-timestamp`; // ${ } uses with back ticks ` ` is JS way to get the value of the videoId variable and put it in this string
const timeStamp = sessionStorage.getItem(timeStampKey);

const themeToggleBtn = document.getElementById('theme-toggle');

// Run this when the GENERATE TEXTS button is clicked
// async allows a function to be asynchronous
// await pauses the async function until a Promise is done, ONLY pauses the async function, everything else still runs

generateBtn.addEventListener('click', async () => {
  if (videoPlayer) {

    // Pause the video and get the current timestamp when GENERATE TEXTS button clicked
    videoPlayer.pause();
    const currentTime = videoPlayer.currentTime;

    if (!videoId || videoId === ""){
      output.innerText = 'Invalid video ID';
      return;
    }

    // pauses here until the fetch() is done, meanwhile everything outside this eventListener runs
    // fetch() is bascially sending a GET to that endpoint

    const response = await fetch(`/video/${videoId}/frame/${currentTime}/ocr`);

    if (response.ok) {
      const data = await response.json();
      output.innerText = data.text;
    }
  }
});

// If a timeStamp exists, set the video player to that time
// Constantly update current time of video with 'timeupdate' and store it in sessionStorage

// Make sure that a videoplayer exists on the page before accessing videoId
if (videoPlayer) {
  videoId = videoPlayer.getAttribute('data-id');

  if (timeStamp) {
      videoPlayer.currentTime = parseFloat(timeStamp);
  }
  videoPlayer.addEventListener('timeupdate', () => {
    sessionStorage.setItem(timeStampKey, videoPlayer.currentTime);
  })
}

if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', function() {
        // Check if 'dark' is active
        if (document.documentElement.classList.contains('dark')) {
            // Turn it off and save
            document.documentElement.classList.remove('dark');
            sessionStorage.setItem('theme', 'light');
        } else {
            // Turn it on and save
            document.documentElement.classList.add('dark');
            sessionStorage.setItem('theme', 'dark');
        }
    });
}