import pandas as pd

data = pd.read_csv('Data.csv')

data['date_of_posting'] = pd.to_datetime(data['date_of_posting'], unit='s')
data['api_applications_created'] = pd.to_datetime(data['api_applications_created'], unit='s')

data['calculated_grad_year'] = data.apply(lambda row: row['yearBirth'] + 22 if row['course_type'] == 'graduation' else row['yearBirth'] + 24, axis=1)

eligible_candidates = data[(data['calculated_grad_year'] >= data['year_of_passing_from']) & (data['calculated_grad_year'] <= data['year_of_passing_to'])]

legislation_date = pd.to_datetime('2017-03-01')

pre_legislation_eligible = eligible_candidates[eligible_candidates['api_applications_created'] < legislation_date]

pre_legislation_eligible_female_interviews = pre_legislation_eligible[(pre_legislation_eligible['FemaleFlag'] == 1) & (pre_legislation_eligible['CalLetterFlag'] == 1)]

pre_legislation_eligible_female_interviews['age_at_application'] = pre_legislation_eligible_female_interviews['api_applications_created'].dt.year - pre_legislation_eligible_female_interviews['yearBirth']

age_counts_pre_legislation = {age: 0 for age in range(22, 31)}

for age in age_counts_pre_legislation.keys():
    age_counts_pre_legislation[age] = pre_legislation_eligible_female_interviews[pre_legislation_eligible_female_interviews['age_at_application'] == age].shape[0]

for age, count in age_counts_pre_legislation.items():
    print(f"Pre-legislation: Number of eligible female getting interview at age {age}: {count}")
