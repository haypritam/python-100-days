import pandas


# with open('weather_data.csv') as data:
#     data=csv.reader(data)
#     temperatures=[]
#     for row in data:
#         if row[1]!="temp":
#             temperatures.append(int(row[1]))
    

data=pandas.read_csv("weather_data.csv")
data_dict=data.to_dict()
temp_list=data['temp'].to_list()
print(data["temp"].mean())
print(data["temp"].max())