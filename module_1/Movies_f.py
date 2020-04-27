#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from collections import Counter
#print(os.listdir("../input"))


# In[3]:


data = pd.read_csv('C:/data.csv')


# In[4]:


len(data)


# # Предобработка датасета

# In[10]:


answer_ls = [] # создадим список с ответами. сюда будем добавлять ответы по мере прохождения теста
# сюда можем вписать создание новых колонок в датасете


# # 1. У какого фильма из списка самый большой бюджет?
# Варианты ответов:
# 1. The Dark Knight Rises (tt1345836)
# 2. Spider-Man 3 (tt0413300)
# 3. Avengers: Age of Ultron (tt2395427)
# 4. The Warrior's Way	(tt1032751)
# 5. Pirates of the Caribbean: On Stranger Tides (tt1298650)

# In[5]:


# тут вводим ваш ответ и добавлем в его список ответов (сейчас для примера стоит "1")
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from collections import Counter
#print(os.listdir("../input"))
data = pd.read_csv('C:/data.csv')
answer_ls = []
#q1='tt1345836'#,'tt0413300','tt1032751','tt1298650']
data1=data[(data.budget==data.budget.max())]
result=data1.original_title
display(result)
answer_ls.append(4)


# # 2. Какой из фильмов самый длительный (в минутах)
# 1. The Lord of the Rings: The Return of the King	(tt0167260)
# 2. Gods and Generals	(tt0279111)
# 3. King Kong	(tt0360717)
# 4. Pearl Harbor	(tt0213149)
# 5. Alexander	(tt0346491)

# In[282]:


data1=data[(data.runtime==data.runtime.max())]
result=data1.original_title
display(result)
answer_ls.append(2)


# # 3. Какой из фильмов самый короткий (в минутах)
# Варианты ответов:
# 
# 1. Home on the Range	tt0299172
# 2. The Jungle Book 2	tt0283426
# 3. Winnie the Pooh	tt1449283
# 4. Corpse Bride	tt0121164
# 5. Hoodwinked!	tt0443536

# In[283]:


data1=data[(data.runtime==data.runtime.min())]
result=data1.original_title
display(result)
answer_ls.append(3)


# # 4. Средняя длительность фильма?
# 
# Варианты ответов:
# 1. 115
# 2. 110
# 3. 105
# 4. 120
# 5. 100
# 

# In[284]:



result=data.runtime.mean()
display(result)
answer_ls.append(2)


# # 5. Средняя длительность фильма по медиане?
# Варианты ответов:
# 1. 106
# 2. 112
# 3. 101
# 4. 120
# 5. 115
# 
# 
# 

# In[285]:



result=data.runtime.median()
display(result)
answer_ls.append(1)


# # 6. Какой самый прибыльный фильм?
# Варианты ответов:
# 1. The Avengers	tt0848228
# 2. Minions	tt2293640
# 3. Star Wars: The Force Awakens	tt2488496
# 4. Furious 7	tt2820852
# 5. Avatar	tt0499549

# In[8]:


data['profit'] = data.revenue - data.budget
data1=data[(data.profit==data.profit.max())]
result=data1.original_title
display(result)
answer_ls.append(5)


# # 7. Какой фильм самый убыточный?
# Варианты ответов:
# 1. Supernova tt0134983
# 2. The Warrior's Way tt1032751
# 3. Flushed Away	tt0424095
# 4. The Adventures of Pluto Nash	tt0180052
# 5. The Lone Ranger	tt1210819

# In[287]:


data1=data[(data.profit==data.profit.min())]
result=data1.original_title
display(result)
answer_ls.append(2)


# # 8. Сколько всего фильмов в прибыли?
# Варианты ответов:
# 1. 1478
# 2. 1520
# 3. 1241
# 4. 1135
# 5. 1398
# 

# In[288]:


data1=data[(data.profit>0)]
#result=data1.value_counts()
display(data1['imdb_id'].nunique())
answer_ls.append(1)


