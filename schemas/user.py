def bookEntity(item) -> dict:
    return {
        #  "id" : int,
         "title": item["title"],
         "author": item["author"],
         "published_year": item["published_year"],
         "genre": item["genre"],
         "is_available": item["is_available"]
    }

def serializeList(entity) -> list:
    return [serializeDict(item) for item in entity]

def serializeDict(a) -> dict:
    return{**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

def serializeList(entity) -> list:
    return[serializeDict(a) for a in entity]