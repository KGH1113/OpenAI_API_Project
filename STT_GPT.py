import openai

class SpeechRecognition:
    def recognize(r):
        import speech_recognition as sr
        while not KeyboardInterrupt:
         try:
            with sr.Microphone() as source:
               print("Listening")
               audio = r.listen(source)
               text = r.recognize_google(audio, language="en-US")
               print(text)
         except Exception as e:
            return e
    def print_error(e):
        import speech_recognition as sr
        if e == sr.UnknownValueError:
            print("Failed to recognize speech")
        elif sr.RequestError:
            print("Failed to request: " + e)
        elif e == Exception:
            print("Exceptional error had been occured")
        else:
            pass


class OpenAI_Request:
    def request(API_KEY_CODE, prompt):
        openai.api_key = API_KEY_CODE

        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        return response["choices"][0]["text"]


if __name__ == '__main__':
    # listener = sr.Recognizer()
    # SpeechRecognition.recognize(listener)
    prompt = input()
    API_KEY_CODE = "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"
    answer = OpenAI_Request.request(API_KEY_CODE, prompt)
    print(answer)

# Please tell me a pros and cons about Chat GPT

