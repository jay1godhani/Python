import csv

def getcsvrows(filename, header, rows):
    with open(filename, "r") as f:
        
        
        csvreader = csv.reader(f)
        header.append(next(csvreader))
        
        for row in csvreader:
            rows.append(row)
            
def lastcost(filename, dest):
    header, rows = [], []
    getcsvrows(filename, header, rows)
    totalsum, count = 0, 0
    
    for i in rows:
        if i[10] == dest:
            totalsum += float(i[3])
            count += 1
            
    if count > 0:
        return {'total': totalsum, 'total count': count ,'average cost': totalsum/count}
    else:
        return {'total': 0, 'average cost': 0}
    
print(lastcost("Met_Office_2011_Air_Data.csv", "JERSEY"))
