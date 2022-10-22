# only math, collections, re, and csv

import math
import re
import collections
import csv



# id,    name,    level,  personality,  type,     weakness,  atk,     def,    hp,    stage
# 53.0,  Persian, 40.0,   mild,         normal,   fighting,  104.0,   116.0,  NaN,   2.0
# 126.0, Magmar,  44.0,   docile,       NaN,      water,     96.0,    83.0,   153.0, 1.0

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
    countOfPokemonOver40 = 0
    with open(fileName, 'r') as f:
        next(f)
        for line in f:
            l = line.rstrip('\n').split(',')
            # above lv 40
            if (float(l[2]) > 40):
                countOfPokemonOver40 += 1
                # attack/def/hp is not NaN
                if (l[6] != "NaN"):
                    avgAtkAbove40 += float(l[6])
                if (l[7] != "NaN"):
                    avgDefAbove40 += float(l[7])
                if (l[8] != "NaN"):
                    avgHpAbove40 += float(l[8])

    avgAtkAbove40 = round(avgAtkAbove40 / countOfPokemonOver40, 1)
    avgDefAbove40 = round(avgDefAbove40 / countOfPokemonOver40, 1)
    avgHpAbove40 = round(avgHpAbove40 / countOfPokemonOver40, 1)

    avgAtkUnder40 = 0
    avgDefUnder40 = 0
    avgHpUnder40 = 0
    countOfPokemonUnder40 = 0
    with open(fileName, 'r') as f:
        next(f)
        for line in f:
            l = line.rstrip('\n').split(',')
            # Under lv 40
            if (float(l[2]) <= 40):
                countOfPokemonUnder40 += 1
                # attack/def/hp is not NaN
                if (l[6] != "NaN"):
                    avgAtkUnder40 += float(l[6])
                if (l[7] != "NaN"):
                    avgDefUnder40 += float(l[7])
                if (l[8] != "NaN"):
                    avgHpUnder40 += float(l[8])

    avgAtkUnder40 = round(avgAtkUnder40 / countOfPokemonUnder40, 1)
    avgDefUnder40 = round(avgDefUnder40 / countOfPokemonUnder40, 1)
    avgHpUnder40 = round(avgHpUnder40 / countOfPokemonUnder40, 1)
    
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


def main():
    fileName = "pokemonTrainTrash.csv"
    # part 1
    # percentOfFireAbove40(fileName)

    # part2
    missingTypeBasedOnHighestWeaknessType(fileName)

    # part3
    avgAtkDefHp("pokemonResult.csv")
    pass


main()
