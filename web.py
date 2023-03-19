import gradio as gr
import openai
import config
from gtts import gTTS
import os
import subprocess



openai.api_key = config.OPENAI_API_KEY

messages = [
        {"role": "system", "content": "You are a preppy tourist guide based in Saudi Arabia. Respond with short and sweet tone, it should not be to long, and it should be natuarly spoken."},
        
            ]

def trascribe(audio):
    global messages
    

    audio_file= open(audio, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    print(transcript)

    messages.append({"role": "user", "content": transcript["text"]})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
        )
    
    systems_message = response["choices"][0]["message"]["content"]

    # The text that you want to convert to audio
    mytext = systems_message
  
    # Language in which you want to convert
    language = 'en'

    myobj = gTTS(text=mytext, lang=language, slow=False)
    # Saving the converted audio in a mp3 file named
     
    myobj.save("welcome.mp3")
  
    subprocess.os.system("ffplay -nodisp -autoexit welcome.mp3")

    messages.append({"role": "assistant", "content": systems_message})

    
    chat_transcript = ""
    for message in messages:
        if message['role'] != 'system':
            chat_transcript += message['role'] + ": " + message['content'] + "\n\n"

    return chat_transcript

# change source="upload" to source="microphone" to record instead of upload what you want to say
ui = gr.Interface(fn=trascribe, inputs=gr.Audio(source="upload", type="filepath"), outputs="text").launch()


ui.launch()
