#Awad Shawl ams934 
#cc1871 cynthia chen
#Andrew Heo ayh35
#Peter Zihe Zhang zz475
import csv
import math
import re

csv_file = 'covidTrain.csv'


#separators for symptoms 
splitChars = "; |;"


# initializing the titles and rows list
fields = []
rows = []
with open(csv_file, 'r') as csv_file:
    # csv_reader = csv.reader(csv_file, delimiter=',')
    # creating a csv reader object
    csvreader = csv.reader(csv_file)
     
    # extracting field names through first row
    fields = next(csvreader)
 
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

    # dictionary for maintaing cities with province keys
    cityDict = {} 

    #dictionary for maintaining symptoms with province keys
    symptomDict ={}

    # dictionary for maintaining latitude and longitude with province keys
    latDict = {}
    lonDict = {}



    # running first iteration to create dictionary for city, latitude and longitude values
    for rowIndex, row in enumerate(rows[:]):

      for colIndex, col in enumerate(row):
        #dealing with city column
        if(colIndex == 3):
          if(col != "NaN"):
            # first check for province key then check for city key in that province
            if cityDict.get(rows[rowIndex][4]) != None:
              #if city exists then add to its count
              if cityDict.get(rows[rowIndex][4]).get(col) != None:
                cityDict[rows[rowIndex][4]].update({col: cityDict[rows[rowIndex][4]].get(col) + 1 })
              #if city does not exist create a key with city name and set value of count to 1  
              else:
                cityDict[rows[rowIndex][4]].update({col: 1})

            # if province does not exist  
            else:
              #city obviously occurs first time then give it value of 1
              cityDict[rows[rowIndex][4]] = {col : 1} 
             
              
        # dealing with latitude column and latDict
        if(colIndex == 6):
          if(not math.isnan(float(col))):
            if latDict.get(rows[rowIndex][4]) != None:
              latDict[rows[rowIndex][4]].append(float(col)) 
            else:
              latDict[rows[rowIndex][4]] = [float(col)]  
        

        # dealing with longitude column and lonDict
        elif(colIndex == 7):
          if(not math.isnan(float(col))):
            if lonDict.get(rows[rowIndex][4]) != None:
              lonDict[rows[rowIndex][4]].append(float(col)) 
            else:
              lonDict[rows[rowIndex][4]] = [float(col)]

        # dealing with symptom column
        elif(colIndex == 11):
          if(col != "NaN"):
            #checking and catering for if there are multiple symptoms in a single entry
            tempSymptoms = col
            tempSymptoms = re.split(splitChars, tempSymptoms)

            # first check for province key then check for symptom key in that province
            if symptomDict.get(rows[rowIndex][4]) != None:
              
              #iterating for all symptoms in entry
              for symptom in tempSymptoms:
                #if symptom already exists then add to its count
                if symptomDict.get(rows[rowIndex][4]).get(symptom) != None:
                  symptomDict[rows[rowIndex][4]].update({symptom: symptomDict[rows[rowIndex][4]].get(symptom) + 1 })
                #if city does not exist create a key with city name and set value of count to 1  
                else:
                  symptomDict[rows[rowIndex][4]].update({symptom: 1})

              
            # if province does not exist  
            else:
              #symptom obviously occurs first time then give it value of 1
              #iterating for all symptoms in entry
              for symptom in tempSymptoms:
                symptomDict[rows[rowIndex][4]] = {symptom : 1}               


            
                          



    for rowIndex, row in enumerate(rows[:]):
      # parsing each column of a row
      # print(f"Columns are: {row}")
      for colIndex, col in enumerate(row):
        # for dealing with age related values
        if(colIndex == 1):
          if("-") in col:
            ageVals = col.split("-")
            ageVals = list(map(int, ageVals))
            replaceVal = round(sum(ageVals)/len(ageVals))
            rows[rowIndex][colIndex] = replaceVal

        # dealing with city columns
        elif(colIndex == 3):
          if(col == "NaN"):
            cities = cityDict[rows[rowIndex][4]]
            
            #finding max Value with alphabetical sorting
            itemMaxValue = max(cities.items(), key=lambda x: x[1])
            listOfKeys = list()

            # Iterate over all the items in dictionary to find keys with max value
            for key, value in cities.items():
              if value == itemMaxValue[1]:
                listOfKeys.append(key)

            #sorting alphabetically and then replacing NaN with the value  
            listOfKeys = sorted(listOfKeys)  
            replaceVal = listOfKeys[0]
            rows[rowIndex][colIndex] = replaceVal


        # dealing with latitude column
        elif(colIndex == 6 ):
          if(math.isnan(float(col))):
            # round to 2 decimal places
            replaceVal = round(sum(latDict[rows[rowIndex][4]]) / len(latDict[rows[rowIndex][4]]), 2)
            rows[rowIndex][colIndex] = replaceVal
            
        #dealing with longitude column
        elif(colIndex == 7):
          if(math.isnan(float(col))):
            # round to 2 decimal places
            replaceVal = round(sum(lonDict[rows[rowIndex][4]]) / len(lonDict[rows[rowIndex][4]]), 2)
            rows[rowIndex][colIndex] = replaceVal

        # dealing with date columns changing from dd/mm/yyyy to mm/dd/yyyy
        elif(colIndex == 8 or colIndex == 9 or colIndex == 10):
          dateVals = col.split(".")
          replaceVal = dateVals[1] + '.' + dateVals[0] + '.' + dateVals[2]
          rows[rowIndex][colIndex] = replaceVal


        # dealing with city columns
        elif(colIndex == 11):
          if(col == "NaN"):
            symptoms = symptomDict[rows[rowIndex][4]]
          
            #finding max Value with alphabetical sorting
            itemMaxValue = max(symptoms.items(), key=lambda x: x[1])
            listOfKeys = list()

            # Iterate over all the items in dictionary to find keys with max value
            for key, value in symptoms.items():
              if value == itemMaxValue[1]:
                listOfKeys.append(key)

            #sorting alphabetically and then replacing NaN with the value  
            listOfKeys = sorted(listOfKeys) 
            replaceVal = listOfKeys[0]
            rows[rowIndex][colIndex] = replaceVal

## writing results in covidResult.csv
with open('covidResult.csv', mode='w+') as result_file:
  result_writer = csv.writer(result_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  
  #for all column field names
  result_writer.writerow(fields)
  #for all rows data
  for row in rows:
    result_writer.writerow(row)