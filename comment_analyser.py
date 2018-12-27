from os import path, getcwd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from nltk.tokenize import RegexpTokenizer
from textblob import TextBlob
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from main import *

d = getcwd()
blob = [TextBlob(i) for i in lst_comments]
blob = [i for i in blob if i.detect_language() == 'en' and len(str(i)) > 3]
pos_comments = []
pos_cmnt_p_lst = []
neg_comments = []
neg_cmnt_p_lst = []

for i in blob:
    if i.polarity > 0:
        pos_cmnt_p_lst.append(i.polarity)
        pos_comments.append(str(i))
    elif i.polarity == 0:
        pass
    else:
        neg_cmnt_p_lst.append(i.polarity)
        neg_comments.append(str(i))
tokenizer = RegexpTokenizer(r'\w+')
pos_tokens = [tokenizer.tokenize(i) for i in pos_comments]
neg_tokens = [tokenizer.tokenize(i) for i in neg_comments]

# print(pos_comments)
# print(neg_comments)
# print(pos_tokens)
stop_words = STOPWORDS

# concatenate the list of comment words
pos_tokens1 = [x for xs in pos_tokens for x in xs]
neg_tokens1 = [y for ys in neg_tokens for y in ys]


# filtering the words
_filtered_pos = ' '
_filtered_neg = ' '
for i in pos_tokens1:
    if i not in stop_words:
        _filtered_pos = _filtered_pos + i + ' '
for j in neg_tokens1:
    if j not in stop_words:
        _filtered_neg = _filtered_neg + j + ' '

mask = np.array(Image.open(path.join(d, "india2.png")))

# word cloud for positive comments
wordcloud_pos = WordCloud(background_color='white', max_font_size=90, mask=mask, max_words=200, contour_width=3,
                          contour_color='green')
image_colors = ImageColorGenerator(mask)
wordcloud_pos.generate(_filtered_pos)
plt.figure()
plt.imshow(wordcloud_pos.recolor(color_func=image_colors), interpolation='bilinear')
plt.axis("off")
plt.show()

# word cloud for negative comments
wordcloud_neg = WordCloud(background_color='black', max_font_size=90, mask=mask, max_words=200, contour_color='green',
                          contour_width=2)
image_colors = ImageColorGenerator(mask)
wordcloud_neg.generate(_filtered_neg)
plt.figure()
plt.imshow(wordcloud_neg.recolor(color_func=image_colors), interpolation='bilinear')
plt.axis("off")
plt.show()