# # 9. Самый прибыльный фильм в 2008 году?
# Варианты ответов:
# 1. Madagascar: Escape 2 Africa	tt0479952
# 2. Iron Man	tt0371746
# 3. Kung Fu Panda	tt0441773
# 4. The Dark Knight	tt0468569
# 5. Mamma Mia!	tt0795421

# In[289]:


#display(data.head(5))
data1=data[(data.release_year==2008)]
data2=data1[(data1.profit==data1.profit.max())]
#result=data1.value_counts()

display(data2.original_title)
answer_ls.append(4)


# # 10. Самый убыточный фильм за период с 2012 по 2014 (включительно)?
# Варианты ответов:
# 1. Winter's Tale	tt1837709
# 2. Stolen	tt1656186
# 3. Broken City	tt1235522
# 4. Upside Down	tt1374992
# 5. The Lone Ranger	tt1210819
# 

# In[290]:


data1=data[(data.release_year>2011) & (data.release_year<2015)]
data2=data1[(data1.profit==data1.profit.min())]
display(data2.original_title)
answer_ls.append(5)


# # 11. Какого жанра фильмов больше всего?
# Варианты ответов:
# 1. Action
# 2. Adventure
# 3. Drama
# 4. Comedy
# 5. Thriller

# In[291]:



varians_of_genres=[]
#создаем полный список всех возможных вариантов жанров
for i in range(1,len(data['imdb_id'])):
    genres=data.genres[i]
    array_genres=genres.split('|')
    for g in range(0,len(array_genres)):
        if array_genres[g] not in varians_of_genres:
            varians_of_genres.append(array_genres[g])
varians_of_genres=sorted(varians_of_genres)

genre_df = pd.DataFrame({'genre': varians_of_genres})
genre_df['Count']=0

for i in range(0,len(varians_of_genres)):
    #data1=data.genres.str.contains(varians_of_genres[i], na=False)
    counter=0
    for ii in range (0, len(data)):
        if varians_of_genres[i] in data.genres[ii]:
            counter=counter+1
    genre_df.Count[i]=counter
display((genre_df))
answer_ls.append(3)


# # 12. Какого жанра среди прибыльных фильмов больше всего?
# Варианты ответов:
# 1. Drama
# 2. Comedy
# 3. Action
# 4. Thriller
# 5. Adventure

# In[292]:



for i in range(0,len(varians_of_genres)):
    #data1=data.genres.str.contains(varians_of_genres[i], na=False)
    counter=0
    for ii in range (0, len(data)):
        if varians_of_genres[i] in data.genres[ii] and data.profit[ii]>0:
            counter=counter+1
    genre_df.Count[i]=counter
display(genre_df)

answer_ls.append(1)


# # 13. Кто из режиссеров снял больше всего фильмов?
# Варианты ответов:
# 1. Steven Spielberg
# 2. Ridley Scott 
# 3. Steven Soderbergh
# 4. Christopher Nolan
# 5. Clint Eastwood

# In[293]:


result=data['director'].value_counts()
display(result)
answer_ls.append(3)


# # 14. Кто из режиссеров снял больше всего Прибыльных фильмов?
# Варианты ответов:
# 1. Steven Soderbergh
# 2. Clint Eastwood
# 3. Steven Spielberg
# 4. Ridley Scott
# 5. Christopher Nolan

# In[294]:


data1=data[(data.profit>0)]
result=data1['director'].value_counts()
display(result)
answer_ls.append(4)


# # 15. Кто из режиссеров принес больше всего прибыли?
# Варианты ответов:
# 1. Steven Spielberg
# 2. Christopher Nolan
# 3. David Yates
# 4. James Cameron
# 5. Peter Jackson
# 

# In[295]:


#data1=data[(data.profit>0)]
result=data.groupby(['director'])['profit'].sum().sort_values(ascending=False)
display(result)
answer_ls.append(5)


# # 16. Какой актер принес больше всего прибыли?
# Варианты ответов:
# 1. Emma Watson
# 2. Johnny Depp
# 3. Michelle Rodriguez
# 4. Orlando Bloom
# 5. Rupert Grint

