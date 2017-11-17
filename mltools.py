import pandas as pd

def chunkify(filename, **kwargs):
    chunker = pd.read_csv(filename, **kwargs)
    first = next(chunker)
    return chunker, first

def memory_cost(df):
    memory = df.memory_usage()
    result = pd.DataFrame(memory / 1024**2)
    result = pd.concat([result, df.dtypes], axis=1)
    result.columns = ['MB', 'dtype']
    result = result.sort_values(by='MB', ascending=False)
    total_mem = result['MB'].sum()
    result = result.append(pd.Series({'MB': total_mem}, name='Total'))
    return result

def range_vals(df):
    mins = df.min()
    maxes = df.max()
    result = pd.concat([maxes, mins], axis=1)
    result.columns = ['max', 'min']
    return result

def count_nulls(df):
    result = pd.DataFrame(df.isnull().sum(), columns=['nulls'])
    return result