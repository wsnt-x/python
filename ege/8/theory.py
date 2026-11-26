from itertools import *

alph = sorted('FOCUS')
# Буквы в алфавитном порядке

# Формирует все возможные комбинации с повторениями
for i in product('123', repeat=3):
    s = ''.join(i)  # Объединяет все символы кортежа в строку

for pos,i in enumerate(product('123',repeat=3),start=1):
    i=''.join(i)
    print(pos,i)