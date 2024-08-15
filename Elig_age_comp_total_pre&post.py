import pandas as pd

data = pd.read_csv('Data.csv')

data['date_of_posting'] = pd.to_datetime(data['date_of_posting'], unit='s')
data['api_applications_created'] = pd.to_datetime(data['api_applications_created'], unit='s')

data['calculated_grad_year'] = data.apply(lambda row: row['yearBirth'] + 22 if row['course_type'] == 'graduation' else row['yearBirth'] + 24, axis=1)

eligible_candidates = data[(data['calculated_grad_year'] >= data['year_of_passing_from']) & (data['calculated_grad_year'] <= data['year_of_passing_to'])]

eligible_female_candidates = eligible_candidates[eligible_candidates['FemaleFlag'] == 1]

eligible_female_candidates['age_at_application'] = eligible_female_candidates['api_applications_created'].dt.year - eligible_female_candidates['yearBirth']

legislation_date = pd.to_datetime('2017-03-01')

pre_legislation_female = eligible_female_candidates[eligible_female_candidates['api_applications_created'] < legislation_date]
post_legislation_female = eligible_female_candidates[eligible_female_candidates['api_applications_created'] >= legislation_date]

age_counts_pre = {age: 0 for age in range(22, 31)}
age_counts_post = {age: 0 for age in range(22, 31)}

for age in age_counts_pre.keys():
    age_counts_pre[age] = pre_legislation_female[pre_legislation_female['age_at_application'] == age].shape[0]

for age in age_counts_post.keys():
    age_counts_post[age] = post_legislation_female[post_legislation_female['age_at_application'] == age].shape[0]

print("Pre-legislation applications by age:")
for age, count in age_counts_pre.items():
    print(f"Age {age}: {count}")

print("\nPost-legislation applications by age:")
for age, count in age_counts_post.items():
    print(f"Age {age}: {count}")
