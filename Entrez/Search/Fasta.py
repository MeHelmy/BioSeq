'''
Created on Mar 11, 2014

@author: medhat
'''
from Bio import Entrez
Entrez.email = "medhat.helmy77@gmail.com"
handle = Entrez.esearch(db="nucleotide", term="GRMZM2G326270_T01")
record = Entrez.read(handle)
recordId = record["IdList"][0]

# get fasts
handleSeq = Entrez.efetch(db="nucleotide", id=recordId, rettype="fasta", retmode="text")
of = open("/home/medhat/Downloads/lol.txt","w")
of.write(handleSeq.read())
of.close()


# for a list of IDs
id_list=[]
search_results = Entrez.read(Entrez.epost("pubmed", id=",".join(id_list)))
webenv = search_results["WebEnv"]
query_key = search_results["QueryKey"]
