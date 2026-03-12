book = {
    "heading": "white nights",
    'author': "dostoevsky",
    "realese date": "1848",
    "pages":"158"

}

del book['realese date']
print(book)

book.popitem()
print(book)