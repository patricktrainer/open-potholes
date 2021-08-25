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


if __name__ == "__main__":
    service_calls = "2jgv-pqrq"
    where = {"request_reason": "Pothole"}

    data = NolaData(service_calls)
    data.doFilter(where)

    response = data.doGet()
