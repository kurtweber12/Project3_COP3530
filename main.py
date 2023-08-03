import csv

def mergeSort(covidList, catIndex):
    if len(covidList) <= 1:
        return covidList
    
    mid = len(covidList) // 2
    left = covidList[:mid]
    right = covidList[mid:]

    left = mergeSort(left, catIndex)
    right = mergeSort(right, catIndex)

    return merge(left, right, catIndex)

def merge(left, right, catIndex):
    sortedList = []
    leftIndex, rightIndex = 0, 0

    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex][catIndex] < right[rightIndex][catIndex]:
            sortedList.append(left[leftIndex])
            leftIndex += 1
        else:
            sortedList.append(right[rightIndex])
            rightIndex += 1

    sortedList.extend(left[leftIndex:])
    sortedList.extend(right[rightIndex:])
    return sortedList

def sentinelLinearSearch(covidList, catIndex, key):
    returnList = []
    #last = covidList[len(covidList) - 1][catIndex]
    #covidList[len(covidList) - 1][catIndex] = key
    flag = True
    try:
        int(key)
    except ValueError:
        flag = False

    if (flag):
        key = str(key)
        for i in range(0, len(covidList)):
            temp = covidList[i][catIndex]
            if (key in temp):
                returnList.append(covidList[i])
    else:
        for i in range(0, len(covidList)):
            temp = covidList[i][catIndex]
            if (key.casefold() in temp.casefold()):
                returnList.append(covidList[i])    
    
    return returnList

def ternarySearch(covidList, catIndex, key):
    left, right = 0, len(covidList) - 1
    returnList = []

    while left <= right:
        thirdSize = (right - left) // 3
        tern1 = left + thirdSize
        tern2 = right - thirdSize

        if key.casefold() in covidList[tern1][catIndex].casefold():
            returnList.append(covidList[tern1])
            tempUp = tern1 + 1
            tempDown = tern1 - 1
            while (tempUp < len(covidList) and key.casefold() in covidList[tempUp][catIndex].casefold()):
                returnList.append(covidList[tempUp])
                tempUp += 1
            while (tempDown >= 0 and key.casefold() in covidList[tempDown][catIndex].casefold()):
                returnList.append(covidList[tempDown])
                tempDown -= 1
        if key.casefold() in covidList[tern2][catIndex].casefold():
            returnList.append(covidList[tern2])
            tempUp = tern2 + 1
            tempDown = tern2 - 1
            while (tempUp < len(covidList) and key.casefold() in covidList[tempUp][catIndex].casefold()):
                returnList.append(covidList[tempUp])
                tempUp += 1
            while (tempDown >= 0 and key.casefold() in covidList[tempDown][catIndex].casefold()):
                returnList.append(covidList[tempDown])
                tempDown -= 1
        
        if key.casefold() < covidList[tern1][catIndex].casefold():
            right = tern1 - 1
        elif key.casefold() > covidList[tern2][catIndex].casefold():
            left = tern2 + 1
        else:
            left = tern1 + 1
            right = tern2 - 1

    return returnList


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


    keyType = type(8)
    linearCovid = sentinelLinearSearch(covidList, 8, "America")
    sortedCovid = mergeSort(covidList, 8)
    ternaryCovid = ternarySearch(sortedCovid, 8, "America")
    
    printList(ternaryCovid)
    #printList(linearCovid)
    #print("hello")
    
if __name__ == "__main__":
    main()