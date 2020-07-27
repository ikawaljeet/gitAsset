from github import Github
from src.gitRestApi import GitRestApi
from config.config import Config

class GitAssetManager:
    def __init__(self):
        self.config = Config()
        self.github = Github(self.config.get_auth_token())
        self.gitRestApi = GitRestApi()

    def get_repo_release_info(self, org, repo):
        git_releases_obj = self.github.get_repo('{}/{}'.format(org, repo)).get_releases()

        releases_info = {}
        for release_obj in git_releases_obj:
            releases_info[release_obj.title] = {}
            releases_info[release_obj.title]['id'] = release_obj.id

        return releases_info

    def get_repo_release_obj_by_title(self, org, repo, release_title):
        git_releases_obj = self.github.get_repo('{}/{}'.format(org, repo)).get_releases()

        for release_obj in git_releases_obj:
            if release_obj.title == release_title:
                return release_obj

        return None

    def get_repo_release_asset_info(self, org, repo, release_title):
        git_assets_obj = self.get_repo_release_obj_by_title(org, repo, release_title).get_assets()

        assets_info = {}
        for asset_obj in git_assets_obj:
            assets_info[asset_obj.name] = {}
            assets_info[asset_obj.name]['id'] = asset_obj.id

        return assets_info

    def get_repo_release_asset_obj_by_name(self, org, repo, release_title, asset_name):
        git_assets_obj = self.get_repo_release_obj_by_title(org, repo, release_title).get_assets()

        for asset_obj in git_assets_obj:
            if asset_obj.name == asset_name:
                return asset_obj

        return None

    def download_asset_by_id(self, org, repo, asset_id, download_location):
        ret = self.gitRestApi.download_asset(org, repo, asset_id, download_location)
        print("Asset Download Status: {}".format(ret))

    def upload_asset_by_id(self, org, repo, release_id, file_location, asset_name):
        ret = self.gitRestApi.upload_asset(org, repo, release_id, file_location, asset_name)
        print("Asset Upload Status: {}".format(ret))

    def test(self):
        org = self.config.get_org_name()
        repo = self.config.get_repo_name()

        releases_info = self.get_repo_release_info(org=org, repo=repo)
        print("releases info: {}".format(releases_info))

        assets_info = self.get_repo_release_asset_info(org=org, repo=repo, release_title='FirstRelease')
        print("assets_info: {}".format(assets_info))

        #Download and Upload Asset
        download_location = "/home/kawaljeet/Workspace/programmingPractice/pythonPrograms/assetFiles"
        upload_location = "/home/kawaljeet/Workspace/programmingPractice/pythonPrograms/assetFiles/build.zip"
        upload_asset_name = "releaseAsset1.zip"
        self.download_asset_by_id(org=org, repo=repo, asset_id=23256640, download_location=download_location)
        self.upload_asset_by_id(org=org, repo=repo, release_id=28902143, file_location=upload_location, asset_name=upload_asset_name)



if __name__ == '__main__':
    gitAssetManager = GitAssetManager()
    gitAssetManager.test()