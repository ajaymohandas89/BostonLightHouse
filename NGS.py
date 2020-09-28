from allImportsFile import *
from csvFileParse import *
from NGS_ComputationFile import *

if __name__ =="__main__":
  try:
    readDataSet = readFile('reads')                                          #Read reads.csv file
    print("read.csv file successfully read")
  except:
    print("Error found at csvFileParse.py error")

  basePairMap,coverageCountMap = readData(readDataSet)                     #Parse data present in read.csv
  print("read.csv file parsed successfully")
  print("")

  try:
    lociDataSet = readFile('loci')                                           #Read loci.csv
    print("loci.csv file successfully read")
  except:
    print("Error found at csvFileParse.py error")

  positionList = getLociList(lociDataSet)                                  #Get a list of DNA positions
  print("Successfully parsed loci data to get list of DNA position")
  print("")

  titleFields = ['postion', 'coverage']                                    #Declaring title in loci csv file
  try:
    lociDataWriter = writeFile('loci')
    lociDataWriter.writerow(titleFields)
  except:
    print("Error found at csvFileParse.py error")

  compute(lociDataWriter,positionList,basePairMap,coverageCountMap)        #Computing coverage of DNA positions
  print("Coverage added successfully in loci.csv")
