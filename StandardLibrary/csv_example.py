import csv

with open("./data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["transcation_id", "product_id", "$price"])
    writer.writerow(["1000", "8435", "$1"])
    writer.writerow(["1001", "34756", "$827"])
