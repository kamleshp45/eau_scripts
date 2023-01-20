base_url = 'https://api.github.com'
organization = 'pfizer'
edison_file_name = '.edison_automated_upgrade'
input_file = 'subscription.csv'
output_file = 'output.csv'

try:
    file = open('github_token.txt', 'r')
except Exception as e:
    print('Please create a "github_token.txt" file at root level and add your github token there.')
    exit()

github_token = file.read().strip()
