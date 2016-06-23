# read in fred.csv unemployment data

import csv

output = open("fred-html.txt", "w+")

with open('fred.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
        
    for i in reader:
        date = i[0].rsplit('-', 1)
        output.write('\t<tr>\n')
        output.write('\t\t<td>'+date[0]+'</td>\n')
        output.write('\t\t<td>'+i[1]+'</td>\n')
        output.write('\t\t<td>'+i[2]+'</td>\n')            
        output.write('\t</tr>\n')

output.close()
