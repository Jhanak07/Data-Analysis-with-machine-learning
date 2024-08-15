import pandas as pd

# Load the dataset
data = pd.read_csv('Data.csv')

# Convert Unix timestamps to datetime
data['api_applications_created'] = pd.to_datetime(data['api_applications_created'], unit='s')

# Calculate age at the time of application for all candidates
data['age_at_application'] = data['api_applications_created'].dt.year - data['yearBirth']

# Define the date when the legislation was passed
legislation_date = pd.to_datetime('2017-03-01')

# Filter applications submitted by recruiters
recruiter_applications = data[data['applier_type'] == 'r']

# Segment data by legislation period
pre_legislation = recruiter_applications[recruiter_applications['api_applications_created'] < legislation_date]
post_legislation = recruiter_applications[recruiter_applications['api_applications_created'] >= legislation_date]

# Function to count applications by age and gender for a given dataset
def count_applications_by_age_and_gender(dataset):
    age_gender_counts = {(age, gender): dataset[(dataset['age_at_application'] == age) & (dataset['FemaleFlag'] == gender)].shape[0] 
                         for age in range(22, 31) for gender in [0, 1]}
    return age_gender_counts

# Count applications pre and post legislation
pre_legislation_counts = count_applications_by_age_and_gender(pre_legislation)
post_legislation_counts = count_applications_by_age_and_gender(post_legislation)

# Print the results
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
