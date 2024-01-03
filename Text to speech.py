# Text to speech

import pyttsx3
engine = pyttsx3.init()
text='''bhature ke pese dede de '''


# for item in text:
#     a=f"shoutout to {item}"
#     print(a)
engine.setProperty("rate",150)
engine.say(text)
engine.runAndWait()
rate = engine.getProperty("rate")
    # print(rate)
