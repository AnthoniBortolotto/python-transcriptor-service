### FastAPI youtube videos transcriptor
===============================

This is a simple project to transcribe youtube videos using FastAPI and YouTubeTranscriptApi.

## How to run
1. Clone the repo
3. Install the requirements by running `pip install -r requirements.txt`
4. Run the app with uvicorn by running `uvicorn main:app --reload`
5. Do a GET request at http://localhost:8000/{youtube-video-id}?lang={video-transcription-language} to get the transcription text

## Return format
The return format is a JSON that can have these 2 following structure depending on the "type" query parameter:
- type=text : returns the transcription as a full text appending all the text from the video 
```json
{
  "transcription": "The full transcription text"
}
```
- type=dialogues: returns the transcription as a list of dialogues
```json
{
  "dialogues": [
    {
      "start": 12.11,
      "end": 15.23, 
      "text": "Dialogue 1"
    },
    {
      "start": 15.24,
      "end": 18.45, 
      "text": "Dialogue 2"
    }
  ]
}
```
the type parameter is optional and if not provided it will default to "text"


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
