import json
from git.repo import Repo


class JSONHandler:
    def load_json(self, filename):
        with open(filename) as f:
            data = json.load(f)
        return data

    def save_json(self, data, filename):
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)

    def to_geojson(self, json_data):
        geojson = {"type": "FeatureCollection", "features": []}

        for item in json_data:
            feature = self.geojson_feature(item)
            geojson["features"].append(feature)
        return geojson

    def geojson_feature(self, item):
        feature = {
            "type": "Feature",
            "properties": {
                "service_request": item["service_request"],
                "request_type": item["request_type"],
                "request_reason": item["request_reason"],
                "date_created": item["date_created"],
                "date_modified": item["date_modified"],
                "request_status": item["request_status"],
                "final_address": item["final_address"],
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    # these are strings, but we need floats
                    float(item["latitude"]),
                    float(item["longitude"]),
                ],
            },
        }

        return feature


class GitHandler:
    def parse_revisions(self, git_dir, filepath, rev="main"):
        """
        Iterate through the versions of a file in a git repo
        """
        repo = Repo(git_dir)
        commits = reversed(list(repo.iter_commits(rev, paths=filepath)))

        for commit in commits:
            blob = [b for b in commit.tree.blobs if b.name == filepath][0]
            yield commit.committed_datetime, commit.hexsha, blob.data_stream.read()


class MapHandler:
    pass
