

import csv 

with open('neurosynth_db.txt','rbU') as fin:
    cr = csv.reader(fin,delimiter='\t')
    filecontents = [line for line in cr]

with open('neurosynth_db.csv', 'wb') as fou:
    cw = csv.writer(fou, quotechar='',quoting=csv.QUOTE_NONE)
    cw.writerows(filecontents)
    cw.close()