# In[296]:


#display(data.head())
actors=[]
#display(data.describe())
for i in range(0, len(data)):
    cast=data.cast[i]
    act_array=cast.split('|')
    for act in range(0,len(act_array)):
        if act_array[act] not in actors:
            actors.append(act_array[act])
actors=sorted(actors)
df_actors=pd.DataFrame({'actors': actors})
df_actors['Profit']=0
display(df_actors.head())
data_cast=data.cast.tolist()
data_profit=data.profit.tolist()
for i in range(0, len(df_actors)):
    for ii in range(0,len(data)):
        if df_actors.actors[i] in data_cast[ii]:
            df_actors.Profit[i]+=data_profit[ii]
result=df_actors.groupby(['actors'])['Profit'].sum().sort_values(ascending=False)
display(result)
answer_ls.append(1)


# # 17. Какой актер принес меньше всего прибыли в 2012 году?
# Варианты ответов:
# 1. Nicolas Cage
# 2. Danny Huston
# 3. Kirsten Dunst
# 4. Jim Sturgess
# 5. Sami Gayle

# In[114]:




df_actors=pd.DataFrame({'actors': actors})
df_actors['Profit']=0
data1=data[data.release_year==2012]
data1_cast=data1.cast.tolist()
data1_profit=data1.profit.tolist()
for i in range(0, len(df_actors)):
    for ii in range(0,len(data1)):
        if df_actors.actors[i] in data1_cast[ii]:
            df_actors.Profit[i]+=data1_profit[ii]
result=df_actors.groupby(['actors'])['Profit'].sum().sort_values(ascending=True)
display(result)
answer_ls.append(3)


# # 18. Какой актер снялся в большем количестве высокобюджетных фильмов? (в фильмах где бюджет выше среднего по данной выборке)
# Варианты ответов:
# 1. Tom Cruise
# 2. Mark Wahlberg 
# 3. Matt Damon
# 4. Angelina Jolie
# 5. Adam Sandler

# In[99]:


#display(data.head())
data1=data[data.budget>data.budget.mean()]
act_array_with_dublicates=[]
s=Counter(data1.cast).most_common(3)
sp_cast=data1['cast'].tolist()
#display(type(sp_cast))
#display(sp_cast)
for i in range(0,len(sp_cast)):
    acters=sp_cast[i].split('|')
    #display(sp_cast[i], acters)
    for ii in range (0,len(acters)):
        act_array_with_dublicates.append(acters[ii])
        #display(acters[ii])

#display(act_array_with_dublicates)
s=Counter(act_array_with_dublicates).most_common(3)
display(s)
answer_ls.append(3)


# # 19. В фильмах какого жанра больше всего снимался Nicolas Cage?  
# Варианты ответа:
# 1. Drama
# 2. Action
# 3. Thriller
# 4. Adventure
# 5. Crime

# In[124]:


data1=data[data.cast.str.contains('Nicolas Cage')]
#display(data1.head())
genre_df = pd.DataFrame({'genre': varians_of_genres})
genre_df['Count']=0
data1_genres=data1.genres.tolist()
for i in range(0,len(varians_of_genres)):
    #data1=data.genres.str.contains(varians_of_genres[i], na=False)
    counter=0
    for ii in range (0, len(data1)):
        if varians_of_genres[i] in data1_genres[ii]:
            counter=counter+1
    genre_df.Count[i]=counter
display(genre_df)
answer_ls.append(2)


# # 20. Какая студия сняла больше всего фильмов?
# Варианты ответа:
# 1. Universal Pictures (Universal)
# 2. Paramount Pictures
# 3. Columbia Pictures
# 4. Warner Bros
# 5. Twentieth Century Fox Film Corporation

# In[207]:


