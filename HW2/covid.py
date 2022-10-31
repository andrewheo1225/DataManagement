def findCutOff(a):
    #  first sort the array from smallest to biggest
    print(type(a))
    n = len(a)
    checkPoint = n
    a.sort() 
    print(a)
    for i in range(n):
        print(a[i],10*checkPoint)
        if(a[i] > 10*checkPoint):
            
            print(checkPoint)
            return checkPoint
        else:
            checkPoint = checkPoint - 1
    
    return "no solution"

def question3(a):
    dict = {}
    itemIndex = {}
    curIndex = 0
    for stuff in a:
        if(dict.get(stuff)!=None):
            dict[stuff] = dict[stuff] + 1
            if(dict[stuff]>=100 and ( curIndex - itemIndex[stuff] +1 ==  len(a)/5)):
                # print(itemIndex[stuff],curIndex)
                return (itemIndex[stuff],curIndex)
        else:
            dict[stuff] = 1
            itemIndex[stuff] = curIndex
        # at end of loop increase the index
        curIndex = curIndex+1
    return "no solution"
        
        
def afk(arr):
    dict = {}
    total = 0
    index = 0
    
    for a in arr:
        total += a
        if(total == 100):
            return (0,index)
        
        print(total, total-100)
        if(dict.get(total-100) != None):
            print("found")
            print(dict)
            j = dict.get((total-100))
            return (j , index)
        else:
            dict[total] =  index
            
        index = index + 1
    return "no solution"
        


arr = [0, 2, 61, 45, 9, 38, 82, 40, 13, 26, 51, 77, 5]

a = [3,3,3,1,2,3]

b = [2,5,25,25,50]
# findCutOff(arr)
# print(question3(a))

print(afk(b))
    
        
   
