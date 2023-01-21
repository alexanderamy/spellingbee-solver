import pandas as pd

def reader(path):
    words_df = pd.read_csv(path, header=None)
    words_df[0] = words_df[0].astype(str).str.lower()
    words_ls = list(words_df[0].unique())
    return words_ls
    