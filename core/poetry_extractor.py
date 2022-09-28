import requests
from random import randrange

class PoetryExtractor:
    url = ""
    
    def get_data(self):
        resp = requests.get(url = self.url)
        data = resp.json()

        return data

    def get_data_tuple(self):
        data = self.get_data()

        list_of_tuples = []

        for index, item in enumerate(data['authors']):
            list_of_tuples.append((index+1, item))

        return (tuple(list_of_tuples))

    def get_random_work(self):
        data = self.get_data()
        return data[randrange(len(data))]



