"""
Prompt

Implement an unbounded set where each entry has an expiration date and disappears once it has expired.

Clarify what an unbounded set is with examples of expiration date

"I wrote the code and please do a code review for me and provide feedback."

Solution

Expected Solution - Milestones

Clarifies the requirements including on expiration date.
Come up with a basic approach of what the solution.
Demonstrates of understanding of concepts like LRU cache, Hashmap and Priority queue.
Implements the expiration date from the beginning and determines the key expiration.
Handles expired keys and purges them.
"""

from heapq import heappop, heappush
import time
import threading

class TTLCache:
    def __init__(self,ttl) -> None:
        self.ttl = ttl
        self.map = {} # (key,timestamp_added)
        self.heap = [] # min heap with time stamp entries
        self.lazy_delete = set() # to lazily delete heap entries
        self.lock = threading.RLock() # reentrant lock to prevent deadlock scenario

    def cleanup(self,now):
        with self.lock:
            print('lock acquired')
            while self.heap and (self.heap[0][0]+self.ttl < now or self.heap[0] in self.lazy_delete):
                _,key=heappop(self.heap)
                if key in self.map:
                    del self.map[key]

    def add(self,key):
        with self.lock:
            print('lock acquired')
            now = time.time()
            self.cleanup(now)
            self.map[key] = now
            heappush(self.heap,(now,key))
    
    def contains(self,key):
        with self.lock:
            now = time.time()
            self.cleanup(now)
            return key in self.map
    
    def remove(self,key):
        with self.lock:
            if not self.contains(key):
                raise KeyError(f"{key} doesn't exist")
            self.lazy_delete.add(self.map[key],key)
            now = time.time()
            self.cleanup(now)
            del self.map[key]

if __name__ == '__main__':
    ttlCache = TTLCache(10)
    ttlCache.add('A')
    time.sleep(20)
    print(ttlCache.contains('A'))

    
        
        