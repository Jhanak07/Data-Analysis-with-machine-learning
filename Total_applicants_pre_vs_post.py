import pandas as pd

# Load the dataset
data = pd.read_csv('Data.csv')

# Convert Unix timestamps to datetime for 'date_of_posting' and 'api_applications_created'
data['date_of_posting'] = pd.to_datetime(data['date_of_posting'], unit='s')
data['api_applications_created'] = pd.to_datetime(data['api_applications_created'], unit='s')

# Define the date when the legislation was passed
legislation_date = pd.to_datetime('2017-03-01')

# Separate the data into pre and post-legislation
pre_legislation = data[data['date_of_posting'] < legislation_date]
post_legislation = data[data['date_of_posting'] >= legislation_date]

# Count the number of unique male and female applicants pre-legislation
pre_legislation_male_applicants = pre_legislation[pre_legislation['FemaleFlag'] == 0]['fid'].nunique()
pre_legislation_female_applicants = pre_legislation[pre_legislation['FemaleFlag'] == 1]['fid'].nunique()

# Count the number of unique male and female applicants post-legislation
post_legislation_male_applicants = post_legislation[post_legislation['FemaleFlag'] == 0]['fid'].nunique()
post_legislation_female_applicants = post_legislation[post_legislation['FemaleFlag'] == 1]['fid'].nunique()

# Print the results
print(f"Pre-legislation: Male Applicants: {pre_legislation_male_applicants}, Female Applicants: {pre_legislation_female_applicants}")
print(f"Post-legislation: Male Applicants: {post_legislation_male_applicants}, Female Applicants: {post_legislation_female_applicants}")