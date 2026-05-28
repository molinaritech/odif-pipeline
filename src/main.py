import pandas as pd

def main():
    data = {
        "product": ["Notebook","Sticker", "Mug"],
        "sales": [25, 40, 15]
    }

    df = pd.DataFrame(data)

    print("\nSales Data:")
    print(df)

    print("\nTotal Sales:")
    print(df["sales"].sum())


if __name__ == "__main__":
    main()
