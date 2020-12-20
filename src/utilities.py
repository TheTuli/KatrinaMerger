import base64
import pandas as pd


def read_csvs(file):
    return pd.read_csv(file)


def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(
        csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    return f'<a href="data:file/csv;base64,{b64}">Download csv file</a>'


def read_and_drop(files):
    df = []
    progress_bar = st.progress(0)
    for i, file in enumerate(files):
        df.append(read_csvs(file))
        progress_bar.progress((i + 1) / len(files))

    df = pd.concat(df)
    columns_indexes_to_merge_on = [0, 3, 4, 5, 6, 7, 8, 9, 10, 11, 27, 28, 46,
                                   47, 60]
    columns_to_merge_on = [df.columns.values[i] for i in
                           columns_indexes_to_merge_on]
    df = df.drop_duplicates(subset=columns_to_merge_on, keep="first")
    return df
