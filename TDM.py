
import numpy as np
import pandas as pd
from IPython.display import display
pd.set_option('display.max_columns', None)  # 행과 열을 생략 없이 모두 보여주는 옵션
pd.set_option('display.max_rows', None)

## 데이타 가져오기 ##
df = pd.read_csv('news.CSV', encoding='cp949', engine='python')

## ?? ##
print('Number of rows and columns:{}'.format(df.shape))         #향과 열 수
print('Column List: {} '.format(df.columns))       # 컬럼 (열) 제먹 리스트

## 데이타에서 '제목' 필드만 5개 가져와 출력하기 ##
print("'제목' 필드만 출력하기")
print(df['제목'].head())


## 먕사 토큰화 ##
from konlpy.tag import Komoran
tagger = Komoran()
text = str(df['제목'].head())           # 자료가 스트링 형태로 제공 되야 한다. TDM을 만들 때는 리스트 타입이어야 한다

## 명사만 출력하가 ##
print("'제목' 필드 내용 중 모든 먕사 츨력 하기")
nouns = tagger.nouns(text)   # 분석 대성 택스트를 스트링 값으로 주어야 한다
print(nouns)


## 1음절 이상의 명사만 출력하기

print("'제목' 필드에서 단 음절 이상의 명사만 출력 하기")
def get_nouns(text):
    nouns = tagger.nouns(text)
    nouns = [word for word in nouns if len(word) > 1]
    print(nouns)
    return nouns

get_nouns(text)


## TDM 생성

from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer()
tdm = cv.fit_transform([text])      # 여기서는 text가 리스트로 변형되어야 한다,
# dtm = pd.DataFrame(data=tdm)
dtm = pd.DataFrame(tdm)

## 단어 목록 출력 ##
print('모든 어휘항목 출력하기')
names = cv.get_feature_names_out()   #단어 목록 보기
print(names)

## dense 행렬로 변환 ##
print('dense matrix 변환')
print(tdm.todense())

print('상관행렬로 변환')
print(np.corrcoef(tdm.todense(), rowvar = 0))

print('단어의 벡터 위치 값 표시 -- 빈도수 표시가 아님')
print(cv.vocabulary_)

print("어휘 빈도수 표시: ")
count_words = pd.DataFrame(cv.fit_transform([text]).toarray(), columns = names)
display(count_words)



