'''
Created on Feb 26, 2014

@author: medhat
'''
import sys , getopt , re


def main(argv):
    inputFile = ''

    try:
        opts, args = getopt.getopt(argv,"hi:",["ifile="])
    except getopt.GetoptError:
        print 'ExonLength.py -i <inputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'ExonLength.py -i <inputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputFile = arg
            myDic , header = getMergeDataFromFile(inputFile)
            writeDic(myDic , header)

def getMergeDataFromFile(inputFile):
        fileData = open(inputFile,'r')
        i = 1
        mergedData = {}
        header = 'GenId\tDiscription'
        for line in fileData:
            header = addToDicFromFile(mergedData, line , i,header)
            i+=1
        return mergedData , header  

#increment dictionary from file
def addToDicFromFile(dictionary , inputFile,i,header):
        header = header + '\tLog' + str(i) + '\t' + 'P-Value' + str(i)
        inputFile = inputFile.rstrip('\n')
        fileData = open(inputFile,'r')
        fileData.next()
        # make the first part of line
        if i > 1:
                begin = '0' + '\t' + '0' + '\t'
                begin = begin * (i-1) 
        else:
                begin = '' 
                  
        for line in fileData:
            colum=line.split('\t')
            geneId = str(colum[7])
            disc = colum[8]
            if '/' in inputFile:
                fileName = inputFile.rsplit('/',1)[1]
                
            logsColumn = re.findall(r'\d+',fileName)
            log = float(colum[int(logsColumn[0])])/float(colum[int(logsColumn[1])])
            pValue = colum[5]
            if geneId not in dictionary:
                    if i == 1:
                        dictionary[geneId] = geneId + '\t' + disc + '\t' + str(log) + '\t' + pValue
                    else:
                        dictionary[geneId] = geneId + '\t' + disc + '\t' + begin + str(log) + '\t' + pValue 
            else:        
                    dictionary[geneId] = dictionary[geneId] +  '\t' + str(log) + '\t' + pValue
        return header           
def writeDic(dic ,header):
    fo = open('tes_merged_seq_report.txt','a')
    fo.write(header + '\n')
    defaultLength = len(header.split('\t'))
    for value in dic.itervalues():
            nOfValues = len(value.split('\t'))
            addString = ''
            if nOfValues < defaultLength:
                numberOflostData = defaultLength - nOfValues
                addString = '\t0' * numberOflostData
                
            fo.write(value + addString + '\n')
        
    fo.close()
