from konlpy.tag import Okt
tagger = Okt()

# result = tagger.pos('아버지가가방에들어가신다')
# result = tagger.morphs('아버지가가방에들어가신다')
result = tagger.nouns('아버지가가방에들어가신다')

print(result)