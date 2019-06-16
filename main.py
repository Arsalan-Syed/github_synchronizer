import requests


def _get_credentials():

    file = open("credentials.txt", "r")
    lines = file.read()
    file.close()
    return lines.split("\n")


def _run_query(append_url):
    """
	Run a REST (GitHub API V3) query
	Args:
	Returns:
		(str): Json
	"""

    username, token = _get_credentials()

    url = "http://api.github.com/" + append_url
    print(url)
    request = requests.get(url, auth=(username, token))

    if request.status_code == 200:
        return request.json()
    else:
        raise Exception(str(request.status_code) + "\n" + request.text)



def get_repos_for_user(user):
    repo_data = _run_query("users/%s/repos" % user)
    return [x["html_url"] for x in repo_data]


print(get_repos_for_user("Arsalan-Syed"))