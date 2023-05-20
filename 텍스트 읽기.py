# 텍스트 읽기

# f = open('sampleText.txt', 'r')
# data = f.read()             # 텍스트 전체 가져 오기
# print(data)
# f.close()

# 텍스트 한 줄씩 가져오고 numbering 하기

# f = open('sampleText.txt', 'r')
# line_num = 1
# line = f.readline()
#
# while line:
#     # print('[%d] %s' %(line_num, line), end='')
#     print('[{}]  {}'.format(line_num, line))
#     line = f.readline()
#     line_num += 1
# f.close

# readlines() 와 enumerate()를 이용해서 한줄씩 읽기

f = open('sampleText.txt', 'r')
lines = f.readlines()
for line_num, line in enumerate(lines):
    print('[{}]  {}'.format(line_num+1, line))

f.close()
