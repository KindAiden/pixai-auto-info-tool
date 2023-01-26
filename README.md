# Info
This is a tool for creating multiple generation tasks at once on pixai.art.
You have the choice between three different versions of the tool, so pick the one you like the most.

# V1 features
- Choose how many images to generate
- Generate multiple images with different prompts
- Type negative prompts
- Raise the sampeling steps to 50
- Choose the image size
- Choose the model to use
- Auto-submit, to automaticaly submit when the generation page is filled in
- Choose to use high priority

# V2 features
- Everything from V1
- A nice GUI

# ~V3 features~
- ***V3 is still in development***

# How it works (V1/V2)
***before starting, open the web browser of your choice***

After you've entered your settings and promt the tool will open a new tab using CTRL-T and go to https://pixai.art/submit/gen?no-redirect=1, it will wait exactly five seconds for the page to load.

Then it turns off auto publish and minimizes the artwork info section.

Now is when it starts typing the prompt you specified in the tool. Note that it will take longer to type more characters (obviously)

After that, the advanced parameters section is opened. If specified, negative promts are added to the start of the negative promts list.

Then the model is choosen, the sampling steps is set to 50 and the size of the image is selected.

If you turned on auto-submit, the submit button is clicked and the tab is closed using CTRL-W for all the prompts it made.

# pefomance (V1/V2)
Time = 8 + (x / 30) + (y / 30)
Where Time is the time in seconds the tool needs for one filled-out submit page, x is the ammount of characters in the prompt and y is the
ammount of characters in the negative prompt.
x and y are devided by 30 since typing 30 characters will take one second.

Time = (1.5 * x) - 1.5
Where Time is the time in seconds the tool needs to submit and close all tabs and x is the ammount of tabs opened by the tool.
The - 1.5 at the end is there because the final tab is not closed so you end up in your accounts generation tasks page.

# ~how it works (V3)~
*V3 is a complete rework of the first two versions, sending data directly to the pixai servers.*
