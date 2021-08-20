from flask_restful import Resource
from notion.client import NotionClient

client = NotionClient(token_v2=ffce6713816560c2034d3e957c8d7acee5a1509bf3b3b8be0debc17b725d44f935ff26a15d3641bd6b6467f6974f7961686ec97a0cefa4516beee8ecbae89a2469597f3d46174b22b1f260c1d00f)
page = client.get_block(https://www.notion.so/Action-Zone-422480d02bd345dda1631c55dbf0ca69)
cv = client.get_collection_view(https://www.notion.so/9715c9074dee4315aefbf549aa2b612e?v=37ebff7696e2488f98ebe53f00b16d2c)
pages = []

def get_title(page)
  return page.get('title')

class Todo(Resource)
  def get(self, id)
    pages.clear()
    for row in cv.collection.get_rows()
      if id in row.category
        temp = {
          'title' row.title,
          'website' row.website,
          'description' row.description,
          'logo' row.logo
          }
        pages.append(temp)
    pages.sort(key=get_title)
    return pages, 200