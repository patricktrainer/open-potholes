import requests


class NolaData:
    """Interface for the data.nola.gov"""

    def __init__(self, dataset_id) -> None:
        self.url = f"https://data.nola.gov/api/id/{dataset_id}.json"
        self.payload = None

    def doGet(self):
        """Sends a GET request"""
        return requests.get(url=self.url, params=self.payload)

    def doFilter(self, clause: dict):
        """Specify limits and/or filters
        ex:
            {
                "$limit": 42,
                "$request_status": "pending",
            }
        """
        self.payload = clause
