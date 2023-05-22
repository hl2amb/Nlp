with open('sampleText.txt', 'r') as f:
    raw_text = f.read()

# 단어의 갰수

word_num = len(raw_text)
print('문장부호를 포함한 단어의 갯수는 모두 {} 자 입니다.'.format(word_num))

# Counter로  단어의 빈도수 확인 / Counter는 개체와 빈도수를 사전형식으로 반환 해줌

# from collections import Counter
#
# word_frequency = Counter(raw_text.split())
# fre = word_frequency.items()
# for k, v in fre:
#     print('{0}의 빈도수: {1}'.format(k,v))


# 문장부호 등 불필요한 문자 제거하기

import re

new_text = re.sub(r'[.,"!?:;")(“—]', '', raw_text)
# print(new_text)
num_words = len(new_text)
print('문장부호를 제거한 단어의 갯수는 {} 입니다.'.format(num_words))

final_text = new_text.lower()
new_num = len(final_text)

print('대소문자 구분 없는 단어의 갯수는 {} 개 입니다.'.format(new_num))

# 단어의 빈도수를 한줄씩 출력하기

from collections import Counter


word_frequency = Counter(final_text.split())
fre = word_frequency.items()
for k, v in fre:
    print('{0} 의 빈도수: {1}'.format(k,v))