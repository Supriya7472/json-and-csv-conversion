import json
import csv

with open("input_csv_file.csv","r") as f:
    reader = csv.reader(f)
    next(reader)
    data = []
    for row in reader:
        data.append({"id": row[0],"firstname": row[1],"lastname": row[2],"email": row[3],"phone" : row[4], "address": row[5],"city":row[6],"state":row[7],"zipcode":row[8],"salary":row[9]})

with open ("output_json_file.json","w") as f:
    json.dump(data,f,indent=4)