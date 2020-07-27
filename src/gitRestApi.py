import requests
import re
from config.config import Config

class GitRestApi:
    def __init__(self):
        self.config = Config()

    def download_asset(self, org, repo, asset_id, file_directory):
        # Download Asset
        try:
            url = "https://api.github.com/repos/{}/{}/releases/assets/{}".format(org, repo, asset_id)
            headers = {
                'Authorization': 'token {}'.format(self.config.get_auth_token()),
                'Accept': 'application/octet-stream'
            }
            response = requests.request("GET", url, headers=headers)
            print("Downloading Asset Successful")
        except Exception as e:
            print("Error in downloading asset: {}".format(e))
            return False

        # Save File
        try:
            cd = response.headers.get('content-disposition')
            file_name = re.findall("filename=(.+)", cd)[0]
            file_location = file_directory + '/' + file_name
            open(file_location, 'wb').write(response.content)
            print("Asset Saved Successfully At: {}".format(file_location))
        except Exception as e:
            print("Error in saving file: {}".format(e))
            return False

        return True  # success

    def upload_asset(self, org, repo, release_id, file_location, asset_name):
        #Upload file
        try:
            url = "https://uploads.github.com/repos/{}/{}/releases/{}/assets".format(org, repo, release_id)
            params = {"name": asset_name}
            headers = {
                'Authorization': 'token {}'.format(self.config.get_auth_token()),
                'Content-Type': 'application/zip'
            }
            files = {'file': open(file_location, 'rb')}
            response = requests.request("POST", url, headers=headers, params=params, files=files)
            print("Uploading Asset Successful")
        except Exception as e:
            print("Uploading Asset Failed: {}".format(e))
            return False

        return True


if __name__ == '__main__':
    gitRestApi = GitRestApi()
    gitRestApi.download_asset("skywalkerInc", "SharpenTheAxe", 23204106, "/home/kawaljeet/Workspace/programmingPractice/pythonPrograms/assetFiles")
    gitRestApi.upload_asset("skywalkerInc", "SharpenTheAxe", 28902143, "/home/kawaljeet/Workspace/programmingPractice/pythonPrograms/assetFiles/pledgeBanner.zip", "new_asset.zip")
    pass