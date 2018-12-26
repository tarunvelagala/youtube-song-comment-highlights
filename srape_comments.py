from main import *
from textblob import *

blob = [TextBlob(i) for i in lst_comments]

for i in blob:
    print(i.sentiment)



