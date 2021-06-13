# Context managers

#Functionaliteten kodet manuelt
from contextlib import contextmanager


class OpenFile():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print('__enter__')
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, *args):
        print('__exit__')
        self.file.close()

#with OpenFile('timelog2.txt', 'w') as file:
#    file.write('Testing')


#with OpenFile('timelog.txt', 'r') as file:
#    print(file.readlines())

@contextmanager
def openFile(file,mode):
    try:
        f = open(file, mode)
        yield f
    finally:
        f.close()

with openFile('timelog.txt', 'w') as f:
    f.write('Hej med dig jeg hedder kaj')

print(f.closed)