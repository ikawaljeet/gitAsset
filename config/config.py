class Config:

    def __init__(self):
        self.organisation_name = 'skywalkerInc'
        self.repository_name = 'SharpenTheAxe'
        self.auth_token = '7eb218d87136cd5cc0252bb0328803f406161942'

    def get_org_name(self):
        return self.organisation_name

    def get_repo_name(self):
        return self.repository_name

    def get_auth_token(self):
        return self.auth_token
