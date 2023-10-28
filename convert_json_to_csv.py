import json
import csv

with open("input_json_file.json","r") as f:
    data = json.load(f)
    x = data ["employees"]

with open ("output_csv_file.csv","w") as f:
    fieldnames = x[0].keys()
    writer = csv.DictWriter(f, fieldnames =fieldnames)
    writer.writeheader()
    for name in x:
        writer.writerow(name)