import requests

token = ""
owner = "Viole01"
repo = "CICD-Vired"
fp = "commit.txt"


def get_latest_commit(owner, repo):
    url = "https://api.github.com/repos/{}/{}/commits"
    headers = {
    "Authorization": "Bearer {}".format(token)
    }
    # Using try except block for error handling
    try:
        response = requests.get(url.format(owner, repo), headers=headers)
        response.raise_for_status()

        commits = response.json()

        if commits:
            latest_commit_sha = commits[0]["sha"]
            return latest_commit_sha
        else:
            print("No New Commits Found")
            return

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return
    
latest_commit = get_latest_commit(owner, repo)

# Using with statement to open the file in write mode
with open(fp, "w") as file:
    file.write(latest_commit)

print(latest_commit)