__author__ = 'Girish'
import requests

#High priority Class

class DataFinder(object):
    """
    takes a url_patterns and then according to the step and start point ( for now which are configured for
    the SPOJ downloader) lazily yields the content of the next page which then is used by the search method
    to find the content using the snippet passed in the search.

    :param
    url_patterns -> a format string having dictionary mapping e.g. www.google.com?q={start}
    start ->the initial index
    step -> the step index
    **kwargs ->mappings that will be accepted by the format string ( will be implemented later)
    """
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




