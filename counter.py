import threading 
import time
  
def print_number():
  for i in range(9999999999999999999999999999):
    time.sleep(2)
    print(i)
  

t1 = threading.Thread(target=print_number)  
t1.start()

