import urllib
#another API for profanity  http://www.purgomalum.com/

path = r"C:\Users\hamod\OneDrive\Desktop\one-million-arab-coders-full-stack\projects\check profanity\movie_quotes.txt"


def get_file(path):
    quote = open(path)
    content = quote.read()
    quote.close()
    return content

def profanity(text):
    connect = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text)
    result = connect.read()
    connect.close()
    return result


text = get_file(path)
result = profanity(text)

if result == "true":
    print "there is a bad word"
else:
    print "all good !"

