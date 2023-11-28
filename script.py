import requests, subprocess

def get_latest_commit(owner, repo, token):
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    headers = {
    "Authorization": "Bearer {}".format(token)
    }
    # Using try except block for error handling
    try:
        response = requests.get(url, headers=headers)
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
    
def store_commit(commit):
    with open(".commit.txt", "w") as file:
        file.write(commit)
        return commit

def retrieve_commit():
    try:
        with open(".commit.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        print("File not found")
        return

if __name__ == "__main__":
    token = ""
    owner = "Viole01"
    repo = "CICD-Vired"

    latest_commit = get_latest_commit(owner, repo, token)
    stored_commit = retrieve_commit()

    try:
        if latest_commit != stored_commit:
            subprocess.run(["sh", "bash.sh"])
            store_commit(latest_commit)
    except FileNotFoundError:
        print("File not found. Creating a new file")
        store_commit(latest_commit)

    print(latest_commit)