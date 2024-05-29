import csv
from load_csv import load
import matplotlib.pyplot as plt 


def load_data(path:str):
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            theta0 = float(row['theta0'])
            theta1 =  float(row['theta1'])
        return theta0,theta1


def main():
    mileageinput = float(input())
    def estimatedPrice(mileage):
        return theta0 + (theta1 * mileage)
    

    data_frame = load("data.csv")
    mileage = data_frame["km"].values.flatten().tolist()
    price = data_frame["price"].values.flatten().tolist()
    
    plt.plot(mileage,price,"o")
    plt.show()

    data_frame = load('theta.csv')
    theta0 = data_frame["theta0"].values
    theta1 = data_frame["theta1"].values
    print(f"Value estimated = {estimatedPrice(mileageinput)} with : theta0 = {theta0} theta1 = {theta1}")


if __name__ == "__main__":
    main()