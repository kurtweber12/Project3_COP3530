import csv
import time

# indexes of csv file for easier manageability
dayIndex = 0
monthIndex = 1
yearIndex = 2
casesIndex = 3
deathsIndex = 4
countryIndex = 5
populationIndex = 7
continentIndex = 8

def read_csv():
    with open('../covid.csv', 'r') as csv_file:
        covid_csv = csv.reader(csv_file)
        next(covid_csv) # skip header line
        covidList = []
        for line in covid_csv:
            covidList.append(line)

    return covidList

def mergeSort(covidList):
    if len(covidList) <= 1:
        return covidList
    
    mid = len(covidList) // 2
    left = covidList[:mid]
    right = covidList[mid:]

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)

def merge(left, right):
    sortedList = []
    leftIndex, rightIndex = 0, 0

    while leftIndex < len(left) and rightIndex < len(right):
        # sort by country
        if left[leftIndex][countryIndex] < right[rightIndex][countryIndex]:
            sortedList.append(left[leftIndex])
            leftIndex += 1
        elif left[leftIndex][countryIndex] > right[rightIndex][countryIndex]:
            sortedList.append(right[rightIndex])
            rightIndex += 1
        else:
            # sort by year
            if left[leftIndex][yearIndex] < right[rightIndex][yearIndex]:
                sortedList.append(left[leftIndex])
                leftIndex += 1
            elif left[leftIndex][yearIndex] > right[rightIndex][yearIndex]:
                sortedList.append(right[rightIndex])
                rightIndex += 1
            else:
                # sort by month
                if left[leftIndex][monthIndex] < right[rightIndex][monthIndex]:
                    sortedList.append(left[leftIndex])
                    leftIndex += 1
                elif left[leftIndex][monthIndex] > right[rightIndex][monthIndex]:
                    sortedList.append(right[rightIndex])
                    rightIndex += 1
                else:
                    # sort by day
                    if left[leftIndex][dayIndex] < right[rightIndex][dayIndex]:
                        sortedList.append(left[leftIndex])
                        leftIndex += 1
                    else:
                        sortedList.append(right[rightIndex])
                        rightIndex += 1

    sortedList.extend(left[leftIndex:])
    sortedList.extend(right[rightIndex:])
    return sortedList

def sentinelLinearSearch(covidList, day, month, year, country):
    # append sentinel value to the end of list
    sentinel = [day, month, year, "", "", country, "", "", "", ""]
    covidList.append(sentinel)

    i = 0
    while True:
        time.sleep(0.00001)
        if covidList[i][dayIndex] == sentinel[0] and covidList[i][monthIndex] == sentinel[1] and covidList[i][yearIndex] == sentinel[2] and covidList[i][countryIndex] == sentinel[5]:
            if i == len(covidList) - 1: # reaches sentinel value, pop it (values not found in list)
                covidList.pop()
                return -1
            else:   # values have been found, return list at found index
                covidList.pop()
                return covidList[i]
        i += 1


def ternarySearch(covidList, day, month, year, country):
    left, right = 0, len(covidList) - 1

    while left <= right:
        time.sleep(0.00001)
        # divide into thirds
        tern1 = left + (right - left) // 3
        tern2 = right - (right - left) // 3

        # if found, return
        if covidList[tern1][dayIndex] == day and covidList[tern1][monthIndex] == month and covidList[tern1][yearIndex] == year and covidList[tern1][countryIndex] == country:
            return covidList[tern1]
        if covidList[tern2][dayIndex] == day and covidList[tern2][monthIndex] == month and covidList[tern2][yearIndex] == year and covidList[tern2][countryIndex] == country:
            return covidList[tern2]
        
        # check which region list is in
        # if list is within the left and first ternary
        if covidList[tern1][countryIndex] > country or (covidList[tern1][countryIndex] == country and covidList[tern1][yearIndex] > year) or (covidList[tern1][countryIndex] == country and covidList[tern1][yearIndex] == year and covidList[tern1][monthIndex] > month) or (covidList[tern1][countryIndex] == country and covidList[tern1][yearIndex] == year and covidList[tern1][monthIndex] == month and covidList[tern1][dayIndex] > day):
            right = tern1 - 1
        # if list is within the second ternary and right
        elif covidList[tern2][countryIndex] < country or (covidList[tern2][countryIndex] == country and covidList[tern2][yearIndex] < year) or (covidList[tern2][countryIndex] == country and covidList[tern2][yearIndex] == year and covidList[tern2][monthIndex] < month) or (covidList[tern2][countryIndex] == country and covidList[tern2][yearIndex] == year and covidList[tern2][monthIndex] == month and covidList[tern2][dayIndex] < day):
            left = tern2 + 1
        # if list is found within both ternaries
        else:
            left = tern1 + 1
            right = tern2 - 1
    # not found
    return -1

def printList(covidList):
    for i in covidList:
        print(i)

def uniqueCountries():
    covidList = read_csv()
    countries = set()
    for x in covidList:
        countries.add(x[countryIndex])
    return countries

def main(day, month, year, country):
    # params for search functions
    # covidList, day, month, year, country
    # {
    #     "day": "31",
    #     "month": "12",
    #     "year": "2019",
    #     "location": "Afghanistan"
    # }

    covidList = read_csv()  # reads in csv file
    sortedCovid = mergeSort(covidList)   #sorts countries

    # sentinel linear search
    start_time_linear = time.time() * 1000.0
    linearCovid = sentinelLinearSearch(sortedCovid, day, month, year, country)
    end_time_linear = time.time() * 1000.0
    linear_time = end_time_linear - start_time_linear

    # ternary search
    start_time_ternary = time.time() * 1000.0
    ternaryCovid = ternarySearch(sortedCovid, day, month, year, country)
    end_time_ternary = time.time() * 1000.0
    ternary_time = end_time_ternary - start_time_ternary

    # api needs list return, converts -1 to an empty list
    if linearCovid == -1:
        linearCovid = list()
    
    if ternaryCovid == -1:
        ternaryCovid = list()
    
    # returns to views.py
    return linearCovid, linear_time, ternaryCovid, ternary_time
