import csv


def estimatedPrice(mileage):
    return theta0 + (theta1 * mileage)


import csv

mileage = []
price = []

with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        mileage.append(float(row['km']))
        price.append(float(row['price']))

learning_ratetheta0 = 0.75
learning_ratetheta1 = 0.0000000000015

m = len(mileage)

theta0 = 0
theta1 = 0

tmptheta0 = 0
tmptheta1 = 0
# value1 = 0
# value2 = 0
sommeValue0 = 0
sommeValue1 = 0
test1 = 0
test2 = 0
for i in range(8000):
    sommeValue1 = 0
    sommeValue0 = 0
    for i in range(m):
        predictedPrice = estimatedPrice(mileage[i])
        sommeValue0 += predictedPrice - price[i]
        sommeValue1 += (predictedPrice - price[i]) * mileage[i]
    test1 = (1/m) * sommeValue0
    test2 = (1/m) * sommeValue1
    # print(test1,test2)
    tmptheta0 = learning_ratetheta0 * test1
    tmptheta1 = learning_ratetheta1 * test2
    # print(f"theta0 = {theta0} , theta1 {theta1}\n")
    theta0 -= tmptheta0
    theta1 -= tmptheta1


mileageinput = float(input())


print(f"test final = {estimatedPrice(mileageinput)} theta0 = {theta0} theta1 = {theta1}")