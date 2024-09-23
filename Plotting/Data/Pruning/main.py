import seaborn as sns
import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("./dataset.csv")
    print(df.head())

