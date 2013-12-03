'''
Created on Nov 20, 2013

@author: medhat
Calculate mismatches in SAM file from the NM column 
'Edit distance to the reference, including ambiguous bases but excluding clipping' 
'''
import matplotlib.pyplot as plot , collections ,sys , getopt
from matplotlib.sphinxext.plot_directive import align


def main(argv):
    inputFile = ''

    try:
        opts, args = getopt.getopt(argv,"hi:",["ifile="])
    except getopt.GetoptError:
        print 'SamAnalysis.py -i <inputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'SamAnalysis.py -i <inputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputFile = arg
    histogramOfMismatch(calculateMismatchFromSam(inputFile))  

    
    
def calculateMismatchFromSam(samFile):
    if samFile:
        mismatchstats={}
        samData=open(samFile,'r')
        for line in samData:
            if not line.startswith('@'):
                colum=line.split('\t')
                intersetColumn= colum[11:]
                for column in intersetColumn:
                    if column.startswith("N"):
                        mismatchValue=column.split(":")[2]
                        mismatchValue = int(mismatchValue)
                        if mismatchValue not in mismatchstats:
                            mismatchstats[mismatchValue]=1
                        else:
                            mismatchstats[mismatchValue]=mismatchstats[mismatchValue]+1
                            

    return mismatchstats    
                    
def histogramOfMismatch(mismatchDictionary):
        od = collections.OrderedDict(sorted(mismatchDictionary.items()))
        plot.bar(od.keys(),od.values(),align='center')
        plot.show()
                    
if __name__ == "__main__":
    main(sys.argv[1:]) 
               
    
    