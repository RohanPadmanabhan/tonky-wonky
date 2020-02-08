import sys

def checkStatus(lookingFor, line):
    if lookingFor in line:
        print(lookingFor, flush=True)


for line in sys.stdin:
    checkStatus('Connecting...', line)
    checkStatus('Listening...', line)
    checkStatus('Thinking...', line)
    checkStatus('Speaking...', line)
    checkStatus('Alexa is currently idle!', line)
