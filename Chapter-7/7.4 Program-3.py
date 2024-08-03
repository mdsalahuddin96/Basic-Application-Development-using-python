try:
    f = open('missing')
except OSError:
    print('It failed')
except FileNotFoundError:
    print('File not found')

