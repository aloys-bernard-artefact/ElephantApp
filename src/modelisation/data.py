import os
import pandas as pd


def load_data() -> pd.DataFrame:
    """
    Try to load the data from the data folder (localy)
    If data doesn't exist, fetch it from the web and save it in the data folder
    In the end, return the data as a pandas DataFrame
    """
    if not os.path.exists("data/raw_data.csv"):
        # Fetch the data from the web
        try:
            data = pd.read_csv(os.environ.get("DATA_URL"))
        except Exception as e:
            print("Error fetching the data")
            print(e)
            return None
        # Save the data in the data folder
        print("Saving the data in the data folder")
        data.to_csv("data/raw_data.csv", index=False)
    data = pd.read_csv("data/raw_data.csv")
    print(data.shape)
    return data


def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the data by removing missing values and duplicates
    """
    # This was the logic to clean the data
    # # Remove columns if they contain more than 30% missing values
    # data.dropna(thresh=0.7*data.shape[0], axis=1, inplace=True)
    # # Remove rows if they contain missing values
    # data.dropna(axis=0, inplace=True)
    # # Remove duplicates
    # data.drop_duplicates(inplace=True)
    # return data

    # Now we want to "hard code" the name of the columns to drop
    # and the name of the columns to keep
    columns_to_keep = [
        "Id",
        "MSSubClass",
        "MSZoning",
        "LotFrontage",
        "LotArea",
        "Street",
        "LotShape",
        "LandContour",
        "Utilities",
        "LotConfig",
        "LandSlope",
        "Neighborhood",
        "Condition1",
        "Condition2",
        "BldgType",
        "HouseStyle",
        "OverallQual",
        "OverallCond",
        "YearBuilt",
        "YearRemodAdd",
        "RoofStyle",
        "RoofMatl",
        "Exterior1st",
        "Exterior2nd",
        "MasVnrArea",
        "ExterQual",
        "ExterCond",
        "Foundation",
        "BsmtQual",
        "BsmtCond",
        "BsmtExposure",
        "BsmtFinType1",
        "BsmtFinSF1",
        "BsmtFinType2",
        "BsmtFinSF2",
        "BsmtUnfSF",
        "TotalBsmtSF",
        "Heating",
        "HeatingQC",
        "CentralAir",
        "Electrical",
        "1stFlrSF",
        "2ndFlrSF",
        "LowQualFinSF",
        "GrLivArea",
        "BsmtFullBath",
        "BsmtHalfBath",
        "FullBath",
        "HalfBath",
        "BedroomAbvGr",
        "KitchenAbvGr",
        "KitchenQual",
        "TotRmsAbvGrd",
        "Functional",
        "Fireplaces",
        "GarageType",
        "GarageYrBlt",
        "GarageFinish",
        "GarageCars",
        "GarageArea",
        "GarageQual",
        "GarageCond",
        "PavedDrive",
        "WoodDeckSF",
        "OpenPorchSF",
        "EnclosedPorch",
        "3SsnPorch",
        "ScreenPorch",
        "PoolArea",
        "MiscVal",
        "MoSold",
        "YrSold",
        "SaleType",
        "SaleCondition",
    ]
    if "SalePrice" in data.columns:
        columns_to_keep.append("SalePrice")
    data = data.loc[:, columns_to_keep]
    return data.dropna().drop_duplicates().dropna()


if __name__ == "__main__":
    load_data()
