from requests import get
from xml.etree import ElementTree as ET


def fetch_files(url,params):
    response = get(url, params=params)
    if response.status_code == 200:
        print("Files fetched successfully!")
        return response.text
    else:
        raise Exception(f"Failed to fetch files: {response.status_code}")



base_url = "https://export.arxiv.org/api/query?"
params = {"search_query": "all:AI", "start": 0, "max_results": 10 }
result = fetch_files(base_url, params)
print(result)


def parse_xml(result):
    tree = ET.fromstring(result)
    print(tree, "tree")
    return tree

xml_tree = parse_xml(fetch_files(base_url, params))
print(xml_tree, "xml tree")
