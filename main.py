from fastapi import FastAPI
from mangum import Mangum
from youtube_transcript_api import YouTubeTranscriptApi

app = FastAPI()
handler = Mangum(app)


@app.get("/{id}")
async def get_subtitles(id: str, lang: str = "en"):
    # importing modules
    try:
        # using the srt variable with the list of dictionaries
        # obtained by the .get_transcript() function
        srt = YouTubeTranscriptApi.get_transcript(id, [lang])

        # creating or overwriting a file "subtitles.txt" with
        # the info inside the context manager
        file = ""
        # iterating through each element of list srt
        for i in srt:
            # writing each element of srt on a new line
            file += "{} \n ".format(i['text'])

        # return the content of the file as a streaming response
        return {"transcription": file}
        # return StreamingResponse(iter([file]), media_type="text/plain")
    except:
        return {"error": "No transcription found in the language " + lang + " please try another language"}
