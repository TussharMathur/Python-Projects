import JarvisAI

obj= JarvisAI.JarvisAssistant()


while True:
    response = obj.mic_input()
    print(response)