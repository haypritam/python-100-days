import pandas

furColor = ["Gray","Cinnamon","Black"]
count = [0,0,0]
dict = {'fur color': furColor, 'count': count} 
data=pandas.read_csv("Squirrel_Data.csv")
data_dist=data.to_dict()
for i in range(len(data_dist["Primary Fur Color"])):
    if data_dist["Primary Fur Color"][i]=="Gray":
        count[0]+=1
    elif data_dist["Primary Fur Color"][i]=="Cinnamon":
        count[1]+=1
    elif data_dist["Primary Fur Color"][i]=="Black":
        count[2]+=1


df = pandas.DataFrame(dict)

df.to_csv('sCount.csv')