with open('files/24_4602.txt') as f:
    data = f.readline()

pairs = ['BA', 'BO', 'CA', 'CO', 'DA', 'DO']

for i in pairs:
    data = data.replace(i,'*')

for i in 'ABCDO':
    data = data.replace(i,' ')

data = data.split()

print(len(max(data,key=len)))
