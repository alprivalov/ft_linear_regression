from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import pandas as ps
from sklearn.utils import check_array


def load(path: str) -> ps.DataFrame:
    """
1.  On read le path pour recuperer les donnee depuis un .csv
    """
    try:
        data_frame = ps.read_csv(path)
        check_array(data_frame)
        return data_frame
    except (FileNotFoundError, ValueError) as msg:
        print("Error:", msg)
        exit(1)


def get_data():
    """
    return: dataframe from data.csv
    """
    data_frame = load("data.csv")
    try:
        mileage = data_frame["km"]
        price = data_frame["price"]
        return mileage, price
    except KeyError as msg:
        print("Error", msg)
        exit(1)


def get_max_min_values(mileage, price):
    return max(mileage), min(mileage), min(price), max(price)


def get_max_min_scaling(mileage, price):
    """
    use: scale mileage to min - max scaling for better processing and learning
    return: scaled array
    """
    max_m, min_m, min_p, max_p = get_max_min_values(mileage, price)

    #   ratios = current mileage / biggest mileage
    scaled_mileage = (mileage - min_m) / (max_m - min_m)

    #   ratios = current price / biggest price
    scaled_price = (price - min_p) / (max_p - min_p)

    return scaled_mileage, scaled_price


def gradient_descent(mileage, price):
    """
    use : gradiant_descend algorithme learn theta0 theta1 with n iteration
    return: theta1 theta0
    """
    def estimatedPrice(mileage):
        return (theta1 * mileage) + theta0
    learning_rate1 = 0.3
    theta1 = 0
    theta0 = 0
    cost = 0
    iteration = 0
    theta_history = []
    m = len(mileage)
    y_pred = estimatedPrice(mileage)
    cost = (1 / 2*m) * (sum(y_pred - price)**2)
    while cost > 0.01:
        y_pred = estimatedPrice(mileage)
        iteration += 1
        theta0 -= learning_rate1 * sum(y_pred - price) / m
        theta1 -= learning_rate1 * sum((y_pred - price) * mileage) / m
        cost = (1 / 2*m) * ((sum(y_pred - price)**2))
        theta_history.append((theta0, theta1, cost, iteration))
    return theta0, theta1, theta_history


def write_file(theta0, theta1):
    """
    use: write theta1 theta0 in theta.csv file
    used in estimateprice program
    """
    mileage, price = get_data()
    max_m, min_m, min_p, max_p = get_max_min_values(mileage, price)

    with open("theta.csv", "w") as f:
        theta = "theta0,theta1,"
        max_min = "max_mileage,min_mileage,min_price,max_price\n"
        f.write(
            f"{theta}{max_min}")
        f.write(
            f"{theta0},{theta1},{max_m},{min_m},{min_p},{max_p}")


def display(scaled_mileage, mileage, price, theta_history):
    """
    args : X data
    use : display linear regression line and scatter all points of the data
    """
    def estimatedPrice(mileage, theta1, theta0):
        return (theta1 * mileage) + theta0
    fig, ax = plt.subplots()
    ax.scatter(mileage, price)
    line, = ax.plot([], [], color='red')

    plt.xlabel("Mileage")
    plt.title("Linear regression")
    plt.ylabel("Price")

    _, _, min_price, max_price = get_max_min_values(mileage, price)
    annotation = ax.text(0.05, 0.05, '', transform=ax.transAxes, va='bottom')

    def init():
        line.set_data([], [])
        return line

    def animate(frame):
        theta0, theta1, cost, iteration = theta_history[frame]
        Y_pred = estimatedPrice(scaled_mileage, theta1, theta0)
        Y_pred = Y_pred * (max_price - min_price) + min_price
        line.set_data(mileage, Y_pred)
        annotation.set_text(f"cost: {cost}\niteration: {iteration}")
        return line, annotation
    len_t = len(theta_history)
    FuncAnimation(
        fig, animate,
        frames=len_t,
        init_func=init,
        blit=True,
        interval=1
        )
    plt.show()


def train_model():
    """
    use: train de model with gradient_descend algorithme
    """
    mileage, price = get_data()

    scaled_mileage, scaled_price = get_max_min_scaling(mileage, price)
    theta0, theta1, theta_history = gradient_descent(
        scaled_mileage,
        scaled_price)
    display(scaled_mileage, mileage, price, theta_history)
    write_file(theta0, theta1)


def main():
    """
    Fonction principale pour entraîner le modèle.
    """
    train_model()


if __name__ == "__main__":
    main()
