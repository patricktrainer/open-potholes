import json
import requests
from .handler import JSONHandler


class BaseClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, params=None):
        # TODO: change this to not implemented error
        response = requests.get(f"{self.base_url}/{endpoint}", params=params)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint, data=None, headers=None):
        
        ...


class GithubClient(BaseClient):
    def __init__(self, base_url="https://api.github.com", token=None):
        super().__init__(base_url)
        self.token = token  # Github requires authentication for gist creation
        self.handler = JSONHandler()

    def create_gist(self, description, public, files):
        # First, convert the files to the geojson using the JSONHandler
        # Assume the to_geojson method takes a file object and returns geojson format
        geojson_files = self.handler.to_geojson(files)

        endpoint = self.base_url + '/gists'
        headers = {'Authorization': f'token {self.token}',
                   'Accept': 'application/vnd.github+json'}

        content = {"description": "potholes",
                   "public": False,
                   "files": {"potholes.geojson": {"content": geojson_files}}
                   }

        response = requests.post(endpoint, data=json.dumps(
            content, indent=2), headers=headers)

        if not response.ok:
            raise Exception('failed to upload to gists')

        print(response.status_code)
