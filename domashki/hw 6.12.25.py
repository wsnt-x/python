# 1.Откройте файл 902, содержащий в каждой строке четыре натуральных числа. Определите
# количество строк, содержащих числа, для которых выполнены оба условия:
# наибольшее из четырёх чисел меньше суммы трёх других;
# среди четырёх чисел есть только одна пара равных чисел.

with open("902.txt","r") as f:
    # 28 51  16 23
    count=0
    for line in f:
        s=line.split()
        d=[]
        for i in s:
            d.append(int(i))
        d=sorted(d)
        counter_amount=0
        for i in range(len(d)):
            counter_cash=-1
            for j in range(len(d)):
                if d[i]==d[j]:
                    counter_cash=counter_cash+1
            if counter_cash>1:
                counter_amount=counter_amount+1
        if d[-1]>sum(d[:-1]) and counter_amount==1:
            count=count+1
    print(count)