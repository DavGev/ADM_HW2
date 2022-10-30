import pandas as pd
import dask.dataframe as dd
import os
import matplotlib.pyplot as plt

if __name__ == '__main__':

    """
    In this program we calculate the difference between posts with tagged locations and posts with
    non tagged locations (the one where the location_id is set as null). Then, we plot the results
    on a bar graph.
    """

    # Punto 4, RQ2
    posts = dd.read_csv("instagram_posts.csv", sep='\t',usecols=['post_id', 'location_id'],dtype={'location_id': 'float64'})
    dim_tot = len(posts)
    dim_tagged_locations = len(posts.dropna(subset=['location_id']))
    dim_non_tagged_loc = dim_tot - dim_tagged_locations

    data = {'location_true':dim_tagged_locations, 'location_false':dim_non_tagged_loc}
    names = list(data.keys())
    values = list(data.values())
    # creating the bar plot
    plt.bar(names, values, color='maroon',
            width=0.4)

    plt.xlabel("Tagged status")
    plt.ylabel("No. of posts")
    plt.title("Number of posts with and without tagged locations")
    plt.show()