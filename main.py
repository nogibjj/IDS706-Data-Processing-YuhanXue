from mylib.lib import get_mean, get_median, get_stddev
import pandas as pd


def main():
    df = pd.read_csv("diabetes.csv")

    column_name = "Age"

    if column_name in df.columns:
        # Print the computed statistics
        print(f"Statistics for column '{column_name}':")
        print(f"Mean: {get_mean(df, 'Age'):.2f}")
        print(f"Median: {get_median(df, 'Age'):.2f}")
        print(f"Standard Deviation: {get_stddev(df, 'Age'):.2f}")
    else:
        print(f"Column '{column_name}' not found in the dataset.")


if __name__ == "__main__":
    main()
