import requests
import json
from bs4 import BeautifulSoup

url = 'https://api.pixai.art/graphql'

data ={
    "query": "\n    mutation createGenerationTask($parameters: JSONObject!) {\n  createGenerationTask(parameters: $parameters) {\n    ...TaskBase\n  }\n}\n    \n    fragment TaskBase on Task {\n  id\n  userId\n  parameters\n  outputs\n  artworkId\n  status\n  priority\n  runnerId\n  startedAt\n  endAt\n  createdAt\n  updatedAt\n  media {\n    ...MediaBase\n  }\n  type {\n    type\n    model\n  }\n}\n    \n\n    fragment MediaBase on Media {\n  id\n  type\n  width\n  height\n  urls {\n    variant\n    url\n  }\n  imageType\n  fileUrl\n  duration\n  thumbnailUrl\n  hlsUrl\n  size\n}\n    ",
    "variables": {
        "parameters": {
            "prompts": "(not)final test",
            "extra": {},
            "negativePrompts": "nsfw, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry",
            "samplingSteps": 28,
            "samplingMethod": "Euler a",
            "cfgScale": 11,
            "autoPublish": False,
            "priority": 0,
            "model": "anything-v3.0",
            "width": 512,
            "height": 512
        }
    }
}

headers = {
    #":authority": "api.pixai.art",
    #":method": "POST",
    #":path": "/graphql",
    #":scheme": "https",
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "nl-NL,nl;q=0.9",
    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2NzQ3MzQxMDQsImV4cCI6MTY3NTMzODkwNCwic3ViIjoiMTU0Mzc3MzE5MTM5OTMyMDcxNCJ9.RMQQ77BZtkffiiSiubuRfq1nJIXWXtszQ0gho-gsoh8",
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

response = requests.post(url, data=json.dumps(data), headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

if response.status_code == 200:
    print('status code: ', response.status_code, ' OK')
    print()
elif response.status_code == 401:
    print('status code: ', response.status_code, ' the request failed, please check your authorization')
    print()
else:
    print('status code: ', response.status_code, ' the request failed, i don\'t know why though...')
    print()

#print('headers: ', response.headers)
#print()
#print('content: ', response.content)
#print()
#print(soup.find_all())
