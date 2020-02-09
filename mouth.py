from queue import Queue
import threading
import enum
import time

class MouthInstruction(enum.Enum):
    START_TALKING = 1
    STOP_TALKING = 2
    TERMINATE = 3

class Mouth:
    def __init__(self):
        print("Init mouth")
        self._instruction_queue = Queue()
        self._setupPins()
        
        self._running_thread = threading.Thread(target=self._run_consumer)
        self._running_thread.start()


    def start_mouth(self):
        print('Starting mouth')
        self._instruction_queue.put(MouthInstruction.START_TALKING)

    def stop_mouth(self, block=False):
        print('Stopping mouth')
        self._instruction_queue.put(MouthInstruction.STOP_TALKING)

    def shut_down(self):
        print('Shutting down mouth')
        self._instruction_queue.put(MouthInstruction.STOP_TALKING)
        self._instruction_queue.put(MouthInstruction.TERMINATE)
        self._running_thread.join()
        self._cleanupPins()
    
    
    def _setupPins(self):
        pass
    
    def _cleanupPins(self):
        pass
    
    def _move_mouth_once(self):
        ''' This function must block until the mouth has been opened and closed. '''
        print('Doing one mouth movement')
        time.sleep(1)
        pass
    
    def _run_consumer(self):
        lastInstruction = MouthInstruction.STOP_TALKING
        while True:
            # Try and update the instruction. Block if we are currently stopped.
            if lastInstruction == MouthInstruction.STOP_TALKING:
                lastInstruction = self._instruction_queue.get(block=True)
            else:
                lastInstruction = lastInstruction if self._instruction_queue.empty() else self._instruction_queue.get()
            
            
            if lastInstruction == MouthInstruction.START_TALKING:
                self._move_mouth_once()
                
            if lastInstruction == MouthInstruction.TERMINATE:
                return
                
            
    

        
        
