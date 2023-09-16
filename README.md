### FastAPI youtube videos transcriptor
===============================

This is a simple project to transcribe youtube videos using FastAPI and YouTubeTranscriptApi.

## How to run
1. Clone the repo
3. Install the requirements by running `pip install -r requirements.txt`
4. Run the app with uvicorn by running `uvicorn main:app --reload`
5. Do a GET request at http://localhost:8000/{youtube-video-id}?lang={video-transcription-language} to get the transcription text

## How to deploy on AWS Lambda

1. Install the libraries locally by running
```
pip3 install -t lib -r requirements.txt
```
2. Create a zip file with the content of the folder lib, if you are using linux you can do it running
```
apt install zip
```
  and then run
```
(cd lib; zip ../aws_lambda_artifact.zip -r .)
```
3. Add the file main.py to the zip file, if you are using linux you can do it running
```
zip aws_lambda_artifact.zip -u main.py
```
4. Create an AWS Lambda function on your AWS account and then upload the zip file and it is done
