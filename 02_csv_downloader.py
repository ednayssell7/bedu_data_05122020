import requests

base_url = 'https://galileoguzman.com/data/best_sellers.csv'

response = requests.get(base_url)
response.raise_for_status()

response_content = response.content
filename = 'datasets/best_sellers.csv'

with open(filename, 'wb') as csv_file:
    csv_file.write(response_content)

print('file downloaded =)')