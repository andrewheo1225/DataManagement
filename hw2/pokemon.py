# only math, collections, re, and csv

import math
import re
import collections
import csv

def percentOfFireAbove40(fileName):
    numOfFire = 0
    numOfFireAndAbove40 = 0
    for line in open(fileName):
        l = line.rstrip('\n').split(',')
        if (l[4] == "fire"):
            numOfFire += 1
        if (l[4] == "fire" and float(l[2]) >= 40):
            numOfFireAndAbove40 += 1
    percent = round((float(numOfFireAndAbove40 / numOfFire)*100))
    f = open("pokemon1.txt", "w")
    f.write("Percentage of fire type pokemon at or above level 40 = " + str(percent))
    f.close()

    pass


# fill in the type section based on their weakness
# use the most common weankess type and in a tie use the one that appears first in alphabetical
def missingTypeBasedOnHighestWeaknessType(fileName):
    weak_type = {}
    with open(fileName, 'r') as f:
        next(f)
        for line in f:    
            l = line.rstrip('\n').split(',')
            if (l[4] != "NaN"):
                key = str(l[5]) + "-" + str(l[4])
                
                if key in weak_type.keys():
                    val = float(weak_type.get(key))
                    val+=1
                    weak_type[key] = val
                else:
                    weak_type[key] = 1
                
                    

    #print(weak_type,end="\n\n")
    r = csv.reader(open(fileName))
    lines = list(r)
        
    for row in lines[1:]: 
        dictOfProperWeakness = {}
        if(row[4] == "NaN"):
            #print(row,end ="\n")
            typeOfWeaknessNaN = row[5]
            #print(typeOfWeaknessNaN,end = "\n")
            for key,val in weak_type.items():   
                l = key.split('-')
                if(l[0] == typeOfWeaknessNaN):
                    dictOfProperWeakness[key] = val
           # print(dictOfProperWeakness,end = "\n")
            highVal = [k for k, v in dictOfProperWeakness.items() if v == max(dictOfProperWeakness.values())]
           # print(highVal,end = "\n")
            sortHighVal = sorted(highVal)
           # print(sortHighVal,end = "\n\n")
            sortHighValFirstElement = sortHighVal[0].split("-")
            row[4] = sortHighValFirstElement[1]
    
    writer = csv.writer(open('pokemonResult.csv', 'w'))
    writer.writerows(lines)
    pass

# the CountofPokemon increments even if they have NaN for atk/def/hp!!!!!
def avgAtkDefHp(fileName):
    # find avg atk/def/hp for pokemons > lv 40
    
    avgAtkAbove40 = 0
    avgDefAbove40 = 0
    avgHpAbove40 = 0
    countOfPokemonOver40Atk = 0
    countOfPokemonOver40Def = 0
    countOfPokemonOver40Hp = 0
    with open(fileName, 'r') as f:
        next(f)
        for line in f:
            l = line.rstrip('\n').split(',')
            # above lv 40
            if (float(l[2]) > 40):
                # attack/def/hp is not NaN
                if (l[6] != "NaN"):
                    avgAtkAbove40 += float(l[6])
                    countOfPokemonOver40Atk+=1
                if (l[7] != "NaN"):
                    avgDefAbove40 += float(l[7])
                    countOfPokemonOver40Def+=1
                if (l[8] != "NaN"):
                    avgHpAbove40 += float(l[8])
                    countOfPokemonOver40Hp+=1

    avgAtkAbove40 = round(avgAtkAbove40 / countOfPokemonOver40Atk, 1)
    avgDefAbove40 = round(avgDefAbove40 / countOfPokemonOver40Def, 1)
    avgHpAbove40 = round(avgHpAbove40 / countOfPokemonOver40Hp, 1)

    #same thing but for under lv <= 40
    avgAtkUnder40 = 0
    avgDefUnder40 = 0
    avgHpUnder40 = 0
    countOfPokemonUnder40Atk = 0
    countOfPokemonUnder40Def = 0
    countOfPokemonUnder40Hp = 0
    with open(fileName, 'r') as f:
        next(f)
        for line in f:
            l = line.rstrip('\n').split(',')
            # Under lv 40
            if (float(l[2]) <= 40):
                
                # attack/def/hp is not NaN
                if (l[6] != "NaN"):
                    avgAtkUnder40 += float(l[6])
                    countOfPokemonUnder40Atk +=1
                if (l[7] != "NaN"):
                    avgDefUnder40 += float(l[7])
                    countOfPokemonUnder40Def +=1
                if (l[8] != "NaN"):
                    avgHpUnder40 += float(l[8])
                    countOfPokemonUnder40Hp +=1

    avgAtkUnder40 = round(avgAtkUnder40 / countOfPokemonUnder40Atk, 1)
    avgDefUnder40 = round(avgDefUnder40 / countOfPokemonUnder40Def, 1)
    avgHpUnder40 = round(avgHpUnder40 / countOfPokemonUnder40Hp, 1)
    
    r = csv.reader(open(fileName))
    lines = list(r)

    for row in lines[1:]:
        if (float(row[2]) > 40):
            if (row[6] == "NaN"):
                row[6] = str(avgAtkAbove40)
            if (row[7] == "NaN"):
                row[7] = str(avgDefAbove40)
            if (row[8] == "NaN"):
                row[8] = str(avgHpAbove40)
        if (float(row[2]) <= 40):
            if (row[6] == "NaN"):
                row[6] = str(avgAtkUnder40)
            if (row[7] == "NaN"):
                row[7] = str(avgDefUnder40)
            if (row[8] == "NaN"):
                row[8] = str(avgHpUnder40)
      

    writer = csv.writer(open('pokemonResult.csv', 'w'))
    writer.writerows(lines)
    pass

