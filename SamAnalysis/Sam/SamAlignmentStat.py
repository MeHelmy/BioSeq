'''
Created on Dec 8, 2014

@author: medhat
'''

import sys , getopt

def main(argv):
    inputFile = ''

    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print 'SamAlignmentStat.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'SamAlignmentStat.py -i <inputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputFile = arg
      
        elif opt in ("-o", "--ofile"):
            outPut = arg
    
def is_empty(any_structure):
    if any_structure:
        #print('Structure is not empty.')
        return False
    else:
        #print('Structure is empty.')
        return True
    
    
    
if __name__ == "__main__":
    main(sys.argv[1:])  