import nltk

text = "I loved you. But you didn't love me. I don't want to see you anymore. What a sucks!"

# 단어 단위로 분리 하기

token_word = nltk.word_tokenize(text)
print(token_word)

# 문장 단위로 분리 하기

token_sent = nltk.sent_tokenize(text)
print(token_sent)

# 단어와 문장 갯수 출력 하기

print('단어의 갯수는 모두 {} 개 입니다.'.format(len(token_word)))
print('문장의 갯수는 모두 {} 개 입니다.'.format(len(token_sent)))

# 문장부호나 불필요한 단어 지우기

import re

new_text = re.sub(r'[.,!]','', text)     #r은 글자 그대로 인식할것, 리스트에 있는 글자를 무('')로 변환해서 text에 반환
                                         # 문장부호나 특정 부호 제거

new_word = nltk.word_tokenize(new_text)
print(new_word)
print('문장부호를 제거한 후 단어의 갯수는 모두 {} 개 입니다.'.format(len(new_word)))

# 단어 빈도수 계산
from collections import Counter

repeating = Counter(new_text.split())  #.split이 없으면 철자 하나씩 카운트 한다.

wd_frequency = sorted(repeating.items(), key =lambda X: X[1], reverse=True) #내림차순으로 정리
print(wd_frequency)

#상위 n개의 단어만 출력하기
# for k, v in wd_frequency:
#     print("{}의 출현 빈도는 {} 번 입니다.".format(k,v))

fre = wd_frequency[:2]
for k, v in fre:
    print("{}의 출현 빈도는 {} 번 입니다.".format(k, v))

