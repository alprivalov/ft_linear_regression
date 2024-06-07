import pandas as ps
from sklearn.utils import check_array


def load(path: str) -> ps.DataFrame:
    """
1.  On read le path pour recuperer les donnee depuis un .csv
    """
    try:
        data_frame = ps.read_csv(path)
        check_array(data_frame)
        print("Loading dataset of dimensions", data_frame.shape)
        return data_frame
    except (FileNotFoundError, ValueError) as msg:
        print("Error:", msg)
        exit(1)


def main():
    """
    Fonction principale pour prédire le prix basé sur le kilométrage
    en prenant les params:
    data,theta0,theta1,max_price,min_price,min_mileage,max_mileage
    du theta.csv file
    """

    def estimatedPrice(mileage):
        """
        Calcule le prix estimé en fonction du kilométrage
        et des paramètres actuels du modèle.
        """
        return (theta1 * mileage) + theta0

    data = load("theta.csv")
    theta0 = data["theta0"].values
    theta1 = data["theta1"].values
    max_price = data["max_price"].values
    min_price = data["min_price"].values
    min_mileage = data["min_mileage"].values
    max_mileage = data["max_mileage"].values

    try:
        mileage_input = float(input("Entrez le kilométrage : "))

        max_min_mileage = max_mileage - min_mileage
        max_min_price = max_price - min_price
        current_min = mileage_input - min_mileage
        mileage_input = current_min / max_min_mileage
        finale_output = estimatedPrice(mileage_input) * max_min_price
        print(
            f"Prix = {finale_output + min_price}")
    except TypeError as msg:
        print("Error:", msg)
        exit(1)


if __name__ == "__main__":
    main()
