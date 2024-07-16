from LinkedList.LinkedList import *

class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.key}={self.value}"

class HashMap:
    INITIAL_CAPACITY = 16
    LOAD_FACTOR = 0.75

    def __init__(self):
        self.buckets = [LinkedList() for _ in range(self.INITIAL_CAPACITY)]
        self.size = 0

    def get_bucket_index(self, key):
        hash_code = hash(key)
        return abs(hash_code) % len(self.buckets)

    def put(self, key, value):
        if (self.size / len(self.buckets)) >= self.LOAD_FACTOR:
            self.resize()
        bucket_index = self.get_bucket_index(key)
        for entry in self.buckets[bucket_index]:
            if entry.key == key:
                entry.value = value
                return
        self.buckets[bucket_index].add(Entry(key, value))
        self.size += 1

    def get(self, key):
        bucket_index = self.get_bucket_index(key)
        for entry in self.buckets[bucket_index]:
            if entry.key == key:
                return entry.value
        return None

    def remove(self, key):
        bucket_index = self.get_bucket_index(key)
        for entry in self.buckets[bucket_index]:
            if entry.key == key:
                self.buckets[bucket_index].remove(entry)
                self.size -= 1
                return entry.value
        return None

    def resize(self):
        old_buckets = self.buckets
        self.buckets = [LinkedList() for _ in range(len(old_buckets) * 2)]
        self.size = 0
        for bucket in old_buckets:
            for entry in bucket:
                self.put(entry.key, entry.value)

    def entry_set(self):
        entries = set()
        for bucket in self.buckets:
            for entry in bucket:
                entries.add(entry)
        return entries

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0
