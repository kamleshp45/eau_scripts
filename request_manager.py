from requests import Session
# from config import github_api_url, private_asset_url, github_token


class RequestManager:
    
    def __init__(self, base_url, headers={}):

        self.base_url = base_url
        self.session = Session()
        for key, value in headers.items():
            self.session.headers[key] = value
    
    def request(self, url, method, **kwargs):
    
        response = getattr(self.session, method)(url=f"{self.base_url}{url}", **kwargs)
        response.raise_for_status()
        return response


# class Github(RequestManager):

#     def __init__(self):

#         super().__init__()
#         self.base_url = github_api_url
#         self.session.headers["Authorization"] = f"token {github_token}"

# class Privateasset(RequestManager):

#     def __init__(self):

#         super().__init__()
#         self.base_url = private_asset_url

