from config import github_api_url, github_token, private_asset_url
from request_manager import RequestManager
import json

github_api = RequestManager(github_api_url, headers={
    'Authorization': f'token {github_token}'
})
privateasset = RequestManager(private_asset_url)


def is_single_file_change(site, env, version):
    
    site = f'{site}_profile'
    
    # find the pr number where target is env and source branch is EDNAU branch
    pr_number = get_pr_number(site, env, version)

    if pr_number == -1:
        raise Exception(f'No open PR present for {site} for {env} with version {version}')
    
    # then send request for this to check how many files are changed and return the names of file
    changed_files_name = get_changed_files_for_pr(site, pr_number)
    
    # if there is single file which is .edison file then return true else false
    return len(changed_files_name) == 1 and changed_files_name[0] == edison_file_name

def get_pr_number(site, env, version, state='open'):

    base_branch = '1.x' if env == 'prod' else env
    head = f'{organization}:EDNAU-{env}-{version}'

    params = {'base': base_branch, 'head': head, 'state': state}
    response = github_api.request(f'/repos/{organization}/{site}/pulls', 'get', params=params)
    pr = json.loads(response.text)
    if not pr:
        return -1
    return pr[0]['number']
    

def get_changed_files_for_pr(site, pr_number):

    response = github_api.request(f'/repos/{organization}/{site}/pulls/{pr_number}/files', 'get')
    response = json.loads(response.text)
    return [file['filename'] for file in response]

