"""Preprocessing functionality"""
import pandas as pd

def vehicle_age_to_int(vehicle_age_col: pd.Series) -> pd.Series:
    """ return a column where categorical string is mapped to int

    Args:
        vehicle_age_col (pd.Series): the column of the df 

    Returns:
        pd.Series: mapped to int values
    """
    map_vehicle_age = {
        '< 1 Year': 0,
        '1-2 Year': 1,
        '> 2 Years': 2
    }
    return vehicle_age_col.map(map_vehicle_age)

def map_categorical_to_int(df: pd.DataFrame) -> pd.DataFrame:
    """map categorical str columns of the df to integer categories

    Args:
        df (pd.DataFrame): the dataframe

    Returns:
        pd.DataFrame: dataframe with numeric columns
    """

    # convert region code and policy sales channel to int for readability
    df_mapped = df.copy()
    df_mapped[["Region_Code", "Policy_Sales_Channel"]] = df_mapped[["Region_Code", "Policy_Sales_Channel"]].astype(int)

    # one-hot encode
    categorical_cols = ["Gender", "Vehicle_Damage", "Region_Code", "Policy_Sales_Channel"]
    # TODO: group "other" channels to reduce load of one hot encoding
    df_mapped = pd.get_dummies(data = df_mapped, columns=categorical_cols, drop_first=True, dtype=int)

    # use vehicle_age_to_int function to maintain ordering
    df_mapped["Vehicle_Age"] = vehicle_age_to_int(df_mapped["Vehicle_Age"])
    
    return df_mapped