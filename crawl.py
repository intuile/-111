import  time,requests,json
import matplotlib
import seaborn

url='https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d'%int(time.time()*1000)
response = requests.get(url=url).json()
data=json.loads(response['data'])
print(data)
print(data.keys())

num = data['areaTree'][0]['children']
print(len(num))
for item in num:
    print(item['name'],end=" ")
else:
    print("\n")
hubei = num[0]['children']
for item in hubei:
    print(item)
else:
    print('\n')
total_data={}
for item in num:
    if item['name'] not in total_data:
        total_data.update({item['name']:0})
    for city_data in item['children']:
        total_data[item['name']]+=int(city_data['total']['confirm'])
print(total_data)
'''
import matplotlib.pyplot as plt
import  numpy as np

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

names = total_data.keys()
nums = total_data.values()

plt.figure(figsize=[10,6])
plt.bar(names,nums,width=0.3,color='green')

plt.xlabel("地区",fontproperties='SimHei',size=12)
plt.ylabel("人数",fontproperties='SimHei',rotation=90,size=12)
plt.title("全国疫情确诊人数对比图",fontproperties='SimHei',size=16)
plt.xticks(list(names), fontproperties='SimHei', rotation=-45, size=10)

for a,b in zip(list(names),list(nums)):
    plt.text(a, b, b, ha='center', va='bottom', size=6)
'''

#解析疑似数据
total_suspect_data={}
for item in num:
    if item['name'] not in total_suspect_data:
        total_suspect_data.update({item['name']:0})
    for city_data in item['children']:
        total_suspect_data[item['name']]+=int(city_data['total']['suspect'])
print(total_suspect_data)
#解析死亡数据

total_dead_data={}
for item in num:
    if item['name'] not in total_dead_data:
        total_dead_data.update({item['name']:0})
    for city_data in item['children']:
        total_dead_data[item['name']]+=int(city_data['total']['dead'])
print(total_dead_data)

#解析治愈数据
total_heal_data={}
for item in num:
    if item['name'] not in total_heal_data:
        total_heal_data.update({item['name']:0})
    for city_data in item['children']:
        total_heal_data[item['name']]+=int(city_data['total']['heal'])
print(total_heal_data)

#新增确诊数据

total_new_data={}
for item in num:
    if item['name'] not in total_new_data:
        total_new_data.update({item['name']:0})
    for city_data in item['children']:
        total_new_data[item['name']]+=int(city_data['today']['confirm'])
print(total_new_data)
'''
names = list(total_data.keys())
num1 =  list(total_data.values())
num2 = list(total_suspect_data.values())
num3 = list(total_dead_data.values())
num4 = list(total_heal_data.values())
num5 = list(total_new_data.values())

n=time.strftime("%Y-%m-%d")+ "-all.csv"
fw = open(n,'w',encoding='utf-8')
fw.write('province,confirm,dead,heal,new_confirm\n')
i =0
while i<len(names):
    fw.write(names[i] + ',' + str(num1[i]) + ',' + str(num3[i]) + ',' + str(num4[i]) + ',' + str(num5[i]) + '\n')
    i = i + 1
else:
    print("Over write file!") #fw.close()别忘了
    
'''

import matplotlib
import numpy as np
import seaborn as sns
import  pandas as pd
import matplotlib.pyplot as plt
n =time.strftime("%Y-%m-%d")+"-all-4db-2no.csv"
data = pd.read_csv(n)

fig,ax=plt.subplots(1,1)
print(data['province'])

sns.set_style("whitegrid",{'font.sans-serif':['simhei','Arial']})
g = sns.barplot(x="province", y="data", hue="tpye", data=data, ax=ax,
            palette=sns.color_palette("hls", 8))
ax.set_title('全国疫情最新情况')
ax.set_xticklabels(ax.get_xticklabels(), rotation=-60)
ax.tick_params(axis='x',labelsize=8)
ax.tick_params(axis='y',labelsize=8)
plt.show()