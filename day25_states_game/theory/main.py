# with open("weather_data.csv") as file:
#     weather_list = file.readlines()
#     print(weather_list)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     next(data_file)  # skip header
#     for row in data:
#         temperature.append(int(row[1]))
#     print(temperature)


import pandas
# data = pandas.read_csv("weather_data.csv")

# temp_list = data["temp"].to_list()
# print(temp_list)  # same as above, but way shorter using pd
# temp_mean = round(sum(temp_list) / len(temp_list), 2)
# print(temp_mean)

# print(data["temp"].mean())  # same result using build in pandas.Series.mean

# print(data.temp.max())  # can use data.header just like data["header"], work the same

# print(data[data.day == "Monday"])  # can give the information from a row if given the header and the row name

# print(data[data.temp == data.temp.max()])  # give me the row with the highest temp

# monday = data[data.day == "Monday"]  #create a variable that can be used
# monday.condition # give the weather condition of monday

# monday_temp = data[data.day == "Monday"]
# print(monday_temp.temp[0])  # just taking the raw number, not the data_frame
# print((monday_temp.temp[0]*9/5) + 32)  # put in F instead of C

data = pandas.read_csv("squirrel_data.csv")

gray_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Number Of Squirrel": [gray_squirrel, cinnamon_squirrel, black_squirrel]
}

print(data_dict)

df = pandas.DataFrame(data_dict)
df.to_csv("fur_color.csv")



