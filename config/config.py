import json

class Config:

    def __init__(self):
        with open('config/jsonConfig.json', 'r') as f:
            self.jsonConfig = json.load(f)
        print("jsonConfig: {}".format(self.jsonConfig))

        # Access Configuration
        self.organisation_name = self.jsonConfig['organisation_name']
        self.repository_name = self.jsonConfig['repository_name']
        self.auth_token = self.jsonConfig['auth_token']

        # Download Configuration
        self.is_download = self.jsonConfig['is_download']
        self.is_download_latest = self.jsonConfig['is_download_latest']
        self.is_download_all = self.jsonConfig['is_download_all']
        self.release_tag_name_to_download = self.jsonConfig['release_tag_name_to_download']
        self.release_asset_download_directory = self.jsonConfig['release_asset_download_directory']
        self.release_asset_name_list = self.jsonConfig['release_asset_name_list']

        # Upload Configuration
        self.is_upload = self.jsonConfig['is_upload']
        self.release_tag_name_to_upload = self.jsonConfig['release_tag_name_to_upload']
        self.release_upload_file_info = self.jsonConfig['release_upload_file_info']

    def get_org_name(self):
        return self.organisation_name

    def get_repo_name(self):
        return self.repository_name

    def get_auth_token(self):
        return self.auth_token

if __name__ == '__main__':
    # Configuration Sample
    config = Config()
    # Access Configuration
    config.organisation_name = 'skywalkerInc'
    config.repository_name = 'SharpenTheAxe'
    config.auth_token = '7ce7d4018d070c844e1b38b86e8435a8f54621ea'

    # Download Configuration
    config.is_download = False
    config.is_download_all = True  # If True, it will download all asset associated with release else it will take only asset names listed in release_asset_name_list
    config.release_tag_name_to_download = 'v0.1'
    config.release_asset_download_directory = '/home/kawaljeet/Workspace/programmingPractice/pythonPrograms/assetFiles'
    config.release_asset_name_list = []  # List of asset name when is_download_all is False

    # Upload Configuration
    config.is_upload = False
    config.release_tag_name_to_upload = 'v0.1'
    config.release_upload_file_info = [
        {
            "asset_name": "releaseAsset1.zip",
            "asset_location": "/home/kawaljeet/Workspace/programmingPractice/pythonPrograms/assetFiles/build.zip"
        }
    ]