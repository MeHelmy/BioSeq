'''
Created on Mar 11, 2014

@author: medhat
'''
from Bio import Entrez
import os
Entrez.email = "medhat.helmy77@gmail.com"
resultFolder = os.path.abspath(__file__) + "/fastaSeq"

# loop a file of ids and locations
def getFasta(inputFile):
    try:
        if inputFile:
            fileData = open(inputFile , 'r')
            for line in fileData:
                lineSpliced = line.split('\t')
                geneId = lineSpliced[0]
                start = lineSpliced[1]
                end = lineSpliced[2]
                
                # get data from ncbi
                handle = Entrez.esearch(db="nucleotide", term=geneId)
                record = Entrez.read(handle)
                recordId = record["IdList"][0]
                handleSeq = Entrez.efetch(db="nucleotide", id=recordId, rettype="fasta", retmode="text")
                of = open(resultFolder+"/"+geneId+".txt", "w")
                fastaData = handleSeq.read()
                
                of.write(fastaData)
                of.close()
                
            
        
    except StandardError:
        print "Oops!  That was ERROR.  Try again..."
        
# function to cut the data according to the coordinates 
def cutSeq(seq , start , end):
    try:
        if seq and start and end:
            return 
            
    except StandardError:
        print "Oops!  That was ERROR cutting sequence.  Try again..."    
