from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt



file_path = "Classic Computer Science Problems in Python by David Kopec (z-lib.org).txt"
file_handle = open(file_path).read()
stopwords = set(STOPWORDS)
stopwords.add("will")

book = WordCloud(max_words=5000, stopwords=stopwords)
book.generate(file_handle)
plt.imshow(book, interpolation='bilinear')
plt.axis("off")
plt.show()

image_file = "griffin-silhouette-ancient-mythology-fantasy-vector-18016755.jpg"

# create mask
a_mask = np.array(Image.open(image_file))

wc = WordCloud(background_color="black", max_words=2000, mask=a_mask,
               stopwords=stopwords)
wc.generate(file_handle)

plt.figure(figsize=(8,6), dpi=120)
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()

