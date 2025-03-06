import time

def count (end,start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(0.5)
    print("Done !")
    
count (25,20)