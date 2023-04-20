# main.py

# Name: Nicole Price
# email: pricenm@mail.uc.edu
# Assignment Title: Assignment 06
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: 
# Citations: https://catalog.data.gov/dataset/crime-data-from-2020-to-present
# Anything else that's relevant: 

from functionsPackage.functions import *
from pip._vendor.urllib3 import response

data = read_CSV_file("Tax_Lien_Sale_Lists.csv")

lotNumber = set([row[4] for row in data]) # determines what column we are working with

maxLot = []
for lot in lotNumber:
    maxLotNumber = list(map(int, lotNumber)) # converts the list of strings to a list of ints
    maxLot = max(maxLotNumber) # finds the max int in the list
print(maxLot)

maxNumber = [int(i) for i in lotNumber] # converts the list of strings to a list of ints
print(max(maxNumber))

streetName = set([row[10] for row in data]) # determines what column we are working with and removes duplicates
# print(streetName) # used this originally to check that no duplicates printed
print(len(streetName)) # I am so paranoid I did a remove duplicates on this to make sure the number was correct 
N = 5
top5 = [x for index, x in enumerate(streetName) if index < N]
print(top5)
