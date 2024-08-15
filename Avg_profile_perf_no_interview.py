import pandas as pd

# Load the dataset
data = pd.read_csv('Data.csv')

# Convert Unix timestamps to datetime
data['date_of_posting'] = pd.to_datetime(data['date_of_posting'], unit='s')
data['api_applications_created'] = pd.to_datetime(data['api_applications_created'], unit='s')

# Calculate graduation year based on year of birth and course type
data['calculated_grad_year'] = data.apply(lambda row: row['yearBirth'] + 22 if row['course_type'] == 'graduation' else row['yearBirth'] + 24, axis=1)

# Filter candidates whose graduation year falls within the job's preferred range
eligible_candidates = data[(data['calculated_grad_year'] >= data['year_of_passing_from']) & (data['calculated_grad_year'] <= data['year_of_passing_to'])]

# Define the date when the legislation was passed
legislation_date = pd.to_datetime('2017-03-01')

# Separate the data into pre and post-legislation for eligible candidates
pre_legislation = eligible_candidates[eligible_candidates['date_of_posting'] < legislation_date]
post_legislation = eligible_candidates[eligible_candidates['date_of_posting'] >= legislation_date]

# Filter for those who weren't invited for an interview
pre_legislation_interviews = pre_legislation[pre_legislation['CalLetterFlag'] == 0]
post_legislation_interviews = post_legislation[post_legislation['CalLetterFlag'] == 0]

# Count the number of male and female applicants invited for an interview
pre_interview_male_count = pre_legislation_interviews[pre_legislation_interviews['FemaleFlag'] == 0].shape[0]
pre_interview_female_count = pre_legislation_interviews[pre_legislation_interviews['FemaleFlag'] == 1].shape[0]
post_interview_male_count = post_legislation_interviews[post_legislation_interviews['FemaleFlag'] == 0].shape[0]
post_interview_female_count = post_legislation_interviews[post_legislation_interviews['FemaleFlag'] == 1].shape[0]

# Calculate average profile_percentage score for applicants that didn't receive  interviews
pre_avg_profile_percentage = pre_legislation_interviews['profile_percentage'].mean()
post_avg_profile_percentage = post_legislation_interviews['profile_percentage'].mean()

# Print the results
print(f"Pre-legislation: Male Invited for Interview: {pre_interview_male_count}, Female Invited for Interview: {pre_interview_female_count}")
print(f"Post-legislation: Male Invited for Interview: {post_interview_male_count}, Female Invited for Interview: {post_interview_female_count}")
print(f"Pre-legislation: Average Profile Percentage (Interviews): {pre_avg_profile_percentage}%")
print(f"Post-legislation: Average Profile Percentage (Interviews): {post_avg_profile_percentage}%")