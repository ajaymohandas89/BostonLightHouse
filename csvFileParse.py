from allImportsFile import csv,os

"""
input type: string
return type: csv dataset
description: function to read data present in the file
"""
def readFile(fileName):
  try:
    csvFilePath = "./data/"+fileName+".csv"
    csvFile = open(csvFilePath,'r',newline = '')
    dataset = csv.reader(csvFile)
    next(dataset)
    return dataset
  except:
    print("CSV file not found")

"""
input type: string
return type: csv dataset
description: function to write data present in the file
"""
def writeFile(fileName):
  try:
    csvFilePath = "./data/"+fileName+".csv"
    csvFile = open(csvFilePath, 'w', newline='')
    dataset = csv.writer(csvFile)
    return dataset
  except:
    print("csvFileParse.py error")
    print("writeFile() --> File not found")