varians_of_studio=[]
#создаем полный список всех возможных вариантов студий
for i in range(1,len(data['imdb_id'])):
    studio=data.production_companies[i]
    
    array_studio=studio.split('|')
    for g in range(0,len(array_studio)):
        if 'Univers' in array_studio[g]:
            array_studio[g]='Universal'
        elif 'Warner' in array_studio[g]:
            array_studio[g]='Warner'
        elif 'Disn' in array_studio[g]:
            array_studio[g]='Disney'
        if array_studio[g] not in varians_of_studio:
            varians_of_studio.append(array_studio[g])
varians_of_studio=sorted(varians_of_studio)

studio_df = pd.DataFrame({'Studio': varians_of_studio})
studio_df['Count']=0

for i in range(0,len(varians_of_studio)):
    counter=0
    for ii in range (0, len(data)):
        if varians_of_studio[i] in data.production_companies[ii]:
            counter=counter+1
    studio_df.Count[i]=counter
display((studio_df.groupby(['Studio'])['Count'].sum().sort_values(ascending=False)))

answer_ls.append(4)


# # 21. Какая студия сняла больше всего фильмов в 2015 году?
# Варианты ответа:
# 1. Universal Pictures
# 2. Paramount Pictures
# 3. Columbia Pictures
# 4. Warner Bros
# 5. Twentieth Century Fox Film Corporation

# In[208]:



data1=data[data.release_year==2015]


studio_df = pd.DataFrame({'Studio': varians_of_studio})
studio_df['Count']=0

for i in range(0,len(varians_of_studio)):
    counter=0
    for ii in range (0, len(data1)):
        if varians_of_studio[i] in data1.production_companies[ii]:
            counter=counter+1
    studio_df.Count[i]=counter
display((studio_df.groupby(['Studio'])['Count'].sum().sort_values(ascending=False)))
answer_ls.append(1)


# # 22. Какая студия заработала больше всего денег в жанре комедий за все время?
# Варианты ответа:
# 1. Warner Bros
# 2. Universal Pictures (Universal)
# 3. Columbia Pictures
# 4. Paramount Pictures
# 5. Walt Disney

# In[213]:


data1=data[data.genres.str.contains('Comedy')]
data1_production_companies=data1.production_companies.tolist()
data1_profit=data1.profit.tolist()
studio_df = pd.DataFrame({'Studio': varians_of_studio})
studio_df['Profit']=0
for i in range(0,len(varians_of_studio)):
    counter=0
    for ii in range (0, len(data1)):
        if varians_of_studio[i] in data1_production_companies[ii]:
            counter=counter+data1_profit[ii]/len(data1_production_companies[ii].split('|'))
    studio_df.Profit[i]=counter
display((studio_df.groupby(['Studio'])['Profit'].sum().sort_values(ascending=False)))
answer_ls.append(5)


# # 23. Какая студия заработала больше всего денег в 2012 году?
# Варианты ответа:
# 1. Universal Pictures (Universal)
# 2. Warner Bros
# 3. Columbia Pictures
# 4. Paramount Pictures
# 5. Lucasfilm

# In[214]:


data1=data[data.release_year==2012]
studio_df = pd.DataFrame({'Studio': varians_of_studio})
studio_df['Profit']=0
ata1_production_companies=data1.production_companies.tolist()
data1_profit=data1.profit.tolist()
for i in range(0,len(varians_of_studio)):
    counter=0
    for ii in range (0, len(data1)):
        if varians_of_studio[i] in data1_production_companies[ii]:
            counter=counter+data1_profit[ii]/len(data1_production_companies[ii].split('|'))
    studio_df.Profit[i]=counter
display((studio_df.groupby(['Studio'])['Profit'].sum().sort_values(ascending=False)))

answer_ls.append(1)


# # 24. Самый убыточный фильм от Paramount Pictures
# Варианты ответа:
# 
# 1. K-19: The Widowmaker tt0267626
# 2. Next tt0435705
# 3. Twisted tt0315297
# 4. The Love Guru tt0811138
# 5. The Fighter tt0964517

# In[158]:


