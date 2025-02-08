# To install, run: pip install tavily-python
from tavily import TavilyClient

client = TavilyClient(api_key="")

response = client.search(
    query="NASQ"
)

print(response['query'])
