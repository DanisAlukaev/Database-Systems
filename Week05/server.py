from misc import queries
from modules.service import preprocess

if __name__ == '__main__':
    preprocess.init_tables(queries)
    preprocess.populate(queries)
