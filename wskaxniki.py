from datetime import datetime
import time

def funk(time = datetime.now()):
    print(time)

for x in range(10):
    time.sleep(0.01)
    funk()