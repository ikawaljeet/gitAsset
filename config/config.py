class Config:

    def __init__(self):
        # Access Configuration
        self.organisation_name = 'skywalkerInc'
        self.repository_name = 'SharpenTheAxe'
        self.auth_token = '7ce7d4018d070c844e1b38b86e8435a8f54621ea'

        # Download Configuration
        self.is_download = True
        self.is_download_all = True #If True, it will download all asset associated with release else it will take only asset names listed in release_asset_name_list
        self.release_tag_name_to_download = 'v0.1'
        self.release_asset_download_directory = '/home/kawaljeet/Workspace/programmingPractice/pythonPrograms/assetFiles'
        self.release_asset_name_list = [] # List of asset name when is_download_all is False

        # Upload Configuration
        self.is_upload = True
        self.release_tag_name_to_upload = 'v0.1'
        self.release_upload_file_info = [
                                        {
                                            "asset_name": "releaseAsset3.zip",
                                            "asset_location": "/home/kawaljeet/Workspace/programmingPractice/pythonPrograms/assetFiles/build.zip"
                                        }
                                     ]

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