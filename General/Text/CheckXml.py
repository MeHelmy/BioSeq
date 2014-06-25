'''
Created on Jun 24, 2014

@author: medhat
'''
from string import strip
__author__ = 'medhat'

import sys , re

argument = []
for arg in sys.argv[1:]:
    argument.append(arg)

def chekLine(inputFile):
        if inputFile:
            fo = open(inputFile,'r')
            num = 1
            for line in fo:
                line = line.strip()

                if line.startswith("<Hsp_qseq>") and not line.endswith("</Hsp_qseq>"):
                    print(num)
                    print(line)
                num +=1
                
#chekLine(argument[0])
chekLine("/home/medhat/Samples/merge_test/NewmRNA/allMaizeGeneGoResult/blast_result/largZea_blast.xml")
