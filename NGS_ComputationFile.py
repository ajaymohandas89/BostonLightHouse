from allImportsFile import csv,collections

"""
input type: csv dataset
return type: dictionary
description: function to read csv data and return dictionary of start and length of DNC sequence 
             and dictionary to count of this basepair 
"""
def readData(dataset):
  basePairMap = collections.defaultdict(list)
  coverageCountMap = {}

  for start, length in dataset:
    s = start[:-3]                                                       #slicing the input
    basePair = str(int(start) + int(length))                             #calculate the start + maximum length of sequence
    if (start, basePair) not in coverageCountMap:
      basePairMap[s] += [(start, basePair)]
      coverageCountMap[(start, basePair)] = 1
    else:
      coverageCountMap[(start, basePair)] += 1
  return basePairMap,coverageCountMap

"""
input type: csv dataset
return type: list
description: function to read csv data and return list of DNA position
"""
def getLociList(dataset):
  positionList = []
  for data in dataset:
    positionList.append(data[0])
  return positionList

"""
input argument
1) lociDataWriter: dataset of Loci csv file
2) positionList: list of DNA position to be found in read csv file
3) basePairMap: Dictionary of DNA start and length
4) coverageCountMap: Dictionary of DNA start and length and value as count present in read file 
return type: void
description: function to write the coverage to DNA positon
"""
def compute(lociDataWriter,positionList,basePairMap,coverageCountMap):
  for pos in positionList:
    count = 0
    d = pos[:-3]
    li = basePairMap.get(d)
    if li == None:
      lociDataWriter.writerow([pos, str(0)])
      continue
    for val in li:
      min = int(val[0])
      max = int(val[1])
      if int(pos) >= int(min) and int(pos) <= max:
        count += coverageCountMap.get((val[0], val[1]))
    lociDataWriter.writerow([pos, str(count)])
