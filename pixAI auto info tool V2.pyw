from pynput.keyboard import Key, Controller
from time import sleep
import mouse
from tkinter import *
import os

def validate_input(new_input):
    if new_input.isdigit() or new_input == '':
        return True
    return False

def start():
    #print(image_amount_input.get())
    #print(prompt_amount_input.get())
    #print(math.get())
    #print(high_priority_var.get())
    #print(auto_submit_var.get())
    #print(sampeling_steps_var.get())
    #print(prompt_input.get('1.0', 'end-1c'))
    #print(negative_prompt_input.get('1.0', 'end-1c'))
    i = 0
    prompts = []
    negative_prompts = []
    prompt = ''
    #add all prompts to an array
    for char in prompt_input.get('1.0', 'end-1c'):
        i = 0
        if char == '|':
            while i < int(image_amount_input.get()) / int(prompt_amount_input.get()):
                prompts.append(prompt)
                i += 1
            prompt = ''
        else:
            prompt = prompt + char
    i = 0
    while i < int(image_amount_input.get()) / int(prompt_amount_input.get()):
        prompts.append(prompt)
        i += 1
        
    prompt = ''
    #add all negative promts to an array
    for char in negative_prompt_input.get('1.0', 'end-1c'):
        i = 0
        if char == '|':
            while i < int(image_amount_input.get()) / int(prompt_amount_input.get()):
                negative_prompts.append(prompt)
                i += 1
            prompt = ''
        else:
            prompt = prompt + char
    i = 0    
    while i < int(image_amount_input.get()) / int(prompt_amount_input.get()):
        negative_prompts.append(prompt)
        i += 1
        
    prompts.sort()
    negative_prompts.sort()
    i = 0
    keyboard = Controller()
    
    mouse.move (10, 10, True)
    mouse.click('left')
    sleep(0.1)   
    
    while i < int(image_amount_input.get()):
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
        keyboard.type(str(prompts[i]))
        WaitTime = (len(prompts[i]) / 30) + 1
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
        if high_priority_var.get() == 0:
            mouse.move(1055, 455, True)
            mouse.click('left')
            sleep(0.1)
            
        #Choose the resolution
        if sizes.index(selected_size.get()) > 0:
            mouse.move(266, 451, True)
            mouse.click('left')
            sleep(0.1)
            mouse.move(0, 55, False)
            mouse.move(0, 35 * sizes.index(selected_size.get()), False)
            sleep(0.1)
            mouse.click('left')
            sleep(1)
        
        #add negative prompts
        mouse.move(190, 595, True)
        mouse.click('left')
        sleep(0.1)
        keyboard.type(str(negative_prompts[i]))
        WaitTime = len(negative_prompts[i]) / 30
        sleep(WaitTime)
        
        #scroll down
        mouse.wheel(delta = -3)
        sleep(0.1)
        
        #set the model
        if models.index(selected_model.get()) > 0:
            mouse.move(186, 456 + (45 * models.index(selected_model.get())), True)
            mouse.click('left')
            sleep(0.5)
        
        #Change the sampling steps to 50
        if sampeling_steps_var.get() == 1:
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
    
    if int(auto_submit_var.get()):
        i = 0
    
    while i < int(image_amount_input.get()):
        #if i % MaxQueue == 0 and i > 0:
            #sleep(queuetimer)
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
        if i == int(image_amount_input.get()):
            break
        with keyboard.pressed(Key.ctrl): #close the tab
            keyboard.tap('w')
    return
    
#create the window
window = Tk()
window.title('PixAi auto info tool V2')

#create the canvas
canvas = Canvas(window, width=512, height=512)
canvas.pack()

images = StringVar()
prompts = StringVar()
math = StringVar()
high_priority_var = IntVar()
auto_submit_var = IntVar()
sampeling_steps_var = IntVar()
selected_model = StringVar()
selected_size = StringVar()
models = ['Anything V3', 'Counterfeit V2', 'Anything V4.5']
sizes = ['Normal', 'Portrait', 'Landscape']

