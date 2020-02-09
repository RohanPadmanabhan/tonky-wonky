import sys
from enum import Enum
import eyes
import neck
import mouth

class AlexaState(Enum):
    #CONNECTING = 'Connecting...'
    IDLE = 'Alexa is currently idle!'
    LISTENING = 'Listening...'
    THINKING = 'Thinking...'
    SPEAKING = 'Speaking...'


class TonkyWonky:
    def __init__(self):
        
        self.eyes = eyes.Eyes()
        self.neck = neck.Neck()
        self.mouth = mouth.Mouth()
        self.currentState = AlexaState.IDLE

       
    def _parse_status(self, line):
        for state in AlexaState:
            if state.value in line:
                return state

    def run(self):
        try:
            for line in sys.stdin:
            
                newState = self._parse_status(line)
            
                if newState is None or newState == self.currentState:
                    continue
                self.currentState = newState
            
                if self.currentState == AlexaState.LISTENING:
                    self.eyes.turn_on()
                    self.neck.raise_neck()
            
                if self.currentState == AlexaState.SPEAKING:
                    self.mouth.start_mouth()
            
                if self.currentState == AlexaState.IDLE:
                    self.mouth.stop_mouth()
                    self.neck.lower_neck()
                    self.eyes.turn_off()
                    
        except Exception or KeyboardInterrupt:
            self.cleanup()


    def cleanup(self):
        self.eyes.shut_down()
        self.neck.shut_down()
        self.mouth.shut_down()

def main():
    TonkyWonky().run()

if __name__ == '__main__':
    main()
        
