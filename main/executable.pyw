import os
from source import start

if __name__ == '__main__':
    if os.name == 'nt':
        if os.path.exists('C:/lDev'):
            start()
        else:
            os.makedirs('C:/lDev')
            os.replace(os.path.dirname(__file__) + 'cache', 'C:/lDev/source.py')