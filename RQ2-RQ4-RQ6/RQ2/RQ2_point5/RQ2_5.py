import pandas as pd
import dask.dataframe as dd
import os
import matplotlib.pyplot as plt

if __name__ == '__main__':

    """
    In this program we just count the number of post types that we can found inside the
    dataset
    """

    # Punto 5, RQ2
    posts = dd.read_csv("instagram_posts.csv", sep='\t',usecols=['post_type'])
    posts = posts.groupby('post_type')['post_type'].aggregate({'post_type': 'count'}).compute()
    print("Number of posts with only photos: ",posts.to_frame().iloc[1,0],
          "\nNumber of posts with both photos and videos: ", posts.to_frame().iloc[2,0])