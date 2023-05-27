import requests

url ='http://www.gutenberg.org/files/2591/2591-0.txt'
res = requests.get(url)

# res.status_code

with open('gt_text','wb') as g:
    g.write(res.content)

# print(res.text[:100])

import re

words = re.findall(r'[a-zA-Z]+', res.text)  # 문자열만 자료화
print(len(words))

word_count ={}
for word in words:
    word = word.lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1


print(word_count)

print("{}가 사용된 횟수는 모두 {} 번 입니다.".format('ring', word_count['ring']))

import pandas as pd

df = pd.DataFrame(list(word_count.items()), columns = ['word', 'n'])
t = df.sort_values('n', ascending = False).head()
print(t)

from wordcloud import WordCloud
from collections import Counter

counts = Counter(word_count)

wc = WordCloud(background_color='white', width=400, height=200)
cloud = wc.fit_words(word_count)
# cloud.to_file('test.jpg')

import matplotlib.pyplot as plt
plt.figure(figsize=(10, 8))
plt.axis('off')
plt.imshow(cloud)
plt.show()

