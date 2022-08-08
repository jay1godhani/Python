import os
import csv
with open('Met_office_2011_Air_Data.csv') as file:
     csvFile = csv.reader(file)
     
if os.path.exists('output'):
        
        if os.path.join('output/','single.csv'):
                with open(r'output/single.csv', 'w', newline='') as f:
                        
                    writer = csv.writer(f)
                    singlelist = list(filter( lambda x: x if x[5]=='Single' else None,list2))
                    writer.writerows(singlelist)
                    
        if os.path.join('output/','return.csv'):
                with open(r'output/return.csv', 'w', newline='') as f:
                    writer = csv.writer(f)
                    returnlist = list(filter( lambda x: x if x[5]=='Return' else None,list2))
                    writer.writerows(returnlist)
