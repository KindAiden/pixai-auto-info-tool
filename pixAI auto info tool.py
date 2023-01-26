from pynput.keyboard import Key, Controller
from time import sleep
import mouse

print(mouse.get_position())

i = 0
queuetimer = 0
UseCreddits = 0
MaxQueue = 30 #the maximum ammount of prompts pixai allows to be in queue
alltext = []
allnegativeprompts = []
loops = int(input('How many times do you want to run the script? (multiple prompts will be devided equaly of this ammount) '))
prompts = int(input('How many prompts do you want to type? '))
NP = int(input('Do you want to use negative promts? (No: 0, Yes: 1) '))
while i < prompts:
    text = input('What do you want to type? ')
    if NP == 1:
        negativePrompts = input('What negative prompts do you want to add? (end with ", ") ')
    i = i + 1
    j = 0
    while j < loops / prompts:
        alltext.append(text)
        if NP == 1:
            allnegativeprompts.append(negativePrompts)
        j = j + 1
    
SampelingSteps = int(input('Do you want to raise the sampeling steps? (No: 0, Yes: 1) '))
Size = int(input('Which size do you want? (Normal: 0, Portarait: 1, Landscape: 2) '))
Model = int(input('What model do you want to use? (Anything V3: 0, Counterfeit V2: 1, Anything V4.5: 2) '))
AutoSubmit = int(input('Do you want to use Auto-submit? (No: 0, Yes: 1) '))
if AutoSubmit == 1:
    UseCreddits = int(input('Do you want to use creddits? (No: 0, Yes: 1) '))

if loops > MaxQueue:
    queuetimer = int(input('Looks like you want to generate more than 8 images, PixAI has a maximum queue of 8. Please enter a time to wait in seconds. '))
i = 0
keyboard = Controller()

mouse.move (10, 10, True)
mouse.click('left')
sleep(0.1)   

while i < loops:
    #create new tab 
    with keyboard.pressed(Key.ctrl):
        keyboard.tap('t')
    sleep(0.5)
    mouse.move(300, 54, True)
    mouse.click('left')
    sleep(0.1)
    keyboard.type('https://pixai.art/submit/gen?no-redirect=1')
    sleep(0.1)
    keyboard.tap(Key.enter)
    sleep(5)
    #type the prompt
    mouse.move(486, 315, True)
    sleep(0.1)
    mouse.click('left')
    sleep(0.1)
    keyboard.type(str(alltext[i]))
    WaitTime = (len(alltext[i]) / 30) + 1
    sleep(WaitTime)
    
    #minimize artwork info
        #mouse.move(240, 743, True)
        #mouse.click('left')
        #sleep(0.1)
    
    #open advanced settings
    mouse.move(283, 538, True)
    sleep(0.1)
    mouse.click('left')
    sleep(0.1)
    #click the high priority button
    if UseCreddits == 0:
        mouse.move(1055, 455, True)
        mouse.click('left')
        sleep(0.1)
    #Choose the resolution
    mouse.move(266, 451, True)
    mouse.click('left')
    sleep(0.1)
    mouse.move(0, 55, False)
    mouse.move(0, 35 * Size, False)
    sleep(0.1)
    mouse.click('left')
    sleep(1)
    if NP == 1: #add negative prompts
        mouse.move(195, 610, True)
        mouse.click('left')
        sleep(0.1)
        keyboard.type(str(allnegativeprompts[i]))
        WaitTime = len(allnegativeprompts[i]) / 30
        sleep(WaitTime)
    #scroll down
    mouse.wheel(delta = -3)
    sleep(0.1)
    
    #set the modle
    mouse.move(186, 456 + (45 * Model), True)
    mouse.click('left')
    sleep(0.5)
    
    #Change the sampling steps to 50
    if SampelingSteps == 1:
        mouse.move(396, 614, True)
        sleep(0.1)
        mouse.press(button='left')
        sleep(0.1)
        mouse.move(700, 614, True, 0.2)
        mouse.release(button='left')
        sleep(0.1)
    #scroll down
    mouse.wheel(delta = -5)
    sleep(0.1)
    i = i + 1

if AutoSubmit == 1:
    i = 0

while i < loops:
    if i % MaxQueue == 0 and i > 0:
        sleep(queuetimer)
    sleep(0.1)
    #scroll down
    a = 0
    while a < 5:
        mouse.wheel(delta = -2)
        sleep(0.1)
        a = a + 1
    #turn off auto publish
    mouse.move(190, 600, True)
    mouse.click('left')
    sleep(0.1)
    #click the submit button
    mouse.move(1250, 800, True)
    mouse.click('left')
    sleep(1.5)
    i = i + 1
    if i == loops:
        break
    with keyboard.pressed(Key.ctrl): #close the tab
        keyboard.tap('w')
