import requests
import json

####
# inputs
####
username = 'py-list1'

# from https://github.com/user/settings/tokens
token = 'efc90070630b03a149b020bc23ef1b0429b60156'

repos_url = 'https://api.github.com/user/repos'

# create a re-usable session object with the user creds in-built
gh_session = requests.Session()
gh_session.auth = (username, token)

# get the list of repos belonging to me
repos = json.loads(gh_session.get(repos_url).text)
print(repos)
print(repos[0].keys())
fo =open("file_name.csv",'w')
# print the repo names
for repo in repos:
    print(repo['name'])
    fo.write(repo['name'))
    print(repo['full_name'])
    print(repo['watchers'])
    print(repo['forks'])
    print(repo['has_wiki'])
    print(repo['git_url'])
    print(repo['language'])
    print(repo['owner']['login'])
    print(repo['owner']['type'])
fo.close()
