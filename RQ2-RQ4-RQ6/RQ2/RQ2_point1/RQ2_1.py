import dask.dataframe as dd

if __name__ == '__main__':

    """
    In this point we just use the groupby function to group the dataset by profile_id and then
    we use the aggregation agg({'n_posts': 'max'}) to eliminate the duplicates since in the
    docs it said that this is the numbers of posts recorded during the last visit.
    Then, we just sort the values.
    """
    #Punto 1, RQ2
    profiles = dd.read_csv("instagram_profiles.csv", sep='\t', usecols=['n_posts', 'profile_id'],dtype={'profile_id': 'float64'})
    profiles = profiles.groupby('profile_id').agg({'n_posts': 'max'}).compute().sort_values('n_posts', ascending=False)
    print(profiles)