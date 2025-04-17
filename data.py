def valid_meme_body_post():
    return {
        "text": "funny cat",
        "url": "https://timeweb.com/media/articles/0001/18/thumb_17628_articles_standart.png",
        "tags": ["funny", "test"],
        "info": {"author": "tester"}
    }

def meme_body_missing_field(field):
    body = valid_meme_body_post()
    if field in body:
        del body[field]
    return body

def valid_meme_body_put(meme_id):
    return {
        "id": meme_id,
        "text": "funny cat",
        "url": "https://timeweb.com/media/articles/0001/18/thumb_17628_articles_standart.png",
        "tags": ["funny", "test"],
        "info": {"author": "tester"}
    }
