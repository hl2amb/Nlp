from collections import Counter
import re

with open('53.txt', 'r', encoding='utf-8-sig') as f: # encoding을 써주면 \ufeff 같은 문자가 사라진다
    raw_text = f.read()
    # print(raw_text)
    print('공백을 포함한 모든 철자의 갯수 : {}'.format(len(raw_text))) # 공백을 포함한 모든 글자 수
    print('공백으로 구분한 모든 단어의 갯수 : {}'.format(len(raw_text.split())))  # 띠어쓰기로 구분한 단어의 갯수

    unified_text = raw_text.lower()
    clean_text = re.sub(r'[.,"?:;]', '', unified_text)
    # print(clean_text)
    print('문장부호를 제외한 철자의 갯수: {}'.format(len(clean_text)))
    print('문장부호를 제외한 단어의 갯수: {}'.format(len(clean_text.split())))

    # words = re.findall(r'[a-zA-Z]+', unified_text)  # ASCII 코드만 적용, 특수문자를 구분자로 인식하기 때문에
                                                      # 확장 ASCII 코드로 되어 있는 텍스트에는 적용할 수 없음
# 문장의 갯수 : nltk.sent 사용
import nltk
# import ssl
#
# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context
# nltk.download()

token_sent = nltk.sent_tokenize(raw_text)
print('이 텍스트는 모두 {} 문장으로 되어 있습니다.'.format(len(token_sent)))

# 단어 빈도수
frequency = Counter(clean_text.split())
fre = frequency.items()

for k, v in fre:
    print('[{}] : {}'.format(k, v))


from wordcloud import WordCloud

wc = WordCloud(background_color='white', width=400, height=200)
cloud = wc.fit_words(frequency)
# cloud.to_file('test.jpg')

import matplotlib.pyplot as plt
plt.figure(figsize = (10, 8))
plt.axis('off')
plt.imshow(cloud)
plt.show()



