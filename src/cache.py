class Cache(dict):
    def __init__(self, server_url):
        self.server_url = server_url

    def __setitem__(self, key, value, expiration):
        item = Item(value, expiration)
        super().__setitem__(key,item)

    def __getitem__(self,key):
        item = super().__getitem__(key)
        if item.expiration != 0:
            return item.value


class Item:
    def __init__(self, value, expiration):
        self.value = value
        self.expiration= expiration
