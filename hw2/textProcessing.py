# only math, collections, re, and csv

import math
import re
import collections
import csv

def clean(fileName):
    
    f = open(fileName, "r")
    documentList = []
    for line in f:
        #strip all the /n in all the doc1.txt/n
        documentList.append(line.strip())
    
    print(documentList)
    
    for doc in documentList:
        print(doc)
        openDoc = open(doc,'r')
        
        for line in openDoc:
            tempStr = ""
            allwords=line.split(" ")
            # print(line)
            # print(allwords)
            editedWords=[]
            wordTotal = len(allwords)
            i = 0
            for word in allwords:
                i = i + 1
                w = word
                # first remove the link, or else we cannot detect the :// when we removed them
                # Remove all website links. A website link is a sequence of non-whitespace
                # characters that starts with either http:// or https://.
                if re.match(r'^https://', w) or re.match(r'^http://',w):
                    w = ""
                    
                # Remove all characters that are not words or whitespace. Words are sequences
                # of letters (upper and lower case), digits, and underscores.
                
                # print(re.sub("[^a-zA-Z0-9_]+", "", "|}|{hell$#%$@%$&^o123_**"))
                
                # first parameter is the matching regex
                # second parameter is the elements that are swapping out the regex
                # third parameter is the input string
                # the regrex means the group of characters that is NOT a to z or A to Z or digits or underscore
                w = re.sub("[^a-zA-Z0-9_]", "", w)
                
                # Remove extra whitespace between words, so that there is exactly one whites-
                # pace character between any pair of words.
                
                # Convert all the words to lowercase.
                w = w.lower()
                # The resulting document should only contain lowercase words separated by a
                # single whitespace character.
                
                if w != "":
                    editedWords.append(w)
                    if i != wordTotal:
                         tempStr += w+" "
                    else:
                        tempStr += w
                    
            print("cleaned:",editedWords)
            print("sentense:", tempStr)
                
            
    f.close()
    
    pass

# current implemention : for this fileName input we remove all stop words and then return
def removeStop(fileName):
    stopWords = []
    s = open("stopwords.txt","r")
    for st in s:
        stopWords.append(st.strip())
    print(stopWords)
    f = open(fileName, "r")
    
    for line in f:
        allwords = line.split(" ")
        tempStr = ""
        editedWords = []
        wordTotal = len(allwords)
        i=0
        for word in allwords:
            i = i+1
            w = word
            if w in stopWords:
                # print("found",w)
                w = ""
        
            if w != "":
                if i != wordTotal:
                    tempStr += w+" "
                else:
                    tempStr += w
                editedWords.append(w)
        
        # print(line)
        # print(editedWords)
        # print(tempStr)
        # print(allwords)
    
    f.close()
    pass
    
def stemAndLemma(fileName):
    
    f = open(fileName, "r")
    for line in f:
        allwords = line.split(" ")
        wordTotal = len(allwords)
        i = 0
        editedWords = []
        tempStr = ""
        for word in allwords:
            i = i + 1
            w = word
            # •Words ending with “ing”: “flying” becomes “fly”
            # •Words ending with “ly”: “successfully” becomes “successful”
            # •Words ending with “ment”: “punishment” becomes “punish”
            w = re.sub("(ing|ly|ment)$" , "", w)
            
            if w != "":   
                editedWords.append(w)
                if i != wordTotal:
                    tempStr += w+" "
                else:
                    tempStr += w
        # print(editedWords)
        # print(tempStr)
    f.close()
    pass

def tfidf(fileName):
    d = open(fileName, "r")
    documentList = []
    for line in d:
        #strip all the /n in all the doc1.txt/n
        documentList.append(line.strip())
    d.close()
    
    print(documentList)
    docNum = 0
    tf = 0
    idf = 0
    
    wordShowsUpInHowManyDoc = {}
    wordFreqInEachDoc = []
    tfInEachDoc = []
    
    for doc in documentList:
        canRecordWord = 0
        
        docNum += 1
        print("doc",docNum)
        f = open(doc,"r")
        # for each of the process document
        
        # pretend for 1 document
        dict={}
        wordCount = 0
        
        for line in f:
            # print(line)
            allwords=line.split(" ")
            for word in allwords:
                wordCount = wordCount + 1
                w=word.strip()
                if w != "" :
                    if(dict.get(w)==None):
                        # if a word is not checked in the current document
                        # that means this word did not count toward wordshowsupinhowmanyDoc
                        # this is the first time word shows up in a doc
                        if(wordShowsUpInHowManyDoc.get(w)!=None):
                            wordShowsUpInHowManyDoc[w] = wordShowsUpInHowManyDoc[w] + 1
                        else:
                            wordShowsUpInHowManyDoc[w] = 1
                        dict[w]=1
                    else:
                        dict[w]=dict[w] + 1
                        
                
                    
        tfDict={}
        print("word count for this doc", wordCount)
        print(dict)
    
        for word, freq in dict.items():
            tfDict[word] = round(float( freq / wordCount ),2)
                
        print(tfDict)
        # save the word freq into master list
        wordFreqInEachDoc.append(dict)
        # save the tf socre for each doc into master list
        tfInEachDoc.append(tfDict)
        f.close()
        print("\n")
    # after looping out all documents
    # we have 
    print("word shows up in how many doc:", wordShowsUpInHowManyDoc)
    
    # compute IDF for each doc
    idfMasterList = []
    
    for wordFreq in wordFreqInEachDoc:
        idfPerDoc = {}
        # each wordFreq is a dict that stores the word and frequency at that doc
        idf = 0
        for word, freq in wordFreq.items():
            idfPerDoc[word] = math.log(float(docNum / wordShowsUpInHowManyDoc.get(word)))
        idfMasterList.append(idfPerDoc)
        
    print("idf", idfPerDoc)
    
    # compute TD-IDF
    print(len(idfMasterList), len(tfInEachDoc))
    
    for i in len(idfMasterList):
        # these should correspond to the same document
        tempidf = idfMasterList[i]
        temptf = tfInEachDoc[i]
        

    
    pass

def main():
    # part 1
    fileName = "tfidf_docs.txt"
    doc1 = "doc1.txt"
    doc2 = "doc2.txt"
    doc3 = "doc3.txt"
    doc4 = "doc4.txt"
    testTFIDF = "testTFIDF.txt"
    # clean(fileName)
    # removeStop("doc3.txt")
    # stemAndLemma("doc3.txt")
    
    # write to whatever
    
    # part 2
    tfidf(testTFIDF)


    

main()