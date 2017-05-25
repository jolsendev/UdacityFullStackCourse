import time
import webbrowser

count = 0
print("This program started on "+time.ctime())
while(count < 3 ):
    time.sleep(2*60*60)
    webbrowser.open("www.google.com")
    count += 1