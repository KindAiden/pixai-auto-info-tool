import requests
import json
from tkinter import *
import os

def validate_input(new_input):
    if new_input.isdigit() or new_input == '':
        return True
    return False

def start():
    i = 0
    prompts = []
    negative_prompts = []
    prompt = ''
    compound_words = []
    compound_meanings = []
    path = os.getcwd()
    if os.path.exists(path + '\\compound words.txt'):
        settings = open(path + '\\compound words.txt', encoding="utf8").readlines()
        for line in settings:
            split = line.split(': ')
            compound_words.append(split[0])
            compound_meanings.append(split[1])
    
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
    
    while len(negative_prompts) < len(prompts):
        negative_prompts.append('')
        
    i = 0
    while i < len(prompts):
        for word in compound_words:
            if word in prompts[i]:                
                prompts[i] = prompts[i].replace(word, '(' + compound_meanings[compound_words.index(word)] + ')')
        i += 1
    
    i = 0
    width = 512
    height = 512
    auto_publish = False
    if selected_size.get() == "Portrait":
        height = 768
    elif selected_size.get() == "Landscape":
        width = 768
    if int(auto_publish_var.get()):
        auto_publish = True
    
    url = 'https://api.pixai.art/graphql'
    
    headers = {
        #":authority": "api.pixai.art",
        #":method": "POST",
        #":path": "/graphql",
        #":scheme": "https",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "nl-NL,nl;q=0.9,en-US;q=0.8,en;q=0.7", 
        "authorization": str(authorization_input.get('1.0', 'end-1c')),
        "content-length": "1015",
        "content-type": "application/json",
        "origin": "https://pixai.art",
        "referer": "https://pixai.art",
        "sec-ch-ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "sec-gpc": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        }
    while i < int(image_amount_input.get()):
        data ={
            "query": "\n    mutation createGenerationTask($parameters: JSONObject!) {\n  createGenerationTask(parameters: $parameters) {\n    ...TaskBase\n  }\n}\n    \n    fragment TaskBase on Task {\n  id\n  userId\n  parameters\n  outputs\n  artworkId\n  status\n  priority\n  runnerId\n  startedAt\n  endAt\n  createdAt\n  updatedAt\n  media {\n    ...MediaBase\n  }\n  type {\n    type\n    model\n  }\n}\n    \n\n    fragment MediaBase on Media {\n  id\n  type\n  width\n  height\n  urls {\n    variant\n    url\n  }\n  imageType\n  fileUrl\n  duration\n  thumbnailUrl\n  hlsUrl\n  size\n}\n    ",
            "variables": {
                "parameters": {
                    "prompts": prompts[i],
                    "extra": {},
                    "negativePrompts": negative_prompts[i],
                    "samplingSteps": int(sampling_steps_input.get()),
                    "samplingMethod": "Euler a",
                    "cfgScale": 11,
                    "autoPublish": auto_publish,
                    "priority": int(high_priority_var.get()) * 1000,
                    "model": selected_model.get(),
                    "width": width,
                    "height": height
                    }
                }
            }
        
        response = requests.post(url, data=json.dumps(data), headers=headers)
        #soup = BeautifulSoup(response.content, 'html.parser')
        
        if response.status_code == 200:
            status.set('status code: ' + str(response.status_code) + ' OK')
            status_text.config(fg='green')
        elif response.status_code == 401:
            status.set('status code: ' + str(response.status_code) + ' the request failed, please check your authorization')
            status_text.config(fg='red')
        else:
            status.set('status code: ' + str(response.status_code) + ' the request failed, i don\'t know why though...')
            status_text.config(fg='red')
        
        #print('headers: ', response.headers)
        #print()
        #print('content: ', response.content)
        #print()
        #print(soup.find_all())
        i += 1
    return

#create the window
window = Tk()
window.title('PixAi auto info tool V3')

#create the canvas
canvas = Canvas(window, width=512, height=512)
canvas.pack()

status = StringVar()
images = StringVar()
prompts = StringVar()
sampling_steps = StringVar()
math = StringVar()
high_priority_var = IntVar()
auto_publish_var = IntVar()
selected_model = StringVar()
selected_size = StringVar()
models = ['anything-v3.0', 'counterfeit-v2.5', 'anything-v4.5', 'abyss-orange-mix-v2', 'pastel-mix']
sizes = ['Normal', 'Portrait', 'Landscape']

#create the text for displaying errors
status_text = Label(canvas, textvariable=status, font=('calibre',10,'normal'))

#create the text for authorization key
authorization_text = Label(canvas, text='auth: ')

#create the input field for the authorization key
authorization_input = Text(canvas, font=('calibre',9,'normal'))

#create the text for the # of images
image_amount_text = Label(canvas, text='# of images: ')

#create the input field for the # of images
image_amount_input = Entry(canvas, justify='right', validate='key', validatecommand=(canvas.register(validate_input), '%P'), textvariable=images)

#create the text for the # of promts
prompt_amount_text = Label(canvas, text='# of promts: ')

#create the input field for # of promts
prompt_amount_input = Entry(canvas, justify='right', validate='key', validatecommand=(canvas.register(validate_input), '%P'), textvariable=prompts)

#create the text for the # of promts
sampling_steps_text = Label(canvas, text='sampling steps: ')

#create the input field for the sampling steps
sampling_steps_input = Entry(canvas, justify='right', validate='key', validatecommand=(canvas.register(validate_input), '%P'), textvariable=sampling_steps)
sampling_steps_input.insert('0', '28')

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

#create the button for auto publish
auto_publish = Checkbutton(canvas, text='Use auto pulish ', font=('calibre',9,'normal'), variable=auto_publish_var)

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
    
    authorization_input.insert('1.0', settings[0].replace('\n', '').replace('authorization: ', ''))
    image_amount_input.insert('0', settings[1].replace('\n', '').replace('# of images: ', ''))
    prompt_amount_input.insert('0', settings[2].replace('\n', '').replace('# of prompts: ', ''))
    Math()
    if int(settings[3].replace('high priority: ', '')):
        high_priority.select()
    auto_publish_var.set(settings[4].replace('\n', '').replace('auto publish: ', ''))
    sampling_steps.set(settings[5].replace('\n', '').replace('sampling steps: ', ''))
    selected_model.set(models[int(settings[6].replace('\n', '').replace('Model: ', ''))])
    selected_size.set(sizes[int(settings[7].replace('\n', '').replace('Size: ', ''))])

#place all widgets on the canvas
status_text.place(x=5, y=27)
authorization_text.place(x=5, y=10)
authorization_input.place(x=40, y=10, width=466, height = 20)
image_amount_text.place(x=5, y=50)
image_amount_input.place(x=100, y=52, width = 25)
prompt_amount_text.place(x=5, y=70)
prompt_amount_input.place(x=100, y=72, width = 25)
sampling_steps_text.place(x=300, y=90)
sampling_steps_input.place(x=395, y=92, width = 25)
math_text.place(x=5, y=90)
prompt_input.place(x=6, y=275, width=500, height=200)
negative_prompt_input.place(x=6, y=170, width=500, height=100)
high_priority.place(x=300, y=47)
auto_publish.place(x=300, y=67)
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
