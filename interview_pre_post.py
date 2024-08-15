import pandas as pd

data = pd.read_csv('Data.csv')

data['date_of_posting'] = pd.to_datetime(data['date_of_posting'], unit='s')
data['api_applications_created'] = pd.to_datetime(data['api_applications_created'], unit='s')

legislation_date = pd.to_datetime('2017-03-01')

pre_legislation = data[data['date_of_posting'] < legislation_date]
post_legislation = data[data['date_of_posting'] >= legislation_date]

pre_legislation_interviews = pre_legislation[pre_legislation['CalLetterFlag'] == 1]
post_legislation_interviews = post_legislation[post_legislation['CalLetterFlag'] == 1]

pre_interview_male_count = pre_legislation_interviews[pre_legislation_interviews['FemaleFlag'] == 0].shape[0]
pre_interview_female_count = pre_legislation_interviews[pre_legislation_interviews['FemaleFlag'] == 1].shape[0]

post_interview_male_count = post_legislation_interviews[post_legislation_interviews['FemaleFlag'] == 0].shape[0]
post_interview_female_count = post_legislation_interviews[post_legislation_interviews['FemaleFlag'] == 1].shape[0]

print(f"Pre-legislation: Male Invited for Interview: {pre_interview_male_count}, Female Invited for Interview: {pre_interview_female_count}")
print(f"Post-legislation: Male Invited for Interview: {post_interview_male_count}, Female Invited for Interview: {post_interview_female_count}")
