# "Database code" for the DB Forum.

import psycopg2, bleach

#DBNAME = "forum"

def get_posts():
  DB = psycopg2.connect("dbname=forum")
  c = DB.cursor()
  c.execute("SELECT time, content FROM posts ORDER BY time DESC")
  #c.execute("UPDATE posts SET content = 'cheese' WHERE content LIKE '%spam%';")
  '''Get all the posts from the database, sorted with the newest first.

    Returns:
      A list of dictionaries, where each dictionary has a 'content' key
      pointing to the post content, and 'time' key pointing to the time
      it was posted.
    '''
  posts = tuple({'text': str(bleach.clean(row[0])), 'date': str(row[1])} for row in c.fetchall())
            #for row in c.fetchall())
  #posts.sort(key=lambda row: row['time'], reverse=True)
  #posts = ({'content': str(bleach.clean(row[1])), 'time': str(row[0])} for row in c.fetchall())
  DB.close()
  return posts

## Add a post to the database.
def add_post(content):
  DB = psycopg2.connect("dbname=forum")
  c = DB.cursor()
  c.execute("INSERT INTO posts (content) VALUES (%s)", (bleach.clean (content),))
  #c.execute("UPDATE posts ")
  DB.commit()
  DB.close()
