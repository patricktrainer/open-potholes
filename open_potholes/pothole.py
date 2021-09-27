import requests


class NolaData:
    """Interface for the data.nola.gov api"""

    def __init__(self, dataset_id) -> None:
        self.url = f"https://data.nola.gov/api/id/{dataset_id}.json"
        self.payload = None

    def fetch(self, filter_clause: dict = None) -> requests.Response:
        """Sends a GET request"""
        if filter_clause:
            self.filter(filter_clause)

        return requests.get(url=self.url, params=self.payload)

    def filter(self, filter_clause: dict) -> None:
        """Specify limits and/or filters for the data
        :param filter_clause:
            {
                "$limit": 42,
                "$request_status": "pending",
            }
        """
        self.payload = filter_clause


if __name__ == "__main__":
    nola = NolaData("2jgv-pqrq")
    filt = {"request_reason": "Pothole"}
    pothole = nola.fetch(filter_clause=filt)
    pothole.json()
