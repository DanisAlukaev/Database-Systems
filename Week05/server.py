from misc import queries
from modules.service import preprocess, optimize

if __name__ == '__main__':
    preprocess.init_tables(queries)
    preprocess.populate(queries)
    optimize.check_performance(queries)
