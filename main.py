from utils import *
import pandas as pd

data = pd.read_csv(input_file, header=0, names=['site', 'env', 'version'])
statuses= []

# Added check to verify whether the output file is open or not
try:
    file = open(output_file, 'a')
except PermissionError as e:
    print('Your output file is already being used. Please close it and then rerun the script.')
    exit()


for site, env, version in zip(data['site'].values, data['env'].values, data['version'].values):
    try:
        status = is_single_file_change(site, env, version)
        print(f'EDNAU PR of {site} for {env} env with version {version} found. Has single file change: {status}')
    except Exception as e:
        print(e)
        status = 'Error'
    statuses.append(status)

output = dict(site=data['site'].values.tolist(), env=data['env'].values.tolist(), version=data['version'].values.tolist(), status=statuses)
# print(output)
df = pd.DataFrame(output)
try:
    df.to_csv(output_file, index=False)
except PermissionError as e:
    print('Your output file is open in your system. Please close it to continue')
