import pandas as pd
import dask.dataframe as dd
import os
import matplotlib.pyplot as plt

if __name__ == '__main__':

    """ 
    In this program we use the 'query' function to get all the records with the max number of
    comments in the dataset
    """

    # Punto 2, RQ2
    posts = dd.read_csv("instagram_posts.csv", sep='\t',
                        usecols=['post_id', 'numbr_likes','number_comments'],
                        dtype={'numbr_likes': 'float64','number_comments': 'float64'})

    print(posts[["post_id", "numbr_likes"]]
          .query(f'number_comments == {posts["number_comments"].max().compute()}')
          .compute())