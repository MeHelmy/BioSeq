'''
Created on Apr 11, 2014

@author: medhat
'''
import sys , re

argument = []
for arg in sys.argv[1:]:
    argument.append(arg)

def getGenes(inputFile):
    geneDictionary ={}
    if inputFile:
        fo = open(inputFile,'r')
        for line in fo:
            data = line.split('\t',1)[0]
            geneDictionary[data] = data
        fo.close()    
    return geneDictionary  

def removeDuplication(inputFile , outputFile):
    dataDictionary =  getGenes(inputFile)
    doneDictionary = {}
    fo = open(inputFile , 'r')
    outputData = open(outputFile , 'a')
    for line in fo:
        geneName = line.split('\t',1)[0]
        if geneName in dataDictionary and geneName not in doneDictionary:
            outputData.write(line)
            doneDictionary[geneName] = geneName
    fo.close()
    outputData.close() 
    
''' method call '''
    
removeDuplication(argument[0], argument[1])                