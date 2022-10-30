import pandas as pd
import dask.dataframe as dd
import os
import matplotlib.pyplot as plt

if __name__ == '__main__':

    """
    In this program we first print the posts with the lowest number of comments (which is supposed
    to be zero) and the we print the one with the highest number.
    """

    # Punto 3, RQ2
    posts = dd.read_csv("instagram_posts.csv", sep='\t',usecols=['post_id', 'number_comments'],dtype={'number_comments': 'float64'})

    print(posts.query('number_comments == 0').compute())

    print(posts[["post_id","number_comments"]]
          .query(f'number_comments == {posts["number_comments"].max().compute()}')
          .compute())