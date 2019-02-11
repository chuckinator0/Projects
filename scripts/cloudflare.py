import json
import requests
import re

def get_all_stars(url):
    r = requests.get(url)

    def get_stars_on_page(r):
        data = json.loads(r.content)
        count = 0 
        for repo in data:
            count += repo["stargazers_count"]
        return count

    number_pages = int( re.findall(r'\?page=(\d+)', r.headers['Link'])[-1] )
    url_array = [url + f"?page={i}" for i in range(1, number_pages + 1)]

    total = 0
    for url in url_array:
        total += get_stars_on_page(r)
    return total

print(get_all_stars('https://api.github.com/orgs/cloudflare/repos'))

""" if __name__ == "__main__":

    # r = requests.get('https://api.github.com/organizations/314135/repos')
    # regex = re.compile('https://api.github.com/organizations/314135/repos?page=(\d+)')
    print( re.findall(r'https://api.github.com/organizations/314135/repos\?page=(\d+)','<https://api.github.com/organizations/314135/repos?page=2>; rel="next", <https://api.github.com/organizations/314135/repos?page=8>; rel="last"')[-1] ) """