# Create a dictionary that maps pokemon types to their personalities.
# This dictionary would map a string to a list of strings.
# no NaN type recorded
def dictMapTypesToPersonalities(fileName):
    typeToPer = {}
    i = 0 
    with open(fileName, 'r') as f:
        # skip first line
        next(f)
        for line in f:    
            l = line.rstrip('\n').split(',')
            # personality is at l[3]
            per = l[3]
            # type is at l[4]
            type = l[4]
            # make sure no repeat of types
            if typeToPer.get(type)== None:
                typeToPer[type]=[per]
            else:
                existPer = typeToPer.get(type)
                # make sure no repeat of personality
                if(per not in existPer):
                    typeToPer[type].append(per)
                    
    # open up new doc, get ready to write
    # get dict size
    f = open("pokemon4.txt", "w")    
    f.write("Pokemon type to personality mapping:\n\n")
    dictSize = len(typeToPer)
    # print(dictSize)
    lineCount = 0
    
    # loop a sorted dict (sorted the key)
    for key, val in sorted(typeToPer.items()):
        # assume we do not record NaN type
        if (key == "NaN"):
            continue
        lineCount = lineCount + 1
        # create string 
        tempStr = "{}:".format(key)
        # sort the personalties list
        #size of val
        listSize = len(val)
        perCount = 0
        # print(key+" has "+ str(listSize)+" element")
        for p in sorted(val):
            # check if it's the last element, we do not need a extra comaa at the end
            perCount = perCount + 1
            if(perCount != listSize):
                tempStr += " {},".format(p)
            else:
                tempStr += " {}".format(p)
        
        # print(tempStr)
        # write into a new doc
        if lineCount != dictSize:
            f.write("   "+tempStr+"\n")
        else:
            f.write("   "+tempStr)
    # close the doc
    f.close()
    pass

# Find out the average Hit Points (“hp”) for pokemon of stage 3.0.
# Your program should print the value as follows (replace . . . with value):         
def aveHitStageThree(fileName):
    ave = 0.0
    sum = 0.0
    pokemonStageThreeCount = 0
    with open(fileName, 'r') as f:
        next(f)
        for line in f:  
            l = line.rstrip('\n').split(',')
            # the HP is at l[8]
            hp = l[8]
            # print(hp)
            # the stage is at l[9]
            stage = l[9]
            # print(hp,stage)
            
            # if the pokemon is at stage 3
            if(stage == "3.0"):
                # print(hp,stage)
                #if the number exists instead of NaN
                # print(type(hp))
                if(hp != "NaN"):
                    # print(hp,stage)
                    pokemonStageThreeCount = pokemonStageThreeCount + 1
                    sum = sum + float(hp)

    f = open("pokemon5.txt", "w") 
    # print(pokemonStageThreeCount)
    if (pokemonStageThreeCount == 0 ):
        f.write("Average hit point for pokemon of stage 3.0 = 0")
        return 
    
    ave = round(float( sum / pokemonStageThreeCount ))
    
    # print(sum,pokemonStageThreeCount,ave)    
     
    tempStr = "Average hit point for pokemon of stage 3.0 = {}".format(ave)
    f.write(tempStr)
    f.close()
            

def main():
    #MUST CHANGE FILENAME PRIOR TO SUBMISSION. I JUST CREATED A TRASH CSV TO WORK WITH SMALLER VALUES
    fileName = "pokemonTrain.csv"
    # part 1
    percentOfFireAbove40(fileName)

    # part2
    missingTypeBasedOnHighestWeaknessType(fileName)

    # part3
    # assuming that there are at least 1 value for missing atk/defhp to prevent division by zero
    avgAtkDefHp(fileName)
    
    # part 4
    dictMapTypesToPersonalities(fileName)
    
    # part 5
    aveHitStageThree(fileName)
    
    pass


main()
