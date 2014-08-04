'''
Created on Jun 25, 2014
this is a script to get all fasta sequences name from a big fasta file
@author: medhat
'''

__author__ = 'medhat'

import sys , re , os

argument = []
for arg in sys.argv[1:]:
    argument.append(arg)
    

def extractFasta(inputFile,outputFile):
    sequanceName = {}
    if inputFile:
        fo = open(inputFile,'r')
        for line in fo:
            line = line.strip()
            if line.startswith(">"):
                sequanceName[line.split()[0].replace(">","")] = line.split()[0].replace(">","")
                #sequanceName.append(line.split()[0].replace(">",""))
        writeFile = open(outputFile,'a')
        for element in sequanceName:
            writeFile.write(element+"\n")
        fo.close()
        writeFile.close()
        
def getSeqNameFromXML(xmlFile,outputfile):
    if xmlFile:
        seqNames = {}
        fo = open(xmlFile,'r')
        for line in fo:
            line = line.strip()
            if line.startswith("<Iteration_query-def>"):
                seqId = line.split()[0].replace("<Iteration_query-def>","")
                seqNames[seqId] = seqId
        seqFromXML  = os.path.split(os.path.abspath(outputfile))[0]+"/seqInXML.txt"
        outFile = open(seqFromXML , 'a')
        for k in seqNames:
            outFile.write(k+'\n')
#         for line in seqNames:
#             outFile.write(line+'\n')
        fo.close()
        outFile.close()             
  
# define a function that extraCT THE NON blasted sequence 

def unblasted(seqFromFile):
        if seqFromFile:
            xmlFile = os.path.split(os.path.abspath(seqFromFile))[0]+"/seqInXML.txt"
            #read two dictionaries 
            seqFromFileRead = open(seqFromFile,'r')
            xmlFileRead = open(xmlFile,'r')
            seqFromFileDic={}
            xmlFileDic= {}
            for line in seqFromFileRead:
                seqFromFileDic[line] = line
            seqFromFileRead.close()
            
            for line in xmlFileRead:
                xmlFileDic[line] = line
            xmlFileRead.close()
                    
            # creat two dictionaryes for each
            differenceFile = open(os.path.split(os.path.abspath(seqFromFile))[0]+"/differenceSequence.txt",'a')
            for k in seqFromFileDic:
                print(k+"-- in outer loop")
                if k not in xmlFileDic:
                    differenceFile.write(k+'\n')
            differenceFile.close()
                      
        
extractFasta(argument[0], argument[1])
getSeqNameFromXML(argument[2], argument[1])
unblasted(argument[1])
