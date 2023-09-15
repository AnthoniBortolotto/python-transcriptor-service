from fastapi import FastAPI
from mangum import Mangum
from youtube_transcript_api import YouTubeTranscriptApi

app = FastAPI()
handler = Mangum(app)


@app.get("/{id}")
async def get_subtitles(id: str, lang: str = "pt"):
    try:
        srt = YouTubeTranscriptApi.get_transcript(id, [lang]) # getting the subtitles of the video
        file = ""
        # iterating through each element of list srt
        for i in srt:
            # writing each element of srt on a new line
            file += "{} \n ".format(i['text'])

        # return the content of the file as a json
        return {"transcription": file}
    except:
        return {"error": "No transcription found in the language " + lang + " please try another language or check the video id"}
