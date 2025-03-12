import csv


file = open("data.csv", "w")
file. close()

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["transaction_id", "product_id", "price"])
    writer.writerow([1000, 1, 51])
    writer.writerow([1001, 2, 15])

with open("data.csv") as file:
    reader = csv.reader(file)
    # print(list(reader))
    # [['transaction_id', 'product_id', 'price'], ['1000', '1', '51'], ['1001', '2', '15']]

    for row in reader:
        print(row)
    # ['transaction_id', 'product_id', 'price']
    # ['1000', '1', '51']
    # ['1001', '2', '15']
