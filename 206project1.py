#William Waters
#discussed date/time with Austin McCall

import os
import filecmp

def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where 
#the keys will come from the first row in the data.

#Note: The column headings will not change from the 
#test cases below, but the the data itself will 
#change (contents and size) in the different test 
#cases.

	#Your code here:
	openfile = open(file)
	keylist = []
	dictlist = []
	i = 0
	for line in openfile:
		wordlist = []
		datadict = {}
		wordlist = line.strip().split(',')
		if (i == 0):
			for item in wordlist:
				keylist.append(item)
			i += 1
		else:
			j = 0
			for item in keylist:
				datadict[keylist[j]] = wordlist[j]
				j += 1
			dictlist.append(datadict)
	return dictlist

#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName

	#Your code here:
	sorteddata = sorted(data, key = lambda x : x[col])
	return sorteddata[0]["First"] + " " + sorteddata[0]["Last"]

#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g 
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	#Your code here:
	tuplelist = []
	num_seniors = 0
	num_juniors = 0
	num_sophomores = 0
	num_freshman = 0
	for item in data:
		if (item["Class"] == "Senior"):
			num_seniors += 1
		elif (item["Class"] == "Junior"):
			num_juniors += 1
		elif (item["Class"] == "Sophomore"):
			num_sophomores += 1
		else:
			num_freshman += 1
	tuplelist.append(('Senior', num_seniors))
	tuplelist.append(('Junior', num_juniors))
	tuplelist.append(('Sophomore', num_sophomores))
	tuplelist.append(('Freshman', num_freshman))
	return sorted(tuplelist, key = lambda x : x[1], reverse = True)

# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	dict_of_days = {}
	for person in a:
		dob = person['DOB']
		dob = dob.split('/')
		dob = dob[1]
		if dob in dict_of_days:
			dict_of_days[dob] = dict_of_days[dob] + 1
		else:
			dict_of_days[dob] = 1
	list_of_days = list(dict_of_days.items())
	list_of_days = sorted(list_of_days, key = lambda x:x[1], reverse = True)
	return int(list_of_days[0][0])

# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	total_years = 0
	total_peeps = 0
	#this uses system's current date/time
	import datetime
	now = str(datetime.datetime.now())
	date = now.split()[0]
	#create list of current date/time
	datelist = date.split("-")
	for person in a:
		dob = person["DOB"].split("/")
		age = int(datelist[0])-int(dob[2])
		if int(datelist[1])>int(dob[1]):
			age-=1
		total_years += age
		total_peeps += 1
	return int(round(total_years / total_peeps))

#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None

	#Your code here:
	sort_data = sorted(a, key = lambda x: x[col])
	file = open(fileName, "w", newline = "\n")
	for p in sort_data:
		file.write(p["First"] + "," + p["Last"] + "," + p["Email"] + "," + "\n")
	file.close()

################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)
	
	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()

