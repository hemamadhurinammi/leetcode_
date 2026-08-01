class MyHashMap:
    def __init__(self):
        self.d = []
    def put(self, key: int, value: int) -> None:
        t = (key,value)
        for i in range(len(self.d)):
             if self.d[i][0] == key:
                 self.d[i] = t
                 return
        self.d.append(t)
    def get(self, key: int) -> int:
        j=0
        for i in range(len(self.d)):
          if self.d[i][j] == key:
            return self.d[i][j+1]
        return -1
    def remove(self, key: int) -> None:
        k=0
        for i in range(len(self.d)):
            if self.d[i][k]==key:
                self.d.pop(i)
                return
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)