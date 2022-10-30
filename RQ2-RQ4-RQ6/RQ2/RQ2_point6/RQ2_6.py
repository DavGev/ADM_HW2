import pandas as pd
import dask.dataframe as dd
import os
import matplotlib.pyplot as plt

if __name__ == '__main__':

    # Punto 6, RQ2
    posts = dd.read_csv("instagram_profiles.csv",usecols=['post_type','is_business_account'], sep='\t',dtype={'profile_id': 'string'})
    posts = posts.groupby(['is_business_account'])['is_business_account'].aggregate({'is_business_account': 'count'}).compute()
    business_acc_true = posts.to_frame().iloc[0,0]
    business_acc_false = posts.to_frame().iloc[1,0]
    tot = business_acc_true + business_acc_false
    print("Percentage of business accounts: ",(business_acc_true/tot * 100),
          "\nPercentage of non-business accounts:",(business_acc_false/tot * 100))