from repo import GitHub
import pprint
import os

def get_stars_and_forks(url):
    gh = GitHub(url)
    metadata = gh.get_repo_metadata()
    pprint.pprint(metadata)

    stars = metadata.get('stargazers_count')
    forks = metadata.get('forks_count')

    print(f"Repo {url} is starred {stars} times and forked {forks} times.")

# get_stars_and_forks("https://github.com/huggingface/transformers")
# get_stars_and_forks("https://github.com/bmareddy/sapphire")

def test_save(url):
    gh = GitHub(url)
    metadata = gh.get_repo_metadata()
    directory = os.path.dirname(os.path.abspath(__file__))
    filename = url.replace('https:','').replace('/', '_')
    gh.save_metadata(metadata, f"{directory}\data\{filename}")

test_save("https://github.com/bmareddy/sapphire")