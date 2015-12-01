"""
Storage module
"""
import shelve

class LocalStore:
    """ store data in shelf """
    def __init__(self):
        self.local = 'localstore'

    def set_token(self, tkn):
        """ store token """
        with shelve.open(self.local, 'c') as store:
            store['token'] = str(tkn)

    def get_token(self):
        """ get token """
        with shelve.open(self.local, 'c') as store:
            tkn = store['token']
            return tkn
