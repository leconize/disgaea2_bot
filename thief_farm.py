import pyautogui
pyautogui.PAUSE = 2.5
def btn_confirm():
    pyautogui.press('k')

def wait_for_map_choose():
    image = pyautogui.locateOnScreen("choosemap.png")
    while image == None:
        image = pyautogui.locateOnScreen("choosemap.png")
        print("still haven't found the image")

def wait_for_map_ready():
    image = pyautogui.locateOnScreen("inmap.png")
    while image == None:
        image = pyautogui.locateOnScreen("inmap.png")
        print("map not ready yet")
i = 0
while i < 5:
    #enter map
    #wait_for_map_choose()
    #btn_confirm()
    #btn_confirm()
    print("enter map")
    wait_for_map_ready()
    #choose character
    print("start choose character")
    btn_confirm()
    btn_confirm()
    btn_confirm()
    btn_confirm()
    print("choose chacter")
    #move to prinny
    btn_confirm()
    pyautogui.press('d')
    pyautogui.press('d')
    pyautogui.press('d')
    pyautogui.press('d')
    btn_confirm()
    print("move")
    #choose lift action
    pyautogui.press('s')
    pyautogui.press('s')
    pyautogui.press('s')
    pyautogui.press('s')
    btn_confirm()
    btn_confirm()

    #lift
    pyautogui.press('d')
    pyautogui.press('d')
    pyautogui.press('d')
    pyautogui.press('d')
    btn_confirm()

    #choose lift position
    pyautogui.press('d')
    pyautogui.press('d')
    btn_confirm()

    #next
    btn_confirm()
    i += 1

