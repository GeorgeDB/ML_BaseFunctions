# Base function to convert categorical values in a dataframe to custom numerical values as defined
# Feel free to use the function as needed
# Further updates will be done to make the function more complete, with the necessary error trapping
#   steps and more possibilities for the configuration

def transform_categorical_to_numerical(df, columns_values_to_transform):
    """
    Transform specified categorical columns in a DataFrame to specified value in dictionary.

    Args:
        df: The DataFrame to be modified
        columns_values_to_tranform: A dictionary of dictionaries, where each main key is a column
                                    and the smaller dictionaries represents the possible values to
                                    be converted (keys) to which value (value).

    Returns:
        The modified DataFrame with transformed columns.
    """

    for column_name, values_to_transform in columns_values_to_transform.items():
        for from_value, to_value in values_to_transform.items():
            df[column_name] = df[column_name].apply(lambda x: to_value if x == from_value else x)

    return df
    