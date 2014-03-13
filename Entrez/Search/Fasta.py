'''
Created on Mar 11, 2014

@author: medhat
'''
from Bio import Entrez
from urllib2 import HTTPError
import os , time ,sys , getopt


#===============================================================================
# def main(argv):
#     try:
#         opts, args = getopt.getopt(argv, "hi:", ["ifile="])
#     except getopt.GetoptError:
#         print 'MapCount.py -i <inputfile>'
#         sys.exit(2)
#     for opt, arg in opts:
#         if opt == '-h':
#             print 'MapCount.py -i <inputfile>'
#             sys.exit()
#         elif opt in ("-i", "--ifile"):
#             inputFile = arg
#             lostData = getFasta(inputFile)
#             printList(lostData)
#===============================================================================
  
Entrez.email = "medhat.helmy77@gmail.com"
resultFolder = os.path.abspath(__file__)
resultFolder = os.path.dirname(resultFolder) + "/fastaSeq"
os.makedirs(resultFolder)

# loop a file of ids and locations
def getFasta(inputFile):
    try:
        if inputFile:
            fileData = open(inputFile , 'r')
            missedSequence=[]
            for line in fileData:
                lineSpliced = line.split('\t')
                geneId = lineSpliced[0]
                start = int(lineSpliced[1])
                end = int(lineSpliced[2])
                
                # get data from ncbi
                handle = Entrez.esearch(db="nucleotide", term=geneId)
                record = Entrez.read(handle)
                
                if not is_empty(record["IdList"]):
                    recordId = record["IdList"][0]
                    handleSeq = Entrez.efetch(db="nucleotide", id=recordId, rettype="fasta", retmode="text")
                    of = open(resultFolder+"/"+geneId+".txt", "w")
                    fastaData = handleSeq.read()
                    newSeq = cutSeq(fastaData, start, end)
                    of.write(newSeq)
                    time.sleep(1)
                    of.close()
                else:
                    missedSequence.append(geneId)
            
        return missedSequence
    except HTTPError:
        print "Oops!  That was ERROR.  Try again..."
        
# function to cut the data according to the coordinates 
def cutSeq(seq , start , end):
    try:
        if seq and start and end:
            # overcome the python 0 counting
            start = start - 1
            end = end - 1
            header = seq.split('\n', 1)[0]
            sansfirstline = '\n'.join(seq.split('\n')[1:])
            sequenc = sansfirstline[start:end]
            # if it is - strand get the complimentry
            content = header +'\n'+sequenc
            return  content
            
    except StandardError:
        print "Oops!  That was ERROR cutting sequence.  Try again..."  
        
def is_empty(any_structure):
    if any_structure:
        #print('Structure is not empty.')
        return False
    else:
        #print('Structure is empty.')
        return True 
    
def printList(data):
    if data:
        fo = open("lost.txt","a")
        for elment in data:
            fo.write(elment+'\n')
        fo.close()                
print("========  BEGINNINGING =========")         
lost = getFasta("/home/medhat/Samples/merge_test/GenIds.txt")
print("========  WRITE THE LIST =========")
printList(lost)
print("========  DONE =========")

