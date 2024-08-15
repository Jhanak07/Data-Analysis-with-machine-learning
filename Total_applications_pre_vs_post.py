import pandas as pd

data = pd.read_csv('Data.csv')

data['date_of_posting'] = pd.to_datetime(data['date_of_posting'], unit='s')
data['api_applications_created'] = pd.to_datetime(data['api_applications_created'], unit='s')

start_date = pd.to_datetime('2015-09-01')
end_date = pd.to_datetime('2018-11-30')

data = data[(data['date_of_posting'] >= start_date) & (data['date_of_posting'] <= end_date)]

legislation_date = pd.to_datetime('2017-03-09')

pre_legislation = data[data['date_of_posting'] < legislation_date]
post_legislation = data[data['date_of_posting'] >= legislation_date]

pre_legislation_male_count = pre_legislation[pre_legislation['FemaleFlag'] == 0].shape[0]
pre_legislation_female_count = pre_legislation[pre_legislation['FemaleFlag'] == 1].shape[0]

post_legislation_male_count = post_legislation[post_legislation['FemaleFlag'] == 0].shape[0]
post_legislation_female_count = post_legislation[post_legislation['FemaleFlag'] == 1].shape[0]

print(f"Pre-legislation (Sep 1, 2015 - Mar 8, 2017): Male Applicants: {pre_legislation_male_count}, Female Applicants: {pre_legislation_female_count}")
print(f"Post-legislation (Mar 9, 2017 - Nov 30, 2018): Male Applicants: {post_legislation_male_count}, Female Applicants: {post_legislation_female_count}")
