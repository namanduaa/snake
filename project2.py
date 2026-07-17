# import pyautogui
# import time
# import pyperclip
# while True:
#     print(pyautogui.position())

# # pyautogui.click(1005, 743)
# # time.sleep(1)
# #    # 510,182
# #     # 1335,637

# # pyautogui.moveTo(510, 182)
# # pyautogui.dragTo(1335, 637, duration=1, button="left")

# # pyautogui.hotkey('ctrl','c')
# # time.sleep(1)

# # text= pyperclip.paste()

# # print(text)



# # # 


from openai import OpenAI

client = OpenAI(api_key="PASTE_YOUR_NEW_KEY_HERE")

response = client.responses.create(
    model="gpt-4.1-mini",
    input="Say hello in one sentence."
)

print(response.output_text)






import pyautogui
import time
import pyperclip
import os
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_ai_reply(message):
    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=f"Reply politely:\n{message}",
            max_output_tokens=150
        )
        return response.output_text

    except Exception as e:
        print("🔥 ERROR TYPE:", type(e))
        print("🔥 ERROR MESSAGE:", e)
        return "API Error"

while True:
    pyautogui.click(1005, 743)
    # 1️⃣ Select latest message (adjust coordinates!)
    pyautogui.moveTo(510, 182)
    pyautogui.dragTo(1335, 637, duration=1, button="left")
    time.sleep(0.5)

    # 2️⃣ Copy text
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(826,583)
    time.sleep(0.5)

    incoming_message = pyperclip.paste()
    print("Received:", incoming_message)

    # 3️⃣ Get AI reply
    reply = get_ai_reply(incoming_message)
    print("AI Reply:", reply)

    # 4️⃣ Click message box
    pyautogui.click(817, 605)
    time.sleep(0.5)

    # 5️⃣ Paste reply
    pyperclip.copy(reply)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)

    # 6️⃣ Press Enter to send
    # pyautogui.press('enter')

    # Wait before checking again
    time.sleep(10)