data1=data[data.production_companies.str.contains('Paramount Pictures')]
display(data1.head())
display((data1.groupby(['original_title'])['profit'].sum().sort_values(ascending=True)))
answer_ls.append(1)


# # 25. Какой Самый прибыльный год (заработали больше всего)?
# Варианты ответа:
# 1. 2014
# 2. 2008
# 3. 2012
# 4. 2002
# 5. 2015

# In[108]:


result=data.groupby(['release_year'])['profit'].sum().sort_values(ascending=False)
display(result)
answer_ls.append(5)


# # 26. Какой Самый прибыльный год для студии Warner Bros?
# Варианты ответа:
# 1. 2014
# 2. 2008
# 3. 2012
# 4. 2010
# 5. 2015

# In[215]:


data1=data[data.production_companies.str.contains('Warn')]
result=data1.groupby(['release_year'])['profit'].sum().sort_values(ascending=False)
display(result)
answer_ls.append(1)


# # 27. В каком месяце за все годы суммарно вышло больше всего фильмов?
# Варианты ответа:
# 1. Январь
# 2. Июнь
# 3. Декабрь
# 4. Сентябрь
# 5. Май

# In[173]:



data['Month']=data['release_date']
for i in range(0,len(data)):
    date=data.release_date[i].split('/')
    data.Month[i]=int(date[0])
result=data.groupby(['Month']).count()
display(result)
answer_ls.append(4)


# # 28. Сколько суммарно вышло фильмов летом? (за июнь, июль, август)
# Варианты ответа:
# 1. 345
# 2. 450
# 3. 478
# 4. 523
# 5. 381

# In[175]:


data1=data[(data.Month>5) & (data.Month<9)]
display(data1.info())
answer_ls.append(2)


# # 29. Какой режисер выпускает (суммарно по годам) больше всего фильмов зимой?
# Варианты ответов:
# 1. Steven Soderbergh
# 2. Christopher Nolan
# 3. Clint Eastwood
# 4. Ridley Scott
# 5. Peter Jackson

# In[197]:


winter=[1,2,12]
display(type(winter[1]))
data1=data.query('Month in [1,2,12]')
result=data1.groupby(['director'])['imdb_id'].count().sort_values(ascending=False)
display(result)
answer_ls.append(5)


# # 30. Какой месяц чаще всего по годам самый прибыльный?
# Варианты ответа:
# 1. Январь
# 2. Июнь
# 3. Декабрь
# 4. Сентябрь
# 5. Май

# In[200]:


result=data.groupby(['Month'])['profit'].sum().sort_values(ascending=False)
display(result)
answer_ls.append(2)


# # 31. Названия фильмов какой студии в среднем самые длинные по количеству символов?
# Варианты ответа:
# 1. Universal Pictures (Universal)
# 2. Warner Bros
# 3. Jim Henson Company, The
# 4. Paramount Pictures
# 5. Four By Two Productions

# In[231]:


data['Len_Title']=0
for i in range(0,len(data)):
    data.Len_Title[i]=len(data.original_title[i])
studio_df = pd.DataFrame({'Studio': varians_of_studio})
studio_df['Len_Title']=0
studio_df['Counter']=0
studio_df['Mean_s']=0
for i in range(0,len(varians_of_studio)):
    counter=0
    counter2=0
    for ii in range (0, len(data)):
        if varians_of_studio[i] in data.production_companies[ii]:
            counter=counter+data.Len_Title[ii]
            counter2+=1
    studio_df.Len_Title[i]=counter
    studio_df.Counter[i]=counter2
    studio_df.Mean_s[i]=counter/counter2
display(studio_df.groupby(['Studio'])['Mean_s'].mean().sort_values(ascending=False))
display(studio)
answer_ls.append(5)


# # 32. Названия фильмов какой студии в среднем самые длинные по количеству слов?
# Варианты ответа:
# 1. Universal Pictures (Universal)
# 2. Warner Bros
# 3. Jim Henson Company, The
# 4. Paramount Pictures
# 5. Four By Two Productions

# In[232]:


