from github import Github
from src.gitRestApi import GitRestApi
from config.config import Config
import os

class GitSimpleAssetManager:
    def __init__(self):
        self.config = Config()
        self.github = Github(self.config.get_auth_token())
        self.gitRestApi = GitRestApi()

    def get_repo_release_obj_by_tag_name(self, org, repo, tag_name):
        if self.config.is_download_latest == True:
            return self.github.get_repo('{}/{}'.format(org, repo)).get_latest_release()

        git_releases_obj = self.github.get_repo('{}/{}'.format(org, repo)).get_releases()

        for release_obj in git_releases_obj:
            if release_obj.tag_name == tag_name:
                return release_obj

        return None

    def get_repo_asset_obj_by_release_tag_name(self, org, repo, tag_name, asset_name):
        git_assets_obj = self.get_repo_release_obj_by_tag_name(org, repo, tag_name).get_assets()

        for asset_obj in git_assets_obj:
            if asset_obj.name == asset_name:
                return asset_obj

        return None


    def download_asset_by_release_tag_and_asset_name(self, org, repo, tag_name, asset_name, download_location):
        release_asset_obj = self.get_repo_asset_obj_by_release_tag_name(org, repo, tag_name, asset_name)

        print("Download Asset Named: {}".format(release_asset_obj.name))
        ret = self.gitRestApi.download_asset(org, repo, release_asset_obj.id, download_location)
        print("Asset {} Download Status: {}".format(release_asset_obj.name, ret))

    def download_all_asset_by_release_tag_name(self, org, repo, tag_name, download_location):
        git_release_obj = self.get_repo_release_obj_by_tag_name(org, repo, tag_name)
        git_assets_obj = git_release_obj.get_assets()

        print("Downloading All {} Assets For Release Tag: {}, Release Name: {}".format(len(list(git_assets_obj)), git_release_obj.tag_name, git_release_obj.title))
        for index, asset_obj in enumerate(git_assets_obj):
            ret = self.gitRestApi.download_asset(org, repo, asset_obj.id, download_location)
            print("{}/{} Asset {} Download Status: {}".format(index+1, len(list(git_assets_obj)), asset_obj.name, ret))

    def upload_asset_by_tag_name(self, org, repo, tag_name, file_location, asset_name):
        git_release_obj = self.get_repo_release_obj_by_tag_name(org, repo, tag_name)

        print("Uploading Asset From Location: {} With Name: {}".format(file_location, asset_name))
        ret = self.gitRestApi.upload_asset(org, repo, git_release_obj.id, file_location, asset_name)
        print("Asset {} Upload Status: {}".format(asset_name, ret))


    def download_release_asset_from_configuration(self):
        org = self.config.get_org_name()
        repo = self.config.get_repo_name()

        if (self.config.is_download == False):
            # Download is InActive
            print("Nothing for Download")
        else:
            # Download is Active
            if (self.config.is_download_all == False):
                # Download Only Listed Assets
                asset_list = self.config.release_asset_name_list
                for asset_name in asset_list:
                    # Download Each Asset
                    self.download_asset_by_release_tag_and_asset_name(self, org, repo, self.config.release_tag_name_to_download, asset_name,
                                                                 self.config.release_asset_download_directory)
            else:
                # Download All Assets
                self.download_all_asset_by_release_tag_name(org,repo,self.config.release_tag_name_to_download, self.config.release_asset_download_directory)


    def upload_release_asset_from_configuration(self):
        org = self.config.get_org_name()
        repo = self.config.get_repo_name()

        if (self.config.is_upload == False):
            # Upload is not Active
            print("Nothing for Upload")
        else:
            # Upload is Active
            for asset_info in self.config.release_upload_file_info:
                # Uploading each asset present in asset info
                asset_name = asset_info['asset_name']
                asset_location = asset_info['asset_location']
                self.upload_asset_by_tag_name(org, repo, self.config.release_tag_name_to_upload, asset_location, asset_name)

    def clean_asset_download_location(self):
        filelist = [f for f in os.listdir(self.config.release_asset_download_directory)]
        print("Removing all files from directory: {}".format(self.config.release_asset_download_directory))
        for f in filelist:
            os.remove(os.path.join(self.config.release_asset_download_directory, f))
            print("Removed File {}".format(f))

    def main(self):
        self.clean_asset_download_location()
        self.download_release_asset_from_configuration()
        self.upload_release_asset_from_configuration()


if __name__ == '__main__':
    gitAssetManager = GitAssetManager()
    gitAssetManager.main()
