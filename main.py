from open_potholes import client, handler


json_handler = handler.JSONHandler()
pothole_data = json_handler.load_json(filename="./potholes.json")
github_client = client.GithubClient(
    token='')
github_client.create_gist(description="potholes",
                          public=False, files=pothole_data)
