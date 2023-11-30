import subprocess
import getpass

def create_github_repo(repo_name, description, private=False):
    username = input("ID GH: ")
    password = getpass.getpass("MDP GH: ")
    curl_command = f'curl -u {username}:{password} -d \'{{"name":"{repo_name}","description":"{description}","private":{str(private).lower()}}}\' https://api.github.com/user/repos'
    process = subprocess.Popen(curl_command, shell=True)
    process.wait()
    if process.returncode == 0:
        print(f"Depot créer {repo_name} ")
    else:
        print(f"Erreur: {process.returncode}")

if __name__ == "__main__":
    repo_name = input("Nom GH: ")
    description = input("Desc GH: ")
    private = input("Privé y/n: ").lower() == 'y'

    create_github_repo(repo_name, description, private)
