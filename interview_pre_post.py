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

# Filter for those who were invited for an interview
pre_legislation_interviews = pre_legislation[pre_legislation['CalLetterFlag'] == 1]
post_legislation_interviews = post_legislation[post_legislation['CalLetterFlag'] == 1]

# Count the number of male and female applicants invited for an interview pre-legislation
pre_interview_male_count = pre_legislation_interviews[pre_legislation_interviews['FemaleFlag'] == 0].shape[0]
pre_interview_female_count = pre_legislation_interviews[pre_legislation_interviews['FemaleFlag'] == 1].shape[0]

# Count the number of male and female applicants invited for an interview post-legislation
post_interview_male_count = post_legislation_interviews[post_legislation_interviews['FemaleFlag'] == 0].shape[0]
post_interview_female_count = post_legislation_interviews[post_legislation_interviews['FemaleFlag'] == 1].shape[0]

# Print the results
print(f"Pre-legislation: Male Invited for Interview: {pre_interview_male_count}, Female Invited for Interview: {pre_interview_female_count}")
print(f"Post-legislation: Male Invited for Interview: {post_interview_male_count}, Female Invited for Interview: {post_interview_female_count}")