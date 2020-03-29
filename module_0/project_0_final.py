from datetime import datetime
import time
import random
random.seed(version=2)
up=100
def what_number(i):
    max=up
    min=1
    counter=0
    answer=(max+min//2)
    while answer!=i:
        answer=(max+min)//2
        if answer>i:
            max=answer
            counter+=1
        elif answer<i:
            min=answer
            counter+=1
        else:
            counter+=1       
    return counter

#result=0
#start_time = datetime.now()
#for i in range(1,up+1):
#    result+=what_number(i)    
#print('Среднее количество попыток:',result/up, 'время выполнения',datetime.now() - start_time)

x=random.randint(0, up+1)
res=what_number(x)
print('Ответ угадан за ',res,'попытки(ок)')
            