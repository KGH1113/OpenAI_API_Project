from pynput.keyboard import Listener, Key, KeyCode
import pyautogui
import openai
import os
import clipboard

store = set()
 
HOT_KEYS = {
    'click_': set( [Key.cmd_l, KeyCode(char='l')] )
}

def get_prompt():
    print(str(clipboard.paste()))
    return str(clipboard.paste())

def click_():
    prompt = get_prompt()
    openai.api_key = "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"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
    )
    print(response)
 
def handleKeyPress(key):
    store.add(key)
 
    for action, trigger in HOT_KEYS.items():
        CHECK = all([ True if triggerKey in store else False for triggerKey in trigger ])
        if CHECK:
            try:
                func = eval(action)
                if callable(func):
                    func()
            except NameError as err:
                print(err)

def handleKeyRelease(key):
    if key in store:
        store.remove(key)
 
with Listener(on_press=handleKeyPress, on_release=handleKeyRelease) as listener:
    listener.join()


# 1565, 20
# 737, 838
# 900, 356