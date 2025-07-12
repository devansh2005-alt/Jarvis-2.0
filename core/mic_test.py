# import speech_recognition as sr

# recognizer = sr.Recognizer()
# with sr.Microphone() as source:
#     print("🎤 Say something...")
#     audio = recognizer.listen(source)

# try:
#     print("⌛ Recognizing...")
#     text = recognizer.recognize_google(audio)
#     print("✅ You said:", text)
# except Exception as e:
#     print("❌ Error:",e)

import speech_recognition as sr

mics = sr.Microphone.list_microphone_names()

if not mics:
    print("❌ No microphones detected by Python.")
else:
    print("✅ Microphones found:")
    for index, name in enumerate(mics):
        print(f"{index}: {name}")