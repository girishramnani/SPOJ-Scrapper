__author__ = 'Girish'
import requests


class DataFetcher(object):
    def __init__(self, url_pattern, start=0, step=50, **kwargs):
        try:
            self.url_pattern = url_pattern
            self.url = url_pattern.format(start=start)
            self.start = start
            self.step = step
        except Exception as e:
            print(e)


    def get_page(self):
        while True:
            response = requests.get(self.url)
            yield response.content.decode()
            self.start += self.step
            self.url = self.url_pattern.format(start=self.start)




