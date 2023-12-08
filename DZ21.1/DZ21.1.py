def popular_words (text, words):
    dct = {}
    text = text.lower()
    text = text.split()
    for x in words:
        number = text.count(x)
        dct[x] = number
    return dct

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')