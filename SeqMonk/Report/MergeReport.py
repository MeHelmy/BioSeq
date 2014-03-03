'''
Created on Feb 26, 2014

@author: medhat
'''
import sys , getopt

def main(argv):
    inputFile = ''
    compareFile = ''
      
    try:
        opts, args = getopt.getopt(argv,"hi:c:",["ifile=","cfile="])
    except getopt.GetoptError:
        print 'MergeReport.py -i <inputfile> -c <comparefile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'MergeReport.py -i <inputfile> -c <comparefile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputFile = arg
        elif opt in ("-c", "--cfile"):    
            compareFile = arg
            mergeDic ,firstDic , secondDic = getMergeId(inputFile,compareFile)
            mergeFile(mergeDic ,firstDic , secondDic,inputFile,compareFile)      
    

def is_empty(any_structure):
    if any_structure:
        #print('Structure is not empty.')
        return False
    else:
        #print('Structure is empty.')
        return True
#merge two dictionaries     
def getMergeId(inputFile ,compareFile):
    firstDic = loopFile(inputFile)
    secondDic = loopFile(compareFile)
    mergeDic = firstDic.copy()
    mergeDic.update(secondDic)
    return mergeDic ,firstDic , secondDic

#compare both files based on the Ids dictionary
def mergeFile(idsDictionary,firstDic , secondDic,firstFile,secondFile):
    fo = open('merged_seq_report.txt','a')
    if idsDictionary:
        with open(firstFile) as f:
                header = f.readline()
        header = header.rstrip('\n')        
        fo.write(header+'\t'+'log1_3'+'\t'+'Pvalue1_3'+'\t'+'log2_4'+'\t'+'Pvalue2_4'+'\t'+'data_type'+'\n')    

        for key in idsDictionary:
            if key in firstDic:
                firstFileKey = True
            else :
                firstFileKey = False
                
            if key in secondDic:
                secondFileKey = True
            else :
                secondFileKey = False 

                
    
                    
            #compare the two files based on the result of the dictionary
            if (firstFileKey and secondFileKey):
                # get the two lines from each file and merge them
                lineFromFirstFile = getLine(key, firstFile)
                lineFromSecondFile = getLine(key, secondFile)
                # merge data from two lines
                row = mergeLine(lineFromFirstFile, lineFromSecondFile)
                fo.write(str(row) +'\n')   
                
            elif firstFileKey:
                # get data from first file and write that it is not exist in the second file
                lineFromFirstFile = getLine(key, firstFile)
                lineFromSecondFile = None
                # merge data from two lines
                row = mergeLine(lineFromFirstFile, lineFromSecondFile)
                fo.write(str(row) +'\n')
            elif secondFileKey:        
                # get data from second file and write that it is not exist in the first file
                lineFromSecondFile = getLine(key, secondFile)
                lineFromFirstFile = None
                # merge data from two lines
                row = mergeLine(lineFromFirstFile, lineFromSecondFile)
                fo.write(str(row) +'\n')
    fo.close()            
                
# get line from file by the Id            
def getLine(ID , inputFile):
        fileData = open(inputFile,'r')
        fileData.next()
        for line in fileData:
            colum=line.split('\t')
            if str(colum[7])== str(ID):
                return line
            
# merge two lines or one adding column that the data does not exist in the other column 
def mergeLine(firstLine , secondLine):
    #first case id exist in both files
            # results in 16 column
    if firstLine is not None :       
        firstLineDevided = firstLine.split('\t')
    if secondLine is not None :    
        secondLineDevided = secondLine.split('\t')
    if (firstLine is not None and secondLine is not None):

        # new data will be added
        log1_3First = float(firstLineDevided[12])/float(firstLineDevided[14])
        log2_4Second =float(secondLineDevided[13])/float(secondLineDevided[15])
        pValue1 = firstLineDevided[5]
        pValue2 = secondLineDevided[5]
        line = firstLine.rstrip('\n') + '\t' + str(log1_3First) + '\t' +pValue1 +'\t'+str(log2_4Second) + '\t'+pValue2+'\t'+'both'
        return line
    #second case id in first file only    
    elif (firstLine is not None and secondLine is None):
        log1_3First = float(firstLineDevided[12])/float(firstLineDevided[14])
        pValue1 = firstLineDevided[5]
        line = firstLine.rstrip('\n') + '\t' + str(log1_3First) + '\t' +pValue1 +'\t'+'-' + '\t'+'-'+'\t'+'first1_3'
        return line
    # third case id exist only in the second file
    elif (secondLine is not None and firstLine is None):
        log2_4Second =float(secondLineDevided[13])/float(secondLineDevided[15])
        pValue2 = secondLineDevided[5]
        line = secondLine.rstrip('\n') + '\t' + '-' + '\t' +'-' +'\t'+str(log2_4Second) + '\t'+pValue2+'\t'+'second2_4'
        return line 
#extract the ID from the file in dictionary
def loopFile(inputFile):
        if inputFile:
            fileData = open(inputFile,'r')
            data = {}
            for line in fileData:
                    colum=line.split('\t')
                    data[colum[7]] = str(colum[7])
        return data 
#===============================================================================
#  
# mergeDic ,firstDic , secondDic = getMergeId('/home/medhat/Downloads/Samples/merge_test/mRNA1-3.txt','/home/medhat/Downloads/Samples/merge_test/mRNA2-4.txt')
# mergeFile(mergeDic ,firstDic , secondDic,'/home/medhat/Downloads/Samples/merge_test/mRNA1-3.txt','/home/medhat/Downloads/Samples/merge_test/mRNA2-4.txt')
#                     
#===============================================================================
if __name__ == "__main__":
    main(sys.argv[1:])     
