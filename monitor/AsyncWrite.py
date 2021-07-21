import threading
import time
import csv

class AsyncWrite(threading.Thread): 
    def __init__(self, dict, out):
        threading.Thread.__init__(self) 
        self.dict = dict
        self.out = out
  
    def run(self):
        with open(self.out, "a", newline="") as f:
            w = csv.DictWriter(f, self.dict.keys())
            w.writerow(self.dict)
