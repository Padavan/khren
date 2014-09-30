import time

class Timer(object):
    def __init__(self):
        object.__init__(self)
        self.minutes=5
        self.count=self.minutes*1
        self.is_state=False
    def start(self):
        self.is_state=False
        while self.count > 0:
            self.count-=1
            time.sleep(1)
            print self.is_state
            if self.is_state:
                break
    def stop(self):
        self.minutes=5
        self.count=5
        self.is_state=True
    def dumb(self):
        return self.count