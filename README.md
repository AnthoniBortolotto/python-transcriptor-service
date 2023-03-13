### FastAPI youtube videos transcriptor
===============================

This is a simple project to transcribe youtube videos using FastAPI and YouTubeTranscriptApi.

## How to run
1. Clone the repo
2. Create a virtual environment
3. Install the requirements
4. Run the app with uvicorn by running `uvicorn main:app --reload`
5. Do a GET request at http://localhost:8000/{youtube-video-id}?lang={video-transcription-language} to get the transcription text
