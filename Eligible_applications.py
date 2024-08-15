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
pre_legislation_eligible = eligible_candidates[eligible_candidates['date_of_posting'] < legislation_date]
post_legislation_eligible = eligible_candidates[eligible_candidates['date_of_posting'] >= legislation_date]

# Count the number of male and female applications meeting graduation criteria pre-legislation
pre_legislation_eligible_male_count = pre_legislation_eligible[pre_legislation_eligible['FemaleFlag'] == 0].shape[0]
pre_legislation_eligible_female_count = pre_legislation_eligible[pre_legislation_eligible['FemaleFlag'] == 1].shape[0]

# Count the number of male and female applications meeting graduation criteria post-legislation
post_legislation_eligible_male_count = post_legislation_eligible[post_legislation_eligible['FemaleFlag'] == 0].shape[0]
post_legislation_eligible_female_count = post_legislation_eligible[post_legislation_eligible['FemaleFlag'] == 1].shape[0]

# Print the results
print(f"Pre-legislation: Eligible Male Applications: {pre_legislation_eligible_male_count}, Eligible Female Applications: {pre_legislation_eligible_female_count}")
print(f"Post-legislation: Eligible Male Applications: {post_legislation_eligible_male_count}, Eligible Female Applications: {post_legislation_eligible_female_count}")




