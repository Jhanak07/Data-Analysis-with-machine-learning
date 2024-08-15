import pandas as pd

data = pd.read_csv('Data.csv')

data['api_applications_created'] = pd.to_datetime(data['api_applications_created'], unit='s')

data['age_at_application'] = data['api_applications_created'].dt.year - data['yearBirth']

legislation_date = pd.to_datetime('2017-03-01')

recruiter_applications = data[data['applier_type'] == 'r']

pre_legislation = recruiter_applications[recruiter_applications['api_applications_created'] < legislation_date]
post_legislation = recruiter_applications[recruiter_applications['api_applications_created'] >= legislation_date]

def count_applications_by_age_and_gender(dataset):
    age_gender_counts = {(age, gender): dataset[(dataset['age_at_application'] == age) & (dataset['FemaleFlag'] == gender)].shape[0] 
                         for age in range(22, 31) for gender in [0, 1]}
    return age_gender_counts

pre_legislation_counts = count_applications_by_age_and_gender(pre_legislation)
post_legislation_counts = count_applications_by_age_and_gender(post_legislation)

print("Pre-legislation applications submitted by recruiters:")
for key, count in pre_legislation_counts.items():
    age, gender = key
    gender_str = "Male" if gender == 0 else "Female"
    print(f"Age {age}, {gender_str}: {count}")

print("\nPost-legislation applications submitted by recruiters:")
for key, count in post_legislation_counts.items():
    age, gender = key
    gender_str = "Male" if gender == 0 else "Female"
    print(f"Age {age}, {gender_str}: {count}")
