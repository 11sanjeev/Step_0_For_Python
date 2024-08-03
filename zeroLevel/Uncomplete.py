import fileinput
def mainFunction():
    print("Please enter the message (no punctuation please):")
    txtMessage = input(">") 
    messageWords = txtMessage.split()
    translationFileName = "deomo.txt"
    fileFound = fileCheck(translationFileName)

    if fileFound == 0 :
        allAbbreviations, allTranslations = dictionaryList(translationFileName) 
        translatedMessage = compare(messageWords, allAbbreviations, allTranslations) 
        print(translatedMessage)
    else : 
        print("Could not translate message, file containing translation terms could not be located.")

def fileCheck(fileName):
    try:
        fileObj = open(fileName) 
        return 0
    except IOError: 
        print("Could not locate the file " + fileName)
        return 1

def dictionaryList(fileName):
    allAbbreviations = []
    allTranslations = []
    fileObj = open(fileName)

    for line in iter(fileObj):
        wordsInTheLine = line.split() 
        allAbbreviations.append(wordsInTheLine[0])
        translation = ""
        totalNumberOfWords = len(wordsInTheLine)
 
        for x in range(2,totalNumberOfWords):
            
            translation = translation + wordsInTheLine[x] + " " 
        allTranslations.append(translation)
    
    return (allAbbreviations, allTranslations)

def compare(messageWords, allAbbreviations, allTranslations):
    
    finalMessage = ""
    for wordPosition in range(0, len(messageWords)):
        currentWord = messageWords[wordPosition]

        try :
            matchPosition = allAbbreviations.index(currentWord.upper())
            finalMessage = finalMessage + " " + allTranslations[matchPosition]
            
        except :
            finalMessage = finalMessage + " " + currentWord 
            
    return (finalMessage)

mainFunction()