import math
import collections
import re
import csv

stopwords = []

def stopword():
    with open("stopwords.txt") as file:
        list = file.read()
        list = list.split('\n')
        for x in list:  
            stopwords.append(x)


def preprocess(docname):

    with open(docname, "r") as f:
        text = f.read()

    #clean:
    text = re.sub(r'(https://\w*.\w*\S*)', '', text) #remove links
    text = re.sub(r'\W', ' ', text) #remove nonword characters
    text = re.sub(r' +', ' ', text) #remove extra whitespace
    text = text.lower() #convert all to lowercase  

    #remove stopwords using stopwords.txt
    for x in stopwords:
        text = re.sub(rf'\b{x}\b', "", text)
        text = re.sub(r' +', ' ', text)
    #print(text)
    
    #stemming and lemmatization: return words to root forms
    matches = re.findall(r'\b(\w*)(?:(?:ing)|(?:ly)|(?:ment))\b', text ) #find all roots (-ing, -ly, -ment)
    #print(matches)
    for stem in matches: #for each root
        text = re.sub(rf'\b{stem}(?:(?:ing)|(?:ly)|(?:ment))\b', stem, text) #change whatever that stem is connected to to just that stem
       
    #write data to preproc_[docname].txt
    with open(f'preproc_{docname}', 'w') as f:
        f.write(text)

    return f'preproc_{docname}'

def gettf(docname):
    #compute frequencies of all the distinct words in that document
    with open(docname, "r") as f:
        text = f.read() 
    freqs = {}
    tokens = text.split(' ')
    tot = len(tokens) #get total # of terms in document
    for word in tokens: #each word add 1 to count
        if word in freqs:
            freqs[word] += 1
        else:
            freqs[word] = 1
    
    for (word, count) in freqs.items():
        freqs[word] = count/tot

    #print(freqs)
    return freqs

def getidf(tf, doclist):    
    #compute inverse document frquency of each word for eac jdocument
    doccount = len(tf)
    wordlist = {}
    for doc in doclist: #for each document
        for word in tf.get(doc): #for each word in that doc
            if word in wordlist:
                wordlist[word] += 1 #add to "# of documents term t in in"
            else:
                wordlist[word] = 1
    
    idf = {}
    for word in wordlist:
        idf[word] = math.log(doccount/wordlist[word] + 1) #ln((total nmber of documents)/(# of documents term t is in)) + 1
    #print(idf)
    return idf


def gettfidf(doc, tf, idf):
    #tf-idf score PER DOC: TF * IDF for each word, round to 2 decimal places.
    tfidf = {} #word:tfidf score dic
    for word in tf:
        tfidf[word] = round(tf.get(word) * idf.get(word), 2) #calculate tfidf for each word.
        print(word + ": " + str(tfidf[word]) + " " + str(tf.get(word)) + " " + str(idf.get(word)))
    print(tfidf)
    
    sdic = dict(sorted(tfidf.items(), key=lambda item: (item[1], item[0]))) #get top 5
    #t5 = take(5, sdic.items())
    t5 = list(sdic.items())[:4]
    #final = []
    #for i in t5: #for word in top 5
    #    final.append(i, i.get())

    with open(f'tfdif_{doc}', 'w') as f:
        f.write("[")
        for x, y in t5:
            f.write(x + ", " + str(y))
        f.write("]")
    #print to tfidf_[document name].txttop 4 most important words in each prepreocessed document according to their tf-idf scores
        #in case of ties, pick words in alcfabetical order
        #print result as list: (word, TF-IDF score)

def main():
    doclist = []
    preproclist = []
    stopword() #read stopwords from doc and make into list
    with open("tf-idf.txt", "r") as f:
        input = f.read()
        doclist = input.split('\n')
        for docname in doclist:
            preproclist.append(preprocess(docname)) #preprocess that doc, add new docname to list
              
        #compute tdidf
        #print top tfidf
    tf = {} #empty list of tf dictionaries for each doc. SAME ORDER AS DOCLIST
    for docname in preproclist: #for each document...
        tf[docname] = tf(docname) #create a dictionary of word:tf and add dictionaries to list.
        idf = idf(tf) #create word:idf dictionary per word for all docs
    #actually:
    for doc in doclist:
        tfidf(doc, tf[doc], idf) #create word:tfidf and print top 5

def test():
    doclist = []
    stopword() #read stopwords from doc and make into list
    with open("testing.txt", "r") as f:
        input = f.read()
        doclist = input.split('\n')
            
        #compute tfidf
        #print top tfidf
    tf = {} #empty list of tf dictionaries for each doc. SAME ORDER AS DOCLIST
    for docname in doclist: #for each document...
        tf[docname] = gettf(f'preproc_{docname}') #create a dictionary of word:tf and add dictionaries to list.
    idf = getidf(tf, doclist) #create word:idf dictionary per word for all docs
    #actually:
    for doc in doclist:
        gettfidf(doc, tf[doc], idf) #create word:tfidf and print top 5


test()