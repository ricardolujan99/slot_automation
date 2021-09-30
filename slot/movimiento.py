import pyautogui


# bet 
def to_bet():
    pyautogui.moveTo(630,685)
    pyautogui.leftClick()



#mount bet
def min_bet():
    pyautogui.moveTo(218,741)
    pyautogui.leftClick()

def half_bet():
    pyautogui.moveTo(302,745)
    pyautogui.leftClick()

def duble_bet(): 
    pyautogui.moveTo(367,738)
    pyautogui.leftClick()

def max_bet():
    pyautogui.moveTo(448,746)
    pyautogui.leftClick()
    pyautogui.moveTo(860,261)
    pyautogui.leftClick()




#probability bet
def prob_25():
    pyautogui.moveTo(633,404)
    pyautogui.leftClick()


def prob_50():
    pyautogui.moveTo(475,558)
    pyautogui.leftClick()


def prob_75():
    pyautogui.moveTo(324,404)
    pyautogui.leftClick()


def prob_97():
    pyautogui.moveTo(457,266)
    pyautogui.leftClick()