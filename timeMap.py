class TimeMap:

    def __init__(self):
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        return None

    def get(self, key: str, timestamp: int) -> str:
        return ""    
    

myTimeMap = TimeMap()
myTimeMap.set("foo", "bar", 1)
print(myTimeMap.get("foo", 1))
print(myTimeMap.get("foo", 3))
