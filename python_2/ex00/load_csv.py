import pandas as pd


def load(path: str) -> pd.DataFrame:
    """ doc """
    try:
        df = pd.read_csv(path)
        dimensions = df.shape
        print(dimensions)
        return df
    except Exception as e:
        print(e)
        return None
