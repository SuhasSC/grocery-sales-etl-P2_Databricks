def check_nulls(df):
    return df.select([df[c].isNull().sum().alias(c) for c in df.columns])