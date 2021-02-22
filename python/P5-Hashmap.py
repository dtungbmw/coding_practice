
class Entry:
    def __init__(self, key, val):
        self.key=key
        self.val=val
    key=None
    val=None
    bucket=-1
    next=None
#caches the hashCode for each key
class MyHashMap:

    def myHash(self, k):
        return hash(k) % self.__size

    def put (self, key, value):
        bucket = self.myHash(key)

        if self.hashMap[bucket] is None:
            self.hashMap[bucket] = []
        entry = Entry(key, value)
        self.hashMap[bucket].append(entry)

    def get (self, key):
        bucket = self.myHash(key)
        for e in hashMap[bucket]:
            if key == e.key:
                return e.val
        return None

    def pop(self, key):
        bucket = self.myHash(key)
        for i in range(len(self.hashMap[bucket])):
            if key == self.hashMap[bucket][i].key:
                if len(self.hashMap[bucket]) ==1:
                    self.hashMap[bucket]=None
                else:
                    self.hashMap[bucket][i]=None


    def print(self):
        for elmList in self.hashMap:
            if elmList is not None and len(elmList)!=0:
                for elm in elmList:
                    print(elm.key)
                    print(elm.val)
        print("===")

    __size = 10
    hashMap = [None for x in range(__size)]


hm=MyHashMap()
hm.put("name", "David")
hm.put("phone", "2139485757")
hm.put("zip", "94086")
hm.put("state", "CA")

hm.print()

hm.pop("name")

hm.print()