data['Words']=0
for i in range(0,len(data)):
    data.Words[i]=len(data.original_title[i].split(' '))
studio_df = pd.DataFrame({'Studio': varians_of_studio})
studio_df['Words']=0
studio_df['Counter']=0
studio_df['Mean_w']=0
for i in range(0,len(varians_of_studio)):
    counter=0
    counter2=0
    for ii in range (0, len(data)):
        if varians_of_studio[i] in data.production_companies[ii]:
            counter=counter+data.Words[ii]
            counter2=counter2+1
    studio_df.Words[i]=counter
    studio_df.Counter[i]=counter2
    studio_df.Mean_w[i]=counter/counter2
display(studio_df.groupby(['Studio'])['Mean_w'].mean().sort_values(ascending=False))
answer_ls.append(15)


# # 33. Сколько разных слов используется в названиях фильмов?(без учета регистра)
# Варианты ответа:
# 1. 6540
# 2. 1002
# 3. 2461
# 4. 28304
# 5. 3432

# In[250]:


slovar=[]
for i in range(0,len(data)):
    array_w=data.original_title[i].split(' ')
    for ii in range(0,len(array_w)):
        slovar.append(array_w[ii].lower())
df_s=pd.DataFrame({'Words': slovar})
s=df_s['Words'].nunique()
print(s)
answer_ls.append(3)


# # 34. Какие фильмы входят в 1 процент лучших по рейтингу?
# Варианты ответа:
# 1. Inside Out, Gone Girl, 12 Years a Slave
# 2. BloodRayne, The Adventures of Rocky & Bullwinkle
# 3. The Lord of the Rings: The Return of the King
# 4. 300, Lucky Number Slevin

# In[35]:


data1=data#.query('vote_average>7')
s=data1.groupby(['original_title'])['vote_average'].mean().sort_values(ascending=False)
df_s=pd.DataFrame(s)
len_data=len(data)//100
display(df_s.head(len_data))
answer_ls.append(1)


# # 35. Какие актеры чаще всего снимаются в одном фильме вместе
# Варианты ответа:
# 1. Johnny Depp & Helena Bonham Carter
# 2. Hugh Jackman & Ian McKellen
# 3. Vin Diesel & Paul Walker
# 4. Adam Sandler & Kevin James
# 5. Daniel Radcliffe & Rupert Grint

# In[279]:


import itertools as itertools
pairs=[]
for i in range(0, len(data)):
    cast=data.cast[i]
    act_array=cast.split('|')
    act_array=sorted(act_array)
    for act in range(0,len(act_array)-1):
        for ii in range (act+1,len(act_array)):
            pairs.append(act_array[act]+'|'+ act_array[ii])
s=Counter(pairs).most_common(5)
display(s)
answer_ls.append(5)


# # 36. У какого из режиссеров выше вероятность выпустить фильм в прибыли? (5 баллов)101
# Варианты ответа:
# 1. Quentin Tarantino
# 2. Steven Soderbergh
# 3. Robert Rodriguez
# 4. Christopher Nolan
# 5. Clint Eastwood

# In[33]:


data1=data
#display(data.head())
data1['Loose']=data1.profit<0
data1['Win']=data1.profit>0
d1=data1.groupby(['director'])['Loose'].sum().sort_values(ascending=False)
d2=data1.groupby(['director'])['Win'].sum().sort_values(ascending=False)
df1 = pd.DataFrame(d1)
df2 = pd.DataFrame(d2)

joined = df1.merge(df2, on='director', how='left')
joined['Proc']=(joined['Win']/(joined['Loose']+joined['Win']))*100
joined=joined[joined.Proc!=0]
joined=joined[joined.Proc!=100]
display(joined.groupby(['director'])['Proc'].sum().sort_values(ascending=False))
#answer_ls.append(1)


# # Submission

# In[297]:


len(answer_ls)


# In[298]:


pd.DataFrame({'Id':range(1,len(answer_ls)+1), 'Answer':answer_ls}, columns=['Id', 'Answer'])


# In[ ]:




