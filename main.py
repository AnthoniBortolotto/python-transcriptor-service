from fastapi import FastAPI, HTTPException
from mangum import Mangum
from youtube_transcript_api import YouTubeTranscriptApi

app = FastAPI()
handler = Mangum(app)


@app.get("/transcription/text/{id}")
async def get_subtitles_text(id: str, lang: str = "pt"):
    try:
        srt = YouTubeTranscriptApi.get_transcript(id, [lang]) # get the subtitles of the video

        file = ""
        # iterate through each element of list srt
        for i in srt:
            # write each element of srt on a new line
            file += "{} \n ".format(i['text'])

        # return the content of the file as a json
        return {"transcription": file}
    except Exception as e:
        if e.args[0].find('No transcripts were found for any of the requested language codes') != -1:
            raise HTTPException(404, detail="No transcription found in the language " + lang + " please try another language or check the video id")

        raise HTTPException(500, detail="Internal Server Error")

@app.get("/transcription/dialogues/{id}")
async def get_subtitles_dialogues(id: str, lang: str = "pt"):
    try:

        srt = YouTubeTranscriptApi.get_transcript(id, [lang]) # getting the subtitles of the video
        JsonResponse = {
            "dialogues": []
        }
        for i in srt:
            JsonResponse["dialogues"].append({
                "start": i['start'],
                # adding the duration to the start time to get the end time and round it to 2 decimal places
                "end":  round(i['start'] + i['duration'], 2),
                "text": i['text']
            })
        return JsonResponse
    except Exception as e:
        if e.args[0].find('No transcripts were found for any of the requested language codes') != -1:
            raise HTTPException(404, detail="No transcription found in the language " + lang + " please try another language or check the video id")

        raise HTTPException(500, detail="Internal Server Error")
