#Script for extracting metadata from NCBI Taxon classification STAT from NCBI websites
#The NCBI SRA Taxonomy Analysis Tool (STAT) calculates the taxonomic 
#distribution of reads from next generation sequencing runs.
#Written by Rhys Parry r.parry@uq.edu.au March 2020
#Requires beautifulsoup dependencies

#Requirements: a file with Sra Accession Numbers called "SraAccList.txt" within the same directory as script
#Usage: python NCBISTATWebscraper.py > outputfile.txt
#Returns about 29-35 a minute

import urllib 
from bs4 import BeautifulSoup

#Reads in the accession file
sraaccessionfile = open("SraAccList.txt", "r")

#Takes every element in the accession file and puts into a list
accessionlist= sraaccessionfile.readlines()
sraaccessionfile.close()

#This replaces the /n of all your lines of the file
accessionlist = [w.replace('\n', '') for w in accessionlist]

#Prints all the accessions you are scraping
print(accessionlist)

#The following loops 

for x in accessionlist:
    url = "https://trace.ncbi.nlm.nih.gov/Traces/sra/?run="
    urlx = url+x
    print(urlx)
    f1 = urllib.request.urlopen(urlx)
    f = f1.read()    
    f1.close()
    soup = BeautifulSoup(f, features="lxml") 
    #print(soup)
    js_text = soup.find_all('script', type="text/javascript")[-1].extract()
    print("Scraped from: "+urlx)
    #print("Status code: "+ str(f.status_code))
    cleaned_taxontable = str(js_text).replace('{','').replace('}','').replace('"','').replace('<script type=text/javascript>\n            (function () \n            var oTaxAnalysisData = [','')
    cleaned_taxontable = cleaned_taxontable.replace('\n0];\n\n            utils.addEvent(window, load, function () \n            StaticTree(document.getElementById(id-tax_analysis), tax_analysis_0_, tree_transform(oTaxAnalysisData),\n            function (oD, bLast) \n            var label = oD.d.name + : <strong> + oD.d.percent + %</strong>;\n            if ( oD.d.kbp !=  && oD.d.percent == < 0.01 )  label = label +  ( + oD.d.kbp +  Kbp) ; \n            return label;\n            );  ); )();\n          </script>''','')
    print(cleaned_taxontable)
