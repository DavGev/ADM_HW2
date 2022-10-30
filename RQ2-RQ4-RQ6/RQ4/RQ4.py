import dask.dataframe as dd

"""
The first function allows us to get every post posted by a single profile
The second function allows us to get the top n profiles with most posts
The third function gets the avg likes avg comments for the top n profile that actually posted something
"""

#Function requested for the exercise RQ4_1
def get_posts(id_profile):
    posts = dd.read_csv("../instagram_posts.csv",
                        sep='\t',
                        usecols=['post_id', 'profile_id'],
                        dtype={'profile_id': 'float64'})
    posts = posts\
        .query(f'profile_id == {id_profile}')\
        .compute()
    return posts

#Function requested for the exercise RQ4_2
def top_n_posts(n):
    profiles = dd.read_csv("../instagram_profiles.csv",
                        sep='\t',
                        usecols=['profile_id', 'n_posts'],
                        dtype={'profile_id': 'string'})
    profiles = profiles\
        .groupby('profile_id')\
        .agg({'n_posts': 'max'})\
        .compute()\
        .sort_values('n_posts', ascending=False)\
        .head(n)
    return profiles

#Function requested for the exercise RQ4_3
def avg_comments_and_likes():
    posts = dd.read_csv("../instagram_posts.csv",
                        sep='\t',
                        usecols=['numbr_likes','number_comments','profile_id'],
                        dtype={'post_id': 'string','profile_id': 'string','number_comments': 'float16','numbr_likes': 'float16'}).dropna(subset=['profile_id']).compute()
    posts = posts.set_index('profile_id')

    profiles = dd.read_csv("../instagram_profiles.csv",
                        sep='\t',
                        usecols=['profile_id','n_posts'],
                        dtype={'profile_id': 'string','n_posts': 'float32'}).dropna(subset=['profile_id']).compute()
    profiles = profiles.set_index('profile_id')

    merged = dd.merge(posts, profiles, how="inner", left_index=True, right_index=True)\
        .groupby(['profile_id'])\
        .agg({'n_posts': 'max','number_comments': 'mean','numbr_likes': 'mean'})\
        .sort_values('n_posts', ascending=False)
    print(merged.head(10))

if __name__ == '__main__':
    print(get_posts("2237947779")) #Example profile_id for RQ4_1
    #print(top_n_posts(20))  # Example counter for RQ4_2
    #avg_comments_and_likes()