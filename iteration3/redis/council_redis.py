import redis
import mysql.connector

def council_to_redis():
    redis_conn = redis.Redis(host='34.198.149.11', port=6379)

    # if not connected to redis then exit
    try:
        redis_conn.ping()
        print("redis Connected")
    except redis.ConnectionError:
        print("redis Not Connected")
        return

    # Connect to MySQL and Redis
    mysql_conn = mysql.connector.connect(
        host='carbonvic.clx2a8hznypy.us-east-1.rds.amazonaws.com',
        user='greenh47',
        password='RRCgwXAfWw53cej',
        database='council'
    )
    # if not connected to mysql then exit
    if mysql_conn.is_connected() == False:
        print("mysql Not Connected")
        return
    else:
        print("mysql Connected")


    # Retrieve data from MySQL
    cursor = mysql_conn.cursor()
    cursor.execute('SELECT * FROM Waste_policy limit 1')
    rows = cursor.fetchall()
    print(rows[0])
    # name = rows[0][0]

    print("All data extracted")
    # print rows count
    print("rows count: ", len(rows))
    print("=====================================")


    # Format and store data in Redis

    print("All data stored in redis")
    # print redis bin data count
    print("redis data count: ", redis_conn.dbsize())

    print("redis data template:")
    # print(redis_conn.hgetall(f'bin:{name}'))


    # Close MySQL and Redis connections
    cursor.close()
    mysql_conn.close()
    redis_conn.close()


if __name__ == '__main__':
    council_to_redis()