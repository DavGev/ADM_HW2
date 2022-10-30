import dask.dataframe as dd

if __name__ == '__main__':

    posts = dd.read_csv("instagram_posts.csv", sep='\t',usecols=['profile_id','cts'],parse_dates=['cts'],dtype={'profile_id':'string'})

    diffMean = dd.Aggregation('diffMean', chunk=lambda x: x.diff(), agg=lambda x0: x0.mean())

    posts = posts.groupby(['profile_id'])\
        .agg({'cts': [diffMean]})\
        .compute() \
        .sort_values(('cts','diffMean'), ascending=True)

    print(posts.head(3))