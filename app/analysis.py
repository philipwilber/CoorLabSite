import pandas as pd
from pymongo import MongoClient
import matplotlib,pylab as plt

# def _connect_mogo(db):
# 	conn = MongoClient('localhost', 27017)
# 	return conn[db]

# def read_mongo(db, collection, query={}, no_id=True):
# 	db = _connect_mogo(db)
# 	cursor = db[collection].find(query)

# 	df = pd.DataFrame(list(cursor))

# 	if no_id:
# 		del df['_id']

# 	return df


if __name__ == '__main__':
    conn = MongoClient('localhost', 27017)
    db = conn.DB_DIANPING
    tb_restaurant = db.TB_RESTAURANT
    df = pd.DataFrame(list(tb_restaurant.find({'per_price':{'$ne':'', '$lt':'50'}}, {'per_price':1,'_id':0})))

    print(df['per_price'].astype('int').describe())
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.hist(df['per_price'].astype('int'), 5)
    plt.title('人均价格分布')
    plt.xlabel('价格')
    plt.ylabel('餐厅数')
    print(plt.show())