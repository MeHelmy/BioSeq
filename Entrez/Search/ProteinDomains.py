'''
Created on Apr 23, 2014

@author: medhat
'''
import subprocess,os,sys,getopt

def main(argv):
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
    loopDirectory(inputFile, outputFile)


#Read all the files in directory and process them one by one
def loopDirectory(directory,resultDirectory):
        
    print("Reading from directory ==> " + directory)
    for fn in os.listdir(directory):
        print("#===============***===================>  New Record  <===============***===================#")    
        if os.path.isfile(os.path.join(directory,fn)):
            # call method to process the file
            fileName = str(fn).rsplit('.',1)[0]
            print("Reading from file ==> " + fn)
            fn = directory+fn
            # forming the command this is based on the read me pfam help command
            cmd = 'perl ~/source/PfamScan/pfam_scan.pl -fasta '+ fn +' -dir ~/Downloads/pfam-files'
            
            processFasta(cmd, resultDirectory,fileName)
        else:
            print("Sorry "+fn+" Is not a file")
 
def processFasta(cmd,resultDirectory,fileName):
    print("Writing to directory #==> " + resultDirectory)
    foDic = open("found_domains.txt",'a')
    firstTime = True
    if os.path.exists(resultDirectory):
        fo=open(resultDirectory,'a')
    else:
        fo = open(resultDirectory,'w') 
     
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    out, err = p.communicate() 
    result = out.split('\n')
    for lin in result:
        if not lin.startswith('#') and  lin:

            if firstTime:
                fo.write("=========================================================\n")
                fo.write(fileName+'\n')
                foDic.write(fileName+'\n')
                firstTime = False
                        
            fo.write(lin+'\n')
    
    fo.close()
    
if __name__ == "__main__":
    main(sys.argv[1:])  


