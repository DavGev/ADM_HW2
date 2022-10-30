wget https://adm2022.s3.amazonaws.com/instagram_posts.zip
wget https://adm2022.s3.amazonaws.com/instagram_profiles.zip

unzip instagram_posts.zip
unzip instagram_profiles.zip

awk 'length($8)>100 {print $4}' instagram_posts.csv | head -n 10 > temp.csv

grep -f temp.csv instagram_profiles.csv | awk '{print $4}'
