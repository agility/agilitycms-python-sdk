import requests


class Client:
    def __init__(self, guid, api_key, locale="en-us", preview=True):
        if preview:
            apitype = "preview"
        else:
            apitype = "fetch"

        self.__locale = locale
        self.__base = '/'.join(["https://api-dev.aglty.io", guid, apitype])
        self.__headers = {
            "accept": "application/json",
            "APIKey": api_key
        }

    def __get(self, url, params=None):
        if params is None or len(params) == 0:
            return requests.get(url, headers=self.__headers).json()
        else:
            return requests.get(url, headers=self.__headers, params=params).json()

    def __url(self, *args):
        return '/'.join([self.__base] + list(args))

    def gallery(self, gallery_id):
        return self.__get(self.__url('gallery', str(gallery_id)))

    def item(self, item_id, **kwargs):
        url = self.__url(self.__locale, 'item', str(item_id))
        return self.__get(url, params=kwargs)

    def list(self, reference_name, **kwargs):
        return self.__get(self.__url(self.locale, 'list', reference_name), params=kwargs)

    def page(self, page_id, **kwargs):
        return self.__get(self.__url(self.locale, 'page', str(page_id)), params=kwargs)

    def sitemap(self, channel_name, nested=False):
        if nested:
            shape = "nested"
        else:
            shape = "flat"

        return self.__get(self.__url(self.__locale, 'sitemap', shape, channel_name))

    def __sync(self, object_type, **kwargs):
        return self.__get(self.__url(self.__locale, 'sync', object_type), params=kwargs)

    def sync_items(self, **kwargs):
        return self.__sync("items", **kwargs)

    def sync_pages(self, **kwargs):
        return self.__sync("pages", **kwargs)

    def url_redirections(self, **kwargs):
        return self.__get(self.__url('urlredirection'), params=kwargs)






