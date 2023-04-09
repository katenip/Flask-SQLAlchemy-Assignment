class MovieRepository:
    
    from flask_sqlalchemy import SQLAlchemy

    movie_id = 0
    
    def get_all_movies(self):
        import psycopg2
        #put login here 
        conn = psycopg2.connect(database="",
                            user="",
                            password="",
                            host="localhost", port="5432")
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM movie;''')
        movies = cursor.fetchall()
        conn.commit()
        conn.close()
        return movies

    def get_movie_by_id(self, movie_id):
        import psycopg2
        #put login here 
        conn = psycopg2.connect(database="",
                            user="",
                            password="",
                            host="localhost", port="5432")
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM movie
        WHERE movie_id = %(id)s ;''', {"id": movie_id})
        movies = cursor.fetchall()
        conn.commit()
        conn.close()
        return movies

    def create_movie(self, title, director, rating):
        import psycopg2
        #put login here 
        conn = psycopg2.connect(database="",
                            user="",
                            password="",
                            host="localhost", port="5432")
        cursor = conn.cursor()
        cursor.execute('''SELECT count(DISTINCT(movie_ID)) FROM movie;''')
        movie_Amount = cursor.fetchall()
        movie_Amount = int(movie_Amount[0][0]) + 1
        cursor.execute("INSERT INTO movie (title, director, rating, movie_ID) VALUES(%s, %s, %s, %s)", (title, director, rating, movie_Amount))
        conn.commit()
        conn.close()
        self.movie_id = movie_Amount
        return self

    def search_movies(self, title):
        import psycopg2
        #put login here 
        conn = psycopg2.connect(database="",
                            user="",
                            password="",
                            host="localhost", port="5432")
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM movie
        WHERE title = %(title)s ;''', {"title": title})
        movies = cursor.fetchall()
        conn.commit()
        conn.close()
        return movies


# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()