#create the text for the # of images
image_amount_text = Label(canvas, text='# of images: ')

#create the input field for the # of images
image_amount_input = Entry(canvas, justify='right', validate='key', validatecommand=(canvas.register(validate_input), '%P'), textvariable=images)

#create the text for the # of promts
prompt_amount_text = Label(canvas, text='# of promts: ')

#create the input field for # of promts
prompt_amount_input = Entry(canvas, justify='right', validate='key', validatecommand=(canvas.register(validate_input), '%P'), textvariable=prompts)

#create math text
math_text = Label(canvas, textvariable=math)
math.set('# of images per promt: ')

def Math(*args):
    try:
        math.set('# of images per promt: ' + str(int(image_amount_input.get()) / int(prompt_amount_input.get())))
    except:
        math.set('# of images per promt: NaN')

#create the input field for the prompt
prompt_input = Text(canvas, wrap=WORD, font=('calibre',10,'normal'))
prompt_input.insert('1.0', 'Enter your promt here.\nUse the pipe character "|" to seperate multiple prompts')

#create the input field for the negative prompt
negative_prompt_input = Text(canvas, wrap=WORD, font=('calibre',10,'normal'))
negative_prompt_input.insert('1.0', 'Enter your negative promt here.\nUse the pipe character "|" to seperate multiple prompts')

#create the button for high priority
high_priority = Checkbutton(canvas, text='Use high priority', font=('calibre',9,'normal'), variable=high_priority_var)

#create the button for auto submit
auto_submit = Checkbutton(canvas, text='Use auto submit', font=('calibre',9,'normal'), variable=auto_submit_var)

#create the button for sampeling steps
sampeling_steps = Checkbutton(canvas, text='Raise the sampeling steps', font=('calibre',9,'normal'), variable=sampeling_steps_var)

#create model text
model_text = Label(canvas, text='Model: ')

#create the menu for model
selected_model.set(models[0])
model_input = OptionMenu(canvas, selected_model, *models)

#create model text
size_text = Label(canvas, text='Size: ')

# create the menu for image size
selected_size.set(sizes[0])
size_input = OptionMenu(canvas, selected_size, *sizes)

#create the start button
start = Button(canvas, text='START', width=5, height=1, bg='lightgray', fg='black', font=('calibre',10,'bold'), command=start)

#load default settings
path = os.getcwd()
if os.path.exists(path + '\\settings.txt'):
    settings = open(path + '\\settings.txt', encoding="utf8").readlines()    
    image_amount_input.insert('0', settings[0].replace('\n', '').replace('# of images: ', ''))
    prompt_amount_input.insert('0', settings[1].replace('\n', '').replace('# of prompts: ', ''))
    Math()
    if int(settings[2].replace('high priority: ', '')):
        high_priority.select()
    if int(settings[3].replace('auto submit: ', '')):
        auto_submit.select()
    if int(settings[4].replace('raise sampelingsteps: ', '')):
        sampeling_steps.select()        
    selected_model.set(settings[5].replace('\n', '').replace('Model: ', ''))
    selected_size.set(settings[6].replace('\n', '').replace('Size: ', ''))

#place all widgets on the canvas
image_amount_text.place(x=5, y=50)
image_amount_input.place(x=80, y=52, width = 25)
prompt_amount_text.place(x=5, y=70)
prompt_amount_input.place(x=80, y=72, width = 25)
math_text.place(x=5, y=90)
prompt_input.place(x=6, y=275, width=500, height=200)
negative_prompt_input.place(x=6, y=170, width=500, height=100)
high_priority.place(x=300, y=50)
auto_submit.place(x=300, y=70)
sampeling_steps.place(x=300, y=90)
model_text.place(x=300, y=115)
model_input.place(x=350, y=110, width=125)
size_text.place(x=5, y=115)
size_input.place(x=55, y=110, width=125)
start.place(x=235, y=485)

#update the # of images per prompt text
images.trace('w', Math)
prompts.trace('w', Math)

window.mainloop()
#window.update()
