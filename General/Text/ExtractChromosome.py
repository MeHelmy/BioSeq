'''
Created on Apr 8, 2014

@author: medhat
'''
import sys , re

argument = []
for arg in sys.argv[1:]:
    argument.append(arg)


def extractChr(inputFile, outPut):
   
    if inputFile:
        fo = open(inputFile, "r")

        firstTime = True
        seqFile = ''

        for line in fo:
           
            line = line.strip()
            if line.startswith(">"):
              
                if firstTime:
                    fileName = line.replace(">", "")
                    fileName = fileName.strip()
                    name =re.split("\|",re.split(" ", fileName)[0])[1]
                    seqFile = open(outPut + name + ".fasta", "a")
                    seqFile.write(line)
                    firstTime = False
                else:
                    seqFile.close
                    fileName = line.replace(">", "")
                    fileName = fileName.strip()
                    name =re.split("\|",re.split(" ", fileName)[0])[1]
                    seqFile = open(outPut + name + ".fasta", "a")
                    seqFile.write(line)
            else:
                    seqFile.write(line)
        



extractChr(argument[0], argument[1])
#extractChr("/home/medhat/Samples/merge_test/NewmRNA/GenomeCDS8-04-14.txt", "/home/medhat/Samples/merge_test/NewmRNA/SequenceCDS/")
