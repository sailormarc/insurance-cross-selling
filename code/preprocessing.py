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

    categorical_cols = ["Gender", "Vehicle_Damage"]
    df_mapped = df.copy()
    for col in categorical_cols:
        df_mapped[col] = pd.factorize(df_mapped[col])[0]

    # use vehicle_age_to_int function to maintain ordering
    df_mapped["Vehicle_Age"] = vehicle_age_to_int(df_mapped["Vehicle_Age"])
    
    
    return df_mapped