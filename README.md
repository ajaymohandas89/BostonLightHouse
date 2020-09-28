# BostonLightHouse
## Problem Definition: Calculating genomic coverage from next-generation sequencing data

### Pre-requisites:
1)	Install [python](https://www.python.org/downloads/) to run python program

### Steps to run:
1)	Copy the python files to any directory
2)	The reads.csv and loci.csv must be present inside “data” folder and data folder must be present where all python files are present
3)	To run the NGS.py on cmd type python NGS.py/python3 NGS.py as per python version installed
4)	If you want to run the python script on IDE then skip step 3 and install IDE of your preference run he NGS.py file 

### Approach 2:
1)	Pre-process the data of reads.csv and stored it in dictionary (Map interface) where key is pattern which is sliced from the start position of DNA.
For instance if start is “101843359”, so key stored is “101843” which is seen as a common pattern in entire reads.csv
The value is set of start position and maximum length of base pair

Example:
Start 			Length
101843359		151

Then dictionary would be {“101843”:[(“ 101843359”,” 101843510”)]}
2)	A second dictionary is used to store the count of this sit(“ 101843359”,” 101843510”). This count is used to add while computing the coverage
3)	For computing the coverage for a position, we get a list of the pattern and from dictionary we return the list and check if position lies in that coverage and increment the count value

### Merits of approach 2:
1)	We are pre-processing millions of data and storing it in dictionary. The time complexity of getting a key from dictionary is O(1)  and putting a value is also O(1)
2)	Thus the search complexity is drastically reduced comparing to Approach 1

### Time complexity for approach 2:
1)	Let “n” be size of data in reads.csv, ”k” be size of data in loci.csv
2)	Time taken to read entire reads.csv file is O(n)
3)	Time taken to read loci.csv file is O(k)
4)	Time to write a row in csv is constant
5)	Time to compute is size O(k*m) where m is length of dictionary value list for that position

Total time complexity for average case is O(n + k + k*m)
