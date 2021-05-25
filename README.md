# Agility CMS Python SDK

This package is a Python library for calling the [Agility CMS Rest API.](https://api-dev.aglty.io/swagger/index.html)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install agility-cms.

```bash
pip install agility-cms
```

## Usage

```python
import agility_cms

client = agility_cms.Client('<your guid>', '<your api key>', locale="en-us", preview=True)

client.gallery('<gallery id>')
client.item('<item id>', content_link_depth=1, expand_all_content_links=False)
client.list('<reference name>', fields=str(), take=10, skip=int(), filter_=str(), sort=str(), direction='asc', content_link_depth=1, expand_all_content_links=False)
client.page('<page id>', content_link_depth=2, expand_all_content_links=False)
client.sitemap('<channel name>', nested=False)
client.sync_items(sync_token=int(), page_size=500)
client.sync_pages(sync_token=int(), page_size=500)
client.url_redirections(last_access_date=str())
```
