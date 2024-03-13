from enum import Enum
import requests
from requests.exceptions import InvalidURL, Timeout
from requests import RequestException
import os, json
import logging

class RepoPlatform(Enum):
    GITHUB = "https://api.github.com/repos"

class Repo:
    """
    Parent class to define common data and methods
    across any type of repo platform
    """
    def __init__(self, platform:RepoPlatform):
        """
        Initializes the Repo object
        """
        self.platform = platform

    def get_repo_metadata(self):
        """
        Implement method for each type of repo
        to get metadata in json format
        """
        pass

    def save_metadata(self, metadata, filename):
        """
        If metadata must be saved to disk
        implement appropriate logic. 
        Base implementation writes to ./filename
        If ./filename already exists, renames to /filename_previous
        """
        logging.info("Fetching metadata")
        if metadata:
            logging.info("Attempting to save")
            try:
                if os.path.exists(filename):
                    os.rename(filename, filename+"_previous")
                with open(filename, 'w') as file:
                    json.dump(metadata, file)
            except Exception as e:
                print(f"Unable to save. Exception: {e}")

class GitHub(Repo):
    """
    GitHub functionality
    """
    def __init__(self, url: str):
        super().__init__(RepoPlatform.GITHUB)

        self.url = url

    def _validate_url(self):
        if self.url.endswith('/'):
            return self.url[:-1]
        else:
            return self.url

    def get_api_url(self):
        validated_url = self._validate_url()
        url_split = validated_url.split('/')
        api_url = f"{self.platform.value}/{url_split[-2]}/{url_split[-1]}"
        return api_url


    def get_repo_metadata(self):
        """
        Get GitHub repo metadata. Returns json response
        """
        api_url = self.get_api_url()
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                response.raise_for_status()
        except InvalidURL as e:
            print(f"{api_url} is invalid. Failed to get a reponse. Status code: {response.status_code}")
        except Timeout as e:
            print(f"Request timed out. Attempted to get from {api_url}. Status code: {response.status_code}")
        except RequestException as e:
            print(f"Request failed. Attempted to get from {api_url}. Status code: {response.status_code}")
