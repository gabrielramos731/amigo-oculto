import base64, json, aiohttp
from pathlib import Path

def encode_pk(pk):
    return base64.urlsafe_b64encode(str(pk).encode()).decode()

def decode_pk(pk):
    return int(base64.urlsafe_b64decode(pk.encode()).decode())


async def send_message(data):
  config_path = Path(__file__).resolve().parent / 'config.json'
  with open(config_path) as f:
    config = json.load(f)  
  
  headers = {
    "Content-type": "application/json",
    "Authorization": f"Bearer {config['ACCESS_TOKEN']}",
    }
  
  async with aiohttp.ClientSession() as session:
    url = 'https://graph.facebook.com' + f"/{config['VERSION']}/{config['PHONE_NUMBER_ID']}/messages"
    print(f'--{url}--')
    try:
      async with session.post(url, data=data, headers=headers) as response:
        if response.status == 200:
          print("Status:", response.status)
          print("Content-type:", response.headers['content-type'])

          html = await response.text()
          print("Body:", html)
        else:
          print(response.status)        
          print(response)        
    except aiohttp.ClientConnectorError as e:
      print('Connection Error', str(e))

def get_text_message_input(recipient, text):
  return json.dumps({
    "messaging_product": "whatsapp",
    "preview_url": False,
    "recipient_type": "individual",
    "to": recipient,
    "type": "text",
    "text": {
        "body": text
    }
  })
