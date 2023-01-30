# Setup
This part will explain how to setup pixai auto info tool V3. Please follow these steps carefully.

1. Download the settings.txt file from this branch.
2. Place the file in the same location as the tool.
3. Open pixai.art in the web browser of your choice and go to the [submit page](https://pixai.art/submit/gen?no-redirect=1).
4. Fill the settings in the submit page. Do **NOT** press the 'Let's go!' button yet.
5. Open the Dev-tools in your browser. This is usualy done by pressing the f12 key.
6. Go to the 'Network' tab and check the 'Preserve log' checkmark.
7. Click the 'Let's go!' button on the submit page.
8. Your Dev-tools page should look like this now: ![image](https://user-images.githubusercontent.com/100278160/215082988-d95d715a-df9a-47ee-8b9f-a8461a36f821.png)
Click on any of the 'graphql' requests and scroll down to the 'Request Headers'.
9. Right-click on 'authorization' -> copy value
10. Open settings.txt and paste your authorization key on the first line. It should look like this: 'authorization: [your_auth_key]'
11. Start the tool, it should read everything from the settings file automaticaly.

You are now done with the setup!

***NEVER SHARE YOUR AUTH KEY!!***
Someone could use it to make requests on your account.

# Compound words
Compound words were added in V3.1, but what are they and how do you use them?

### What are compound words?
Compound words are words in your prompt that get replaced by the tool automaticaly, For example, when typing 'Mia, relaxing, picnic' in the prompt the tool will send '(schoolgirl, cute, blonde hair, blue eyes), relaxing, picnic'. This way you can just type the names of your favorite characters or places and the tool will describe them to the pixai servers.

### How to use compound words?
Using compound words is really simple, all you need to do is create a new .txt file in the same folder as the tool and name it 'compound words'.

Now open the file, type a word like 'mia' and add the description for that word; 'schoolgirl, cute, blonde hair, blue eyes'.
The text should be formatted as **[compound word]: [description]**.
