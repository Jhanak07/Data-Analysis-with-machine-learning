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

# Further filter for female candidates
eligible_female_candidates = eligible_candidates[eligible_candidates['FemaleFlag'] == 1]

# Calculate age at the time of application
eligible_female_candidates['age_at_application'] = eligible_female_candidates['api_applications_created'].dt.year - eligible_female_candidates['yearBirth']

# Define the date when the legislation was passed
legislation_date = pd.to_datetime('2017-03-01')

# Split into pre and post-legislation
pre_legislation_female = eligible_female_candidates[eligible_female_candidates['api_applications_created'] < legislation_date]
post_legislation_female = eligible_female_candidates[eligible_female_candidates['api_applications_created'] >= legislation_date]

# Initialize dictionaries to hold the counts for each age, for pre and post-legislation
age_counts_pre = {age: 0 for age in range(22, 31)}
age_counts_post = {age: 0 for age in range(22, 31)}

# Count applications for each age category, pre-legislation
for age in age_counts_pre.keys():
    age_counts_pre[age] = pre_legislation_female[pre_legislation_female['age_at_application'] == age].shape[0]

# Count applications for each age category, post-legislation
for age in age_counts_post.keys():
    age_counts_post[age] = post_legislation_female[post_legislation_female['age_at_application'] == age].shape[0]

# Print the results
print("Pre-legislation applications by age:")
for age, count in age_counts_pre.items():
    print(f"Age {age}: {count}")

print("\nPost-legislation applications by age:")
for age, count in age_counts_post.items():
    print(f"Age {age}: {count}")
