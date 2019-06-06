import pandas as pd


def load_and_prepare(source):
    data = pd.read_csv(source, low_memory=False)
    data.dropna(inplace=True)
    data.drop(columns=['Unnamed: 0'], inplace=True)

    data.rename(columns={n: n.lower() for n in data.columns}, inplace=True)
    categorical_columns = [
        'gender',
        'student',
        'married',
        'ethnicity'
    ]
    for name in categorical_columns:
        data[name] = data[name].astype('category')

    income_groups = {
        'The Poor': 0,  # - 18
        'Working Class': 18,  # - 30
        'Lower-Middle Class': 30,  # - 50
        'Upper-Middle Class': 50,  # - 100
        'The Rich': 100,  # - ...
    }
    data['income_group'] = pd.cut(data['income'], list(income_groups.values()) + [data['income'].max() + 1],
                                  right=False, labels=income_groups.keys())

    return data
