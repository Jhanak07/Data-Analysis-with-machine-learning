import pandas as pd

# Load the dataset
data = pd.read_csv('Data.csv')

# Convert Unix timestamps to datetime for 'date_of_posting' and 'api_applications_created'
data['date_of_posting'] = pd.to_datetime(data['date_of_posting'], unit='s')
data['api_applications_created'] = pd.to_datetime(data['api_applications_created'], unit='s')

# Define the time range for the analysis
start_date = pd.to_datetime('2015-09-01')
end_date = pd.to_datetime('2018-11-30')

# Filter the data to include only applications within the specified time range
data = data[(data['date_of_posting'] >= start_date) & (data['date_of_posting'] <= end_date)]

# Define the date when the legislation was passed
legislation_date = pd.to_datetime('2017-03-09')

# Separate the data into pre and post-legislation
pre_legislation = data[data['date_of_posting'] < legislation_date]
post_legislation = data[data['date_of_posting'] >= legislation_date]

# Count the number of male and female applicants pre-legislation
pre_legislation_male_count = pre_legislation[pre_legislation['FemaleFlag'] == 0].shape[0]
pre_legislation_female_count = pre_legislation[pre_legislation['FemaleFlag'] == 1].shape[0]

# Count the number of male and female applicants post-legislation
post_legislation_male_count = post_legislation[post_legislation['FemaleFlag'] == 0].shape[0]
post_legislation_female_count = post_legislation[post_legislation['FemaleFlag'] == 1].shape[0]

# Print the results
print(f"Pre-legislation (Sep 1, 2015 - Mar 8, 2017): Male Applicants: {pre_legislation_male_count}, Female Applicants: {pre_legislation_female_count}")
print(f"Post-legislation (Mar 9, 2017 - Nov 30, 2018): Male Applicants: {post_legislation_male_count}, Female Applicants: {post_legislation_female_count}")