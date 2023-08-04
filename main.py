import csv

dayIndex = 0
monthIndex = 1
yearIndex = 2
casesIndex = 3
deathsIndex = 4
countryIndex = 5
populationIndex = 7
continentIndex = 8

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
        if left[leftIndex][countryIndex] < right[rightIndex][countryIndex]:
            sortedList.append(left[leftIndex])
            leftIndex += 1
        elif left[leftIndex][countryIndex] > right[rightIndex][countryIndex]:
            sortedList.append(right[rightIndex])
            rightIndex += 1
        else:
            if left[leftIndex][2] < right[rightIndex][2]:
                sortedList.append(left[leftIndex])
                leftIndex += 1
            elif left[leftIndex][2] > right[rightIndex][2]:
                sortedList.append(right[rightIndex])
                rightIndex += 1
            else:
                if left[leftIndex][1] < right[rightIndex][1]:
                    sortedList.append(left[leftIndex])
                    leftIndex += 1
                elif left[leftIndex][1] > right[rightIndex][1]:
                    sortedList.append(right[rightIndex])
                    rightIndex += 1
                else:
                    if left[leftIndex][0] < right[rightIndex][0]:
                        sortedList.append(left[leftIndex])
                        leftIndex += 1
                    else:
                        sortedList.append(right[rightIndex])
                        rightIndex += 1

    sortedList.extend(left[leftIndex:])
    sortedList.extend(right[rightIndex:])
    return sortedList

def sentinelLinearSearch(covidList, day, month, year, country):
    sentinel = [day, month, year, "", "", country, "", "", "", ""]
    covidList.append(sentinel)

    i = 0
    while True:
        if covidList[i][dayIndex] == sentinel[0] and covidList[i][monthIndex] == sentinel[1] and covidList[i][yearIndex] == sentinel[2] and covidList[i][countryIndex] == sentinel[5]:
            if i == len(covidList) - 1: # reaches sentinel value, pop it
                covidList.pop()
                return -1
            else:
                covidList.pop()
                print(i)
                return covidList[i]
        i += 1


def ternarySearch(covidList, day, month, year, country):
    left, right = 0, len(covidList) - 1

    while left <= right:
        tern1 = left + (right - left) // 3
        tern2 = right - (right - left) // 3

        if covidList[tern1][dayIndex] == day and covidList[tern1][monthIndex] == month and covidList[tern1][yearIndex] == year and covidList[tern1][countryIndex] == country:
            return covidList[tern1]
        if covidList[tern2][dayIndex] == day and covidList[tern2][monthIndex] == month and covidList[tern2][yearIndex] == year and covidList[tern2][countryIndex] == country:
            return covidList[tern2]
        
        if covidList[tern1][countryIndex] > country or (covidList[tern1][countryIndex] == country and covidList[tern1][yearIndex] > year) or (covidList[tern1][countryIndex] == country and covidList[tern1][yearIndex] == year and covidList[tern1][monthIndex] > month) or (covidList[tern1][countryIndex] == country and covidList[tern1][yearIndex] == year and covidList[tern1][monthIndex] == month and covidList[tern1][dayIndex] > day):
            right = tern1 - 1
        elif covidList[tern2][countryIndex] < country or (covidList[tern2][countryIndex] == country and covidList[tern2][yearIndex] < year) or (covidList[tern2][countryIndex] == country and covidList[tern2][yearIndex] == year and covidList[tern2][monthIndex] < month) or (covidList[tern2][countryIndex] == country and covidList[tern2][yearIndex] == year and covidList[tern2][monthIndex] == month and covidList[tern2][dayIndex] < day):
            left = tern2 + 1
        else:
            left = tern1 + 1
            right = tern2 - 1
    
    return -1

def printList(covidList):
    for i in covidList:
        print(i)

def main():
    with open('covid.csv', 'r') as csv_file:
        covid_csv = csv.reader(csv_file)
        next(covid_csv) # skip header line
        covidList = []
        for line in covid_csv:
            covidList.append(line)

    linearCovid = sentinelLinearSearch(covidList, "31", "12", "2019", "Afghanistan")
    print(linearCovid)

    sortedCovid = mergeSort(covidList)   #sorts countries
    ternaryCovid = ternarySearch(sortedCovid, "31", "12", "2019", "Afghanistan")
    print(ternaryCovid)

    
if __name__ == "__main__":
    main()