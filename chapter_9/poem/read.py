
# .read()
with open("poem.txt", encoding="utf-8") as f:
    print(f.read())

    '''
    Line one
    Line two
    Line three
    '''

# .readline()
with open("poem.txt", encoding="utf-8") as f:
    print(f.readline())
    print(f.readline())
    '''
    
    Line one

    Line two
    '''

# .readlines()
with open("poem.txt", encoding="utf-8") as f:
    lines = f.readlines()
    print(lines)
    '''
    ['Line one\n', 'Line two\n', 'Line three\n']
    '''
