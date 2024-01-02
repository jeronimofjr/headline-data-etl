from logging import basicConfig, DEBUG, info
from pipeline import pipeline_data

def init():

    basicConfig(filename="log.txt", format="%(asctime)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S", level=DEBUG)
    info('Started')
    pipeline_data()
    info('Finished')

if __name__ == '__main__':
    init()



