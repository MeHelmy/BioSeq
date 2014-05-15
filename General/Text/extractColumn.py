'''
Created on May 15, 2014

@author: medhat
'''
import os  ,sys , getopt
def main(argv):
    scriptName = os.path.basename(__file__)
    try:
        opts, args = getopt.getopt(argv, "hi:o:c:s:", ["ifile=", "ofile=","col1=","col2="])
    except getopt.GetoptError:
        print scriptName + ' -i <inputfile> -o <outputfile> -c <firstColumn> -s <secondColumn>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print scriptName + ' -i <inputfile> -o <outputfile> -c <firstColumn> -s <secondColumn>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputFile = arg
        elif opt in ("-o", "--ofile"):
            outputFile = arg
        elif opt in ("-c", "--col1"):
            col1 = arg
        elif opt in ("-s", "--col2"):
            col2 = arg
    extractColumn(inputFile, outputFile,col1,col2)
    
def extractColumn(inputFile, outputFile,col1,col2):
    if inputFile:
        inFile = open(inputFile,'r')
        outFile = open(outputFile , 'a')
        firstLine = inFile.next()
        firstTime = True
        #inFile.next()
        for line in inFile:
            line = line.strip()
            splitLine = line.split('\t')
            newColumn = float(splitLine[int(col1)]) - float(splitLine[int(col2)])
            if firstTime:
                outFile.write(firstLine.strip()+"\t"+"log1-log2\n")
                outFile.write(line+"\t"+str(newColumn)+"\n")
                firstTime = False
            else:
                outFile.write(line+"\t"+str(newColumn)+"\n")     
        inFile.close()
        outFile.close()
        
if __name__ == "__main__":
    main(sys.argv[1:])        