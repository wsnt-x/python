with open('files/24_4627.txt') as f:
    data = f.readline()

pairs = ['PNO','NPO']

for i in pairs:
    data = data.replace(i,'*')

for i in 'NPO':
    data = data.replace(i,' ')

data = data.split()

print(len(max(data,key=len)))
