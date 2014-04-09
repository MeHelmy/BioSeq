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
        # count number of lines in file
        num_lines = sum(1 for row in open(inputFile) if row.rstrip())
        i = 1
        mergedData = {}
        header = 'GenId\tDiscription\tChr\tStart\tEnd\tStrand'
        num = 1
        while (num <= num_lines):
            header = header + '\tSample-' + str(num)
            num = num +1
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
            samples = {}
            # i can make this dynamic by using dictionary the where the name is the column name and the value will be the value in the column 
            sample1 = str(colum[12])
            sample2 = str(colum[13])
            sample3 = str(colum[14])
            sample4 = str(colum[15])
            samples = sample1 + '\t' + sample2 + '\t' + sample3 + '\t' + sample4
            samples = samples.rstrip('\n')
            disc = colum[8]
            start = colum[2]
            end = colum[3]
            strand = colum[4]
            chromosome = "chr"+str(colum[1])
            if '/' in inputFile:
                fileName = inputFile.rsplit('/',1)[1]
                
            logsColumn = re.findall(r'\d+',fileName)
            log = float(colum[int(logsColumn[0])]) - float(colum[int(logsColumn[1])])
            pValue = colum[5]
            if geneId not in dictionary:
                    if i == 1:
                        dictionary[geneId] = geneId + '\t' + disc + '\t' + chromosome +'\t'+start + '\t' + end + '\t' + strand + '\t' + samples + '\t' + str(log) + '\t' + pValue
                    else:
                        dictionary[geneId] = geneId + '\t' + disc + '\t' + chromosome + '\t' + start + '\t' + end + '\t' + strand + '\t' + samples + '\t' + begin + str(log) + '\t' + pValue 
            else:        
                    dictionary[geneId] = dictionary[geneId] +  '\t' + str(log) + '\t' + pValue
        return header           
def writeDic(dic ,header):
    fo = open('merged_seq_report.txt','a')
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

if __name__ == "__main__":
    main(sys.argv[1:])     