#===============================================================================
# def main(argv):
#     try:
#         opts, args = getopt.getopt(argv,"hi:i2:i3:i4:",["ifile=","ifile2=","ifile3=","ifile4="])
#     except getopt.GetoptError:
#         print 'MergeReport.py -i1 <inputfile> -i2 <comparefile2> -i3 <comparefile3> -i4 <comparefile4>'
#         sys.exit(2)
#     for opt, arg in opts:
#         if opt == '-h':
#             print 'MergeReport.py -i1 <inputfile> -i2 <comparefile2> -i3 <comparefile3> -i4 <comparefile4>'
#             sys.exit()
#         elif opt in ("-i", "--ifile"):
#             inputFile = arg
#         elif opt in ("-i2", "--ifile2"):    
#             compareFile2 = arg
#         elif opt in ("-i3", "--ifile3"):
#             compareFile3 = arg
#         elif opt in ("-i4", "--ifile4"):    
#             compareFile4 = arg    
#             mergeDic ,firstDic , secondDic,thirdDic,fourthDic = getMergeId(inputFile,compareFile2,compareFile3,compareFile4)
#             mergeFile(mergeDic ,firstDic , secondDic,thirdDic,fourthDic,inputFile,compareFile2,compareFile3,compareFile4)      
#     
# def is_empty(any_structure):
#     if any_structure:
#         #print('Structure is not empty.')
#         return False
#     else:
#         #print('Structure is empty.')
#         return True
# #merge two dictionaries     
# def getMergeId(inputFile,compareFile2,compareFile3,compareFile4):
#     firstDic = loopFile(inputFile)
#     secondDic = loopFile(compareFile2)
#     thirdDic = loopFile(compareFile3)
#     fourthDic = loopFile(compareFile4)
#     mergeDic = firstDic.copy()
#     mergeDic.update(secondDic)
#     mergeDic.update(thirdDic)
#     mergeDic.update(fourthDic)
#     return mergeDic ,firstDic , secondDic ,thirdDic , fourthDic
# 
#            
# #compare both files based on the Ids dictionary
# def mergeFile(idsDictionary,firstDic , secondDic,thirdDic,fourthDic,inputFile,compareFile2,compareFile3,compareFile4):
#     fo = open('merged_seq_report.txt','a')
#     if idsDictionary:
#         with open(inputFile) as f:
#                 header = f.readline()
#         header = header.rstrip('\n')        
#         fo.write(header+'\t'+'log1_3'+'\t'+'Pvalue1_3'+'\t'+'log2_4'+'\t'+'Pvalue2_4'+'\t'+'data_type'+'\n') 
#         headerValue = 'genId' + '\t' + 'log' + '\t' + 'p-Value'  + '\t' + 'log' + '\t' + 'p-Value' + '\t' + 'log' + '\t' + 'p-Value' + '\t' + 'log' + '\t' + 'p-Value'  
# #===============================================================================
# # 
# #         for key in idsDictionary:
# #             if key in firstDic:
# #                 firstFileKey = True
# #             else :
# #                 firstFileKey = False
# #                 
# #             if key in secondDic:
# #                 secondFileKey = True
# #             else :
# #                 secondFileKey = False 
# #             if key in thirdDic:
# #                 thirdFileKey = True
# #             else :
# #                 thirdFileKey = False
# #                 
# #             if key in fourthDic:
# #                 fourthFileKey = True
# #             else :
# #                 fourthFileKey = False 
# # 
# #                 
# #     
# #                     
# #             #compare the two files based on the result of the dictionary
# #             if (firstFileKey and secondFileKey and thirdDic and fourthDic):
# #                 # get the two lines from each file and merge them
# #                 lineFromFirstFile = getLine(key, inputFile)
# #                 lineFromSecondFile = getLine(key, secondFile)
# #                 # merge data from two lines
# #                 row = mergeLine(lineFromFirstFile, lineFromSecondFile)
# #                 fo.write(str(row) +'\n')   
# #             elif (firstFileKey and secondFileKey and thirdFileKey):
# #             elif (firstFileKey and secondFileKey and fourthFileKey):
# #             elif (firstFileKey and thirdFileKey and fourthFileKey):
# #             elif (secondFileKey and thirdFileKey and fourthFileKey):
# #             elif (firstFileKey and secondFileKey):
# #             elif (firstFileKey and thirdFileKey):
# #             elif (firstFileKey and fourthFileKey):
# #             elif (secondFileKey and thirdFileKey):
# #             elif (secondFileKey and fourthFileKey):
# #             elif (thirdFileKey and fourthFileKey):                                    
# #             elif firstFileKey:
# #                 # get data from first file and write that it is not exist in the second file
# #                 lineFromFirstFile = getLine(key, firstFile)
# #                 lineFromSecondFile = None
# #                 # merge data from two lines
# #                 row = mergeLine(lineFromFirstFile, lineFromSecondFile)
# #                 fo.write(str(row) +'\n')
# #             elif secondFileKey:        
# #                 # get data from second file and write that it is not exist in the first file
# #                 lineFromSecondFile = getLine(key, secondFile)
# #                 lineFromFirstFile = None
# #                 # merge data from two lines
# #                 row = mergeLine(lineFromFirstFile, lineFromSecondFile)
# #                 fo.write(str(row) +'\n')
# #             elif thirdFileKey:
# #             elif fourthFileKey:    
# #===============================================================================
#         
#         # get the files from input file and but it in  a list
#         fileData = open(inputFile,'r')
#         i = 1
#         mergedData = {}
#         for line in fileData:
#             line = line.rstrip('\n')
#             addToDicFromFile(mergedData, line , i)
#             i+=1
#         
# 
#                 
#                 
#                         
#     fo.close()            
# 
#                
# # get line from file by the Id            
# def getLine(ID , inputFile):
#         fileData = open(inputFile,'r')
#         fileData.next()
#         for line in fileData:
#             colum=line.split('\t')
#             if str(colum[7])== str(ID):
#                 return line
#             
# # merge two lines or one adding column that the data does not exist in the other column 
# def mergeLine(firstLine , secondLine):
#     #first case id exist in both files
#             # results in 16 column
#     if firstLine is not None :       
#         firstLineDevided = firstLine.split('\t')
#     if secondLine is not None :    
#         secondLineDevided = secondLine.split('\t')
#     if (firstLine is not None and secondLine is not None):
# 
#         # new data will be added
#         log1_3First = float(firstLineDevided[12])/float(firstLineDevided[14])
#         log2_4Second =float(secondLineDevided[13])/float(secondLineDevided[15])
#         pValue1 = firstLineDevided[5]
#         pValue2 = secondLineDevided[5]
#         line = firstLine.rstrip('\n') + '\t' + str(log1_3First) + '\t' +pValue1 +'\t'+str(log2_4Second) + '\t'+pValue2+'\t'+'both'
#         return line
#     #second case id in first file only    
#     elif (firstLine is not None and secondLine is None):
#         log1_3First = float(firstLineDevided[12])/float(firstLineDevided[14])
#         pValue1 = firstLineDevided[5]
#         line = firstLine.rstrip('\n') + '\t' + str(log1_3First) + '\t' +pValue1 +'\t'+'-' + '\t'+'-'+'\t'+'first1_3'
#         return line
#     # third case id exist only in the second file
#     elif (secondLine is not None and firstLine is None):
#         log2_4Second =float(secondLineDevided[13])/float(secondLineDevided[15])
#         pValue2 = secondLineDevided[5]
#         line = secondLine.rstrip('\n') + '\t' + '-' + '\t' +'-' +'\t'+str(log2_4Second) + '\t'+pValue2+'\t'+'second2_4'
#         return line 
# #extract the ID from the file in dictionary
# def loopFile(inputFile):
#         if inputFile:
#             fileData = open(inputFile,'r')
#             data = {}
#             for line in fileData:
#                     colum=line.split('\t')
#                     data[colum[7]] = str(colum[7])
#         return data 
# #===============================================================================
# #  
# # mergeDic ,firstDic , secondDic = getMergeId('/home/medhat/Downloads/Samples/merge_test/mRNA1-3.txt','/home/medhat/Downloads/Samples/merge_test/mRNA2-4.txt')
# # mergeFile(mergeDic ,firstDic , secondDic,'/home/medhat/Downloads/Samples/merge_test/mRNA1-3.txt','/home/medhat/Downloads/Samples/merge_test/mRNA2-4.txt')
# #                     
# #===============================================================================
#===============================================================================
if __name__ == "__main__":
    main(sys.argv[1:])     
