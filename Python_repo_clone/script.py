import git
import os

def clone_repo_and_readme(repo_url):
    # Ask for the location to save the repository
    save_location = input("Enter the location to save the repository: !avoid whitespace!")

    # Clone the repository
    repo_folder_name = repo_url.split("/")[-1].split(".")[0]  # Extract repository name from URL
    repo_path = os.path.join(save_location, repo_folder_name)
    repo = git.Repo.clone_from(repo_url, repo_path)

    # Read the README file
    readme_path = os.path.join(repo_path, 'README.md')
    with open(readme_path, 'r') as readme_file:
        readme_content = readme_file.read()

    # Print the README content
    print(readme_content)
    print (readme_path)
    return repo

if __name__ == "__main__":
    repo_url = input("Enter the URL of the repository: !avoid whitespace!")
    clone_repo_and_readme(repo_url)
