# Agility CMS Python SDK

This package is a Python library for calling the [Agility CMS Rest API.](https://api-dev.aglty.io/swagger/index.html)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install agility-cms.

```bash
pip install agility-cms
```

## Initialization
```python
import Client from agility_cms

client = Client(
    '<your guid>', 
    '<your api key>', 
    locale="en-us", 
    preview=True, 
    url="api.aglty.io"
)
```
### Required Arguments
* guid (str)
* api_key (str)

### Optional Arguments
* locale (str)
* preview (bool)
* url (str)

## Gallery
```python
client.gallery('<gallery id>')
```
### Required Arguments
* gallery_id (int)

## Item
```python
client.item(
    '<item id>', 
    content_link_depth=1, 
    expand_all_content_links=False
)
```
### Required Arguments
* item_id (int)

### Optional Arguments
* content_link_depth (int)
* expand_all_content_links (bool)

## List
```python
client.list(
    '<reference name>', 
    fields="", 
    take=10, 
    skip=0, 
    filter_="", 
    sort="", 
    direction='asc', 
    content_link_depth=1, 
    expand_all_content_links=False
)
```
### Required Arguments
* reference_name (str)

### Optional Arguments
* fields (str)
* take (int)
* skip (int)
* filter (str)
* sort (str)
* direction (str)
* content_link_depth (int)
* expand_all_content_links (bool)

## Page
```python
client.page(
    '<page id>', 
    content_link_depth=2, 
    expand_all_content_links=False
)
```
### Required Arguments
* page_id (int)

### Optional Arguments
* content_link_depth (int)
* expand_all_content_links (bool)

## Sitemap
```python
client.sitemap('<channel name>', nested=False)
```
### Required Arguments
* channel_name (str)

### Optional Arguments
* nested (bool)

## Sync Items
```python
client.sync_items(sync_token=0, page_size=500)
```
### Optional Arguments
* sync_token (int)
* page_size (int)

## Sync Pages
```python
client.sync_pages(sync_token=0, page_size=500)
```
### Optional Arguments
* sync_token (int)
* page_size (int)

## Url Redirections
```python
client.url_redirections(last_access_date="")
```
### Optional Arguments
* last_access_date (str)

