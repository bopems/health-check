import sys
import requests
import json
import time
import os

assert ('ENV_URL' in os.environ), "Url não informada, use para configurar use ENV_URL."
url = os.environ['ENV_URL']

payload = ""
headers = ""
tentativas = 10
timeout = 10
interval_seconds = 30
debug = 0

if ('ENV_DEBUG' in os.environ):
    debug = int(os.environ('ENV_DEBUG'))

if ('ENV_TRIES' in os.environ):
    tentativas = int(os.environ['ENV_TRIES'])

if ('ENV_PAYLOAD' in os.environ):
    payload = os.environ['ENV_PAYLOAD']

if ('ENV_HEADERS' in os.environ):
    headers = os.environ['ENV_HEADERS']

if ('ENV_TIMEOUT' in os.environ):
    timeout = int(os.environ['ENV_TIMEOUT'])

if ('ENV_INTERVAL' in os.environ):
    interval_seconds = int(os.environ['ENV_INTERVAL'])

if (debug):
    os.system('echo Url check: ' + url)
    os.system('echo Tentativas: ' + str(tentativas) + '. (Obs.: Para alterar use ENV_TRIES)')
    os.system('echo Payload: ' + payload + '. (Obs.: Para alterar use ENV_PAYLOAD, no formato json)')
    os.system('echo Headers: ' + headers + '. (Obs.: Para alterar use ENV_HEADERS, no formato json)')
    os.system('echo Timeout (segundos): ' + str(timeout) + '. (Obs.: Para alterar use ENV_TIMEOUT)')
    os.system('echo Interval (segundos): ' + str(interval_seconds) + '. (Obs.: Para alterar use ENV_INTERVAL)')

cont = 1
error = True

while(True):
    try:
        req = requests.request("GET", url, data=payload, headers=headers, timeout=timeout)
        data = json.loads(req.content)
    except:
        if (debug):
            os.system("Tentando " + str(cont) + "...")
    else:
        error = False
        break
    cont += 1
    if (cont > tentativas):
        break
    time.sleep(interval_seconds)

if (error==False):
    os.system("echo SUCCESS")
else:
    os.system("echo FAILURE")
