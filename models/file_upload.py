from filestack import Client


class UploadFile:

    def __init__(self, file_path, api_token='A2QKY8Cs2S2KzhSN1akrWz'):
        self.file_path = file_path
        self.api_token = api_token

    def upload(self):
        client = Client(self.api_token)
        file_link = client.upload(filepath=self.file_path)
        return file_link.url
