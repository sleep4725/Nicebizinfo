import requests

class GetSessionObj:

    @classmethod
    def sessObjGet(cls):
        sess = requests.Session()
        return sess