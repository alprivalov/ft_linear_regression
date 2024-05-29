import pandas as ps


def load(path: str) -> ps.DataFrame:
    """
1.  On read le path pour recuperer les donnee depuis un .csv
    """
    data_frame = ps.read_csv(path)
    print("Loading dataset of dimensions", data_frame.shape)
    return data_frame
