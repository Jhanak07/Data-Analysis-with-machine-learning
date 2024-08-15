import pandas as pd

data = pd.read_csv('Data.csv')

data['date_of_posting'] = pd.to_datetime(data['date_of_posting'], unit='s')
data['api_applications_created'] = pd.to_datetime(data['api_applications_created'], unit='s')

data['calculated_grad_year'] = data.apply(
    lambda row: row['yearBirth'] + 22 if row['course_type'] == 'graduation' else row['yearBirth'] + 24, 
    axis=1
)

eligible_female_interviews = data[
    (data['FemaleFlag'] == 1) & 
    (data['CalLetterFlag'] == 1) & 
    (data['calculated_grad_year'] >= data['year_of_passing_from']) & 
    (data['calculated_grad_year'] <= data['year_of_passing_to'])
]
legislation_date = pd.to_datetime('2017-03-01')

company_size_mapping = {2: "51-200", 3: "201-1000", 4: "1001-10000", 5: ">10000"}
eligible_female_interviews['company_size'] = eligible_female_interviews['no_of_employees'].map(company_size_mapping)

company_sizes = eligible_female_interviews['company_size'].dropna().unique()
results = []

for size in company_sizes:
    size_data = eligible_female_interviews[eligible_female_interviews['company_size'] == size]
    pre_legislation = size_data[size_data['api_applications_created'] < legislation_date]
    post_legislation = size_data[size_data['api_applications_created'] >= legislation_date]
    
    pre_count = pre_legislation.shape[0]
    post_count = post_legislation.shape[0]
    
    results.append((size, pre_count, post_count))

for size, pre_count, post_count in sorted(results, key=lambda x: x[0]):
    print(f"Company Size {size}: Pre-legislation Interviews: {pre_count}, Post-legislation Interviews: {post_count}")
