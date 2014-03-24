'''
Created on Mar 19, 2014

@author: medhat
'''
from Bio.Blast import NCBIWWW
from Bio import SeqIO
from Bio.Blast import NCBIXML
import os  ,sys , getopt ,copy

def main(argv):
    print(argv)
    scriptName = os.path.basename(__file__)
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
        
    except getopt.GetoptError:
        print scriptName + ' -i <inputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print scriptName + ' -i <inputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputFile = arg
        elif opt in ("-o", "--ofile"):
            outputFile = arg
            print(outputFile)    
    loopDirectory(inputFile, outputFile)        

#Read all the files in directory and process them one by one
def loopDirectory(directory,resultDirectory):
    print("Reading from directory ==> " + directory)
    for fn in os.listdir(directory):
        
        if os.path.isfile(os.path.join(directory,fn)):
            # call method to process the file
            fn = directory+fn
            processFasta(fn, resultDirectory)
        else:
            print("Sorry "+fn+" Is not a file")    
def processFasta(fastaFile,resultDirectory):
    print("Writing to directory ==> " + resultDirectory)
    record = SeqIO.read(fastaFile, format="fasta")
    result_handle = NCBIWWW.qblast("blastx", "nr", record.format("fasta"), expect=1e-10 , hitlist_size=5)
    baseFile = os.path.basename(fastaFile)
    fileName = baseFile.rsplit('.',1)[0] + '.xml'
    #fileName = fastaFile
    location = resultDirectory  + fileName
    
    save_file = open(location, "w")
    save_file.write(result_handle.read())
    save_file.close()
    result_handle = open(location)
    genomeName=os.path.basename(fastaFile).rsplit(".",1)[0]
    handelBlastResult(result_handle,genomeName)            

def handelBlastResult(result_handle,genomeName):
    print("Handeling Result  for ==> " + genomeName)
    blast_records = NCBIXML.parse(result_handle)
    valueSet = set()
    sub_strings = ('description' , 'hypothetical','unknown','uncharacterized')
    for blast_record in blast_records:
        for alignment in blast_record.alignments:
            for hsp in alignment.hsps:
                titleData = alignment.title
                splitTitleData = titleData.split('|')
                proteinFunction = splitTitleData[4]
                valueSet.add(proteinFunction)
    # test if it is functional or non functional genome 
    valueSetCopy =  copy.deepcopy(valueSet)
    for value in valueSet:
            if any(x in value for x  in sub_strings):
                valueSetCopy.remove(value)
    # genome has functional protein
    proteinDescription = ''
    first =  True
    for element  in valueSet:
        if first:
            proteinDescription = element + '\t'
            first = False
        else:
            proteinDescription = proteinDescription + element + '\t'    
        
    if len(valueSetCopy) > 0:
        print("Writing Result  for ==> functionalSequence.txt" )
        writtingSearchResult(genomeName, proteinDescription, "functionalSequence.txt")
    else:
        print("Writing Result  for ==> nonFunctionalSequence.txt" )
        writtingSearchResult(genomeName, proteinDescription, "nonFunctionalSequence.txt")    

def writtingSearchResult(id,dataString,fileName):
    fo = open(fileName,"a")
    fo.write(id+'\t'+dataString+'\n')
    fo.close()    
 
if __name__ == "__main__":
    main(sys.argv[1:])  
