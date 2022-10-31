#FINAL 10/29
import math
import re

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
    text = re.sub(r'[^\w\s]', '', text) #remove nonword characters
    text = re.sub(r'(https\w*\S)', '', text) #remove links
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r' +', ' ', text) #remove extra whitespace
    text = text.lower() #convert all to lowercase   

    #remove stopwords using stopwords.txt
    for x in stopwords:
        text = re.sub(rf'\b{x}\b', "", text)
        text = re.sub(r' +', ' ', text)
    
    #stemming and lemmatization: return words to root forms
    matches = re.findall(r'\b(\w*)(?:(?:ing)|(?:ly)|(?:ment))\b', text ) #find all roots (-ing, -ly, -ment)
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
    
    #print("tf: " + str(freqs) + "\n") #FREQUENCY/COUNT SEEMS TO BE CORRECT
    return freqs

def getidf(tf, doclist):
    #compute inverse document frquency of each word for each jdocument
    doccount = len(tf)
    wordlist = {}
    for doc in doclist: #for each document
        for word in tf.get(doc): #for each word in that doc
            if word in wordlist:
                wordlist[word] += 1 #add to "# of documents term t in in"
            else:
                wordlist[word] = 1
    #print("total number of documents: " + str(doccount) + "\n" + "# of documents term is in: " + str(wordlist) )
    idf = {}
    for word in wordlist:
        idf[word] = math.log(doccount/wordlist[word]) + 1 #ln((total nmber of documents)/(# of documents term t is in)) + 1
    #print("idf: " + str(idf) + "\n")
    return idf
    


def gettfidf(doc, tf, idf):
    #tf-idf score PER DOC: TF * IDF for each word, round to 2 decimal places.
    tfidf = {} #word:tfidf score dic
    for word in tf:
        tfidf[word] = round(tf.get(word) * idf.get(word), 2) #calculate tfidf for each word.

    #print("tfidf: " + str(tfidf))
    t5 = []
    n = 5
    if (len(tfidf) < 5): n = len(tfidf) #if there isnt enough for top 5
    for i in range(n):
        max = ("", 0)
        for k, v in tfidf.items(): #iterate thru dict
            if v > max[1]: #if this is max
                max = (k, v) #save it
            if v == max[1]: #tiebreakers
                if k < max[0]:
                    max = (k, v)
        t5.append(max) #save actual max
        #print(max)
        del tfidf[max[0]] #delete it from list 
    
    with open(f'tfdif_{doc}', 'w') as f:
        f.write(str(t5))
    
    #print to tfidf_[document name].txttop 5 most important words in each prepreocessed document according to their tf-idf scores
        #in case of ties, pick words in alcfabetical order
        #print result as list: (word, TF-IDF score)

def main():
    doclist = []
    stopword() #read stopwords from doc and make into list
    with open("tfidf_docs.txt", "r") as f:
        input = f.read()
        doclist = input.split('\n')
        for docname in doclist:
            preprocess(docname)
        #compute tfidf
        #print top tfidf
    tf = {} #empty list of tf dictionaries for each doc. SAME ORDER AS DOCLIST
    for docname in doclist: #for each document...
        tf[docname] = gettf(f'preproc_{docname}') #create a dictionary of word:tf and add dictionaries to list.
    idf = getidf(tf, doclist) #create word:idf dictionary per word for all docs
    #actually:
    for doc in doclist:
        gettfidf(doc, tf[doc], idf) #create word:tfidf and print top 5

main()