import pandas as pd

data = pd.read_csv('Data.csv')

data['date_of_posting'] = pd.to_datetime(data['date_of_posting'], unit='s')
data['api_applications_created'] = pd.to_datetime(data['api_applications_created'], unit='s')

legislation_date = pd.to_datetime('2017-03-01')

pre_legislation = data[data['date_of_posting'] < legislation_date]
post_legislation = data[data['date_of_posting'] >= legislation_date]

pre_legislation_male_applicants = pre_legislation[pre_legislation['FemaleFlag'] == 0]['fid'].nunique()
pre_legislation_female_applicants = pre_legislation[pre_legislation['FemaleFlag'] == 1]['fid'].nunique()

post_legislation_male_applicants = post_legislation[post_legislation['FemaleFlag'] == 0]['fid'].nunique()
post_legislation_female_applicants = post_legislation[post_legislation['FemaleFlag'] == 1]['fid'].nunique()

print(f"Pre-legislation: Male Applicants: {pre_legislation_male_applicants}, Female Applicants: {pre_legislation_female_applicants}")
print(f"Post-legislation: Male Applicants: {post_legislation_male_applicants}, Female Applicants: {post_legislation_female_applicants}")
