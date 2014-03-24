'''
Created on Dec 10, 2013

@author: medhat

This module get smallest and largest introns
'''
#import matplotlib.pyplot as plot , collections ,
import sys , getopt ,collections 
import matplotlib.pyplot as plot 
#from matplotlib.sphinxext.plot_directive import align


def main(argv):
    inputFile = ''

    try:
        opts, args = getopt.getopt(argv,"hi:",["ifile="])
    except getopt.GetoptError:
        print 'Intron.py -i <inputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'Intron.py -i <inputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputFile = arg
            dic=getIntronLength(inputFile)
            writeFile(dic)
            histogramOfMismatch(dic)
            print "DONE!"

def is_empty(any_structure):
    if any_structure:
        #print('Structure is not empty.')
        return False
    else:
        #print('Structure is empty.')
        return True
    
def getIntronLength(gffFile):
    if gffFile:
        intronList={}
        fo = open(gffFile , 'r')
        for line in fo:
            columns = line.split('\t')
            if columns[2] == 'intron':
                if not int(columns[4]) - int(columns[3]) == 0:
                    intronSize = int(columns[4]) - int(columns[3])
                if int(intronSize) not in intronList:
                    intronList[int(intronSize)] = 1
                else:
                    intronList[int(intronSize)] = int(intronList[int(intronSize)])+1
                    #print "max intron =====> "+ str(max(intronList))+"\n"+"min intron =====> "+str(min(intronList))
        return intronList
def writeFile(introndictionary):
    if not is_empty(introndictionary):
        fo = open('intronReads.txt','a')
        fo.write("Intron_Size\tFrequence\n")
        for k , v in introndictionary.iteritems():
            fo.write(str(k)+"\t"+str(v)+"\n")
        fo.close()
        
def histogramOfMismatch(mismatchDictionary):
        od = collections.OrderedDict(sorted(mismatchDictionary.items()))
        plot.bar(od.keys(),od.values(),align='center')
        plot.show()         

if __name__ == "__main__":
    main(sys.argv[1:])  
                
                
                
            