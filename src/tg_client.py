K = TypeVar("T")
V = TypeVar("K")

class Entry[V]:
    value: V
    expiration: float # epoch in millis
    last_used: float # epoch in millis
    last_updated: float #epoch in millis
    
class Cache[K,V]:
    """A distributed cache with localized data for high performance"""
    
    def put(self, key: K, value: V):
        //todo

    def get(self, key: K) -> V:
        //todo
        
