from requests import get
import feedparser

base_url = "http://export.arxiv.org/api/query?search_query"
def fetch_files(url, topic):
    url = f"{url}={topic}&start=0&max_results=10"
    response = get(url)
    if response.status_code == 200:
        print("Files fetched successfully!")
        return response.text
    else:
        raise Exception(f"Failed to fetch files: {response.status_code}")



# input_topic = input("Enter a research topic to search for: ")
# xml_tree = fetch_files(base_url, input_topic)
# #print(xml_tree, "xml tree")


# #parse the XML response

# feed = feedparser.parse(xml_tree)
# print(len(feed.entries), "number of entries found")
# for entry in feed.entries:

#     print(f"Title: {entry.title}")
#     print(f"Authors: {', '.join(author.name for author in entry.authors)}")
#     print(f"Published: {entry.published}")
#     print(f"Summary: {entry.summary}\n")
