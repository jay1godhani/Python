import csv
import os


JAY = []
with open('Met_office_2011_Air_Data.csv') as file:
    
    csv_file = csv.DictReader(file)
    
    TotalSum = 0
    godhani = {}
    
    for row in csv_file:
        TotalSum = TotalSum+float(row["Total Cost ex VAT"])
        
        if row["Air Carrier"] in godhani:
            godhani[row["Air Carrier"]] = godhani[row["Air Carrier"]] + \
                float(row["Total Cost ex VAT"])
        else:
            godhani[row["Air Carrier"]] = float(row["Total Cost ex VAT"])
            
    print("Total Sum: ", TotalSum)
    sort_orders = sorted(godhani.items(), key=lambda x: x[1], reverse=False)

    for i in sort_orders:
        print(i[0], i[1])
