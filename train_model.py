import csv
from load_csv import load

def train_model():
    """
    Use: train de model to predict the price from mileage
    Return: make a new file with theta0 and theta1 values inside 
    """
    def estimatedPrice(mileage):
        return theta0 + (theta1 * mileage)
    
    learning_ratetheta0 = 0.75
    learning_ratetheta1 = 0.0000000000015

    data_frame = load("data.csv")
    mileage = data_frame["km"].values.flatten().tolist()
    price = data_frame["price"].values.flatten().tolist()
    
    theta0 = 0
    theta1 = 0
    m = len(mileage)
    for i in range(8000):
        sommeValue1 = 0
        sommeValue0 = 0
        for i in range(m):
            predictedPrice = estimatedPrice(mileage[i])
            sommeValue0 += predictedPrice - price[i]
            sommeValue1 += (predictedPrice - price[i]) * mileage[i]
        tmptheta0 = learning_ratetheta0 * ((1/m) * sommeValue0)
        tmptheta1 = learning_ratetheta1 * ((1/m) * sommeValue1)
    theta0 -= tmptheta0
    theta1 -= tmptheta1


    f = open("theta.csv", "w")
    f.write(f"theta0,theta1\n{theta0},{theta1}")
    


def main():
    train_model()
    

if __name__ == "__main__":
    main()