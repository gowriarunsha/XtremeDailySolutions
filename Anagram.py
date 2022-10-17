def getAnagramSet(words):
 
  #remove duplicate words from the list
  words=list(set(words))
 
  #find the anagram of each word in the list
  anagramWords=[''.join(sorted(x)) for x in words]
 
  finalOut=[]
  for word in set(anagramWords):
    #find the index for all occurences of string word
    ind=[i for i, x in enumerate(anagramWords) if x==word]
 
    #make the list of all the string 
    #which is anagram to each other
    tempOut=[]
    for i in ind:
      tempOut.append(words[i])
 
    #append all the set to the final output list
    finalOut.append(set(tempOut))
 
  return finalOut
 
words=['cat', 'dog', 'god', 'cat']  
 
if _name_ == "_main_":
    print(getAnagramSet(words))
