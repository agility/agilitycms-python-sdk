# Agility CMS Python SDK

This package is a Python library for calling the [Agility CMS Rest API.](https://api-dev.aglty.io/swagger/index.html)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install agility-cms
```

## Usage

```python
import agility_cms

client = agility_cms.Client('<your guid>', '<your api key>')

client.gallery('<gallery id>')
client.item('<item id>')
client.list('<reference name>')
client.page('<page id>')
client.sitemap('<channel name>')
client.sync_items()
client.sync_pages()
client.url_redirections()
```
