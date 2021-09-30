import requests
import json


class Client:
    def __init__(self, guid, api_key, locale="en-us", preview=False, url='api.aglty.io'):
        if preview:
            apitype = "preview"
        else:
            apitype = "fetch"

        self.__locale = locale
        self.__base = '/'.join([url, guid, apitype])
        self.__headers = {
            "accept": "application/json",
            "APIKey": api_key
        }

    def __get(self, url, params=None):
        if params is None:
            return requests.get(url, headers=self.__headers).json()
        else:
            return requests.get(url, headers=self.__headers, params=params).json()

    def __url(self, *args):
        return '/'.join([self.__base] + list(args))

    def gallery(self, gallery_id):
        return self.__get(self.__url('gallery', str(gallery_id)))

    def item(self, item_id, content_link_depth=1, expand_all_content_links=False):
        payload = {
            "contentLinkDepth": content_link_depth,
            "expandAllContentLinks": expand_all_content_links
        }
        return self.__get(self.__url(self.__locale, 'item', str(item_id)), params=payload)

    def list(self, reference_name, fields=str(), take=10, skip=int(), filter_=str(), sort=str(), direction='asc', content_link_depth=1, expand_all_content_links=False):
        payload = {
            'Take': take,
            'Skip': skip,
            'Direction': direction,
            'contentLinkDepth': content_link_depth,
            'expandAllContentLinks': expand_all_content_links
        }
        
        if fields != str():
            payload['Fields'] = fields
            
        if filter_ != str():
            payload['Filter'] = filter_
            
        if sort != str():
            payload['Sort'] = sort
            
        return self.__get(self.__url(self.__locale, 'list', reference_name.lower()), params=payload)

    def page(self, page_id, content_link_depth=2, expand_all_content_links=False):
        payload = {
            "contentLinkDepth": content_link_depth,
            "expandAllContentLinks": expand_all_content_links
        }
        return self.__get(self.__url(self.__locale, 'page', str(page_id)), params=payload)

    def sitemap(self, channel_name, nested=False):
        if nested:
            shape = "nested"
        else:
            shape = "flat"

        return self.__get(self.__url(self.__locale, 'sitemap', shape, channel_name.lower()))

    def sync_items(self, sync_token=int(), page_size=500):
        payload = {
            "pageSize": page_size
        }
        if sync_token != int():
            payload["syncToken"] = sync_token
        return self.__get(self.__url(self.__locale, 'sync', 'items'), params=payload)
        
    def sync_pages(self, sync_token=int(), page_size=500):
        payload = {
            "pageSize": page_size
        }
        if sync_token != int():
            payload["syncToken"] = sync_token
        return self.__get(self.__url(self.__locale, 'sync', 'pages'), params=payload)

    def url_redirections(self, last_access_date=str()):
        if last_access_date != str():
            payload = {"lastAccessDate": last_access_date}
        return self.__get(self.__url('urlredirection'), params=payload)
        
    def sync_all_items(self):
        all_items = []
        resp = self.sync_items()

        while len(resp['items']) > 0:
            all_items += resp['items']
            resp = self.sync_items(sync_token=resp['syncToken'])
        
        return all_items
        
    def sync_all_pages(self):
        all_items = []
        resp = self.sync_pages()

        while len(resp['items']) > 0:
            all_items += resp['items']
            resp = self.sync_pages(sync_token=resp['syncToken'])
        
        return all_items
