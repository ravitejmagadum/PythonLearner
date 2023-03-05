import csv
import pandas as pd

""""without using pandas"""
# with open("weather_data.csv", "r") as data:
#     data = csv.reader(data)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#
#     print(temperature)
#
#
""""with using pandas"""
# data = pandas.read_csv("weather_data.csv")
# print(data['temp'])


"""exercise  to extract colour and its count"""
# print(pd.__version__)
squirrel = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# grays = ((squirrel['Primary Fur Color'] == 'Gray'))
# gray_count = 0
# for n in grays:
#     if n == True:
#         gray_count += 1
#
# print(gray_count)
#
# black = ((squirrel['Primary Fur Color'] == 'Black'))
# black_count = 0
# for n in black:
#     if n == True:
#         black_count += 1
#
# print(black_count)

#
# red = ((squirrel['Primary Fur Color'] == 'Red'))
# red_count = 0
# for n in red:
#     if n == True:
#         red_count += 1
#
# print(red_count)
#
#
# pd.DataFrame(['Gray', gray_count], ['Black', black_count]).to_csv('colour count.csv')


print(len(squirrel[squirrel['Primary Fur Color'] == 'Gray']))