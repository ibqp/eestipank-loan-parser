import re
import pandas as pd

def _get_period_columns(cols_json):
    period_cols = cols_json["upperRows"][0]["cellList"]
    periods = [re.findall(r'\d{2}/\d{4}', col['cellText'])[1] for col in period_cols]
    return periods

def _filter_data(data_json):
    filtered_data = [
        {key:value for key,value in dictionary.items() if 'veerg' in key}
        for dictionary in data_json
    ]
    return filtered_data

def _return_dataframe(values, fields):
    # duplicate each value in fields list (which are periods)
    duplicated_periods = [
        pd.to_datetime(date, format='%m/%Y').strftime('%Y-%m')
        for date in fields for _ in range(2)
    ]

    df = pd.DataFrame(values)
    df = (
        df
        .rename(columns=dict(zip(df.columns, duplicated_periods)))
        .rename(columns={'veerg_a_0': 'metric'})
        .replace('%', '', regex=True)
    )

    return df

def _process_df(df, fields_slice, value_name):
    metric = df['metric']
    values = df.drop('metric', axis=1).iloc[:, fields_slice]

    result = (
        pd
        .concat([metric, values], axis=1)
        .query('metric == "Overdue loans"')
        .melt(id_vars='metric', var_name='period', value_name=value_name) # convert from wide to long
        .drop('metric', axis=1)
        .sort_values(by='period', ascending=True)
        .reset_index(drop=True)
    )
    result[value_name] = result[value_name].astype(float)

    return result

def get_title(cols_json):
    title = f"{cols_json['reportTitlePrev']} {cols_json['title']}"
    return title

def prepare_raw_dataframe(data_json, cols_json):
    periods = _get_period_columns(cols_json)
    data = _filter_data(data_json)
    df = _return_dataframe(values=data, fields=periods)
    return df

def return_result_df(df):
    values = _process_df(df, slice(0, None, 2), 'overdue_loans')
    shares = _process_df(df, slice(1, None, 2), 'overdue_loans_share')
    result = pd.merge(values, shares, on='period')
    return result
