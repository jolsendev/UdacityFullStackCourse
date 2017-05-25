import urllib

def read_quotes():
    quotes = open(r"C:\Users\a5w5nzz\Desktop\profanitychecker.txt")
    contents = quotes.read()
    print (contents)
    quotes.close()
    check_profanity(contents)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    if "true" in output:
        print("Profanity detected!")
    elif "false" in output:
        print("No profanity detected")
    else:
        print("Something got fucked up")
    connection.close()

read_quotes()
