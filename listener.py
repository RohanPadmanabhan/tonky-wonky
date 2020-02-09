import sys
from enum import Enum


class AlexaState(Enum):
    #CONNECTING = 'Connecting...'
    IDLE = 'Alexa is currently idle!'
    LISTENING = 'Listening...'
    THINKING = 'Thinking...'
    SPEAKING = 'Speaking...'

        
def parseStatus(line):
    for state in AlexaState:
        if state.value in line:
            return state

def raiseHead():
    print("Raising head")
    
def lowerHead():
    print("Lower head")

def turnLedsOn():
    print("Turn LEDs on")

def turnLedsOff():
    print("Turn LEDs off")
    
def moveMouth():
    print("Move mouth")
    
def shutMouth():
    print("Stop move mouth")

def main():
    currentState = AlexaState.IDLE
    for line in sys.stdin:
        
        newState = parseStatus(line)
        
        if newState is None or newState == currentState:
            continue
        
        currentState = newState
        
        if currentState == AlexaState.LISTENING:
            turnLedsOn()
            raiseHead()
            
        if currentState == AlexaState.SPEAKING:
            moveMouth()
        
        if currentState == AlexaState.IDLE:
            shutMouth()
            lowerHead()
            turnLedsOff()


if __name__ == '__main__':
    main()
        
