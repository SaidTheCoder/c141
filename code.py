from flask import Flask,jsonify,request
import csv
from pprint import pprint
all_movies=[]
with open("movies.csv", newline ="",encoding="utf8") as f:
    reader=csv.reader(f)
# pprint(reader)
    data = list(reader)
# print(data)
    all_movies=data[1:]

liked_movies=[]
not_liked_movies=[]
did_not_watch=[]
app=Flask(__name__)
@app.route("/get-movie")

def get_movie():
    return jsonify({
        "data":all_movies[0],
        "status":"success"
    })

@app.route("/liked-movies",methods=["POST"])
def liked_movie():
    movie=all_movies[0]
    all_movies=all_movies[1:]
    liked_movies.append(movie)
    return  jsonify({
        "status":"success"
    }),


@app.route("/unliked-movies",methods=["POST"])
def unliked_movie():
    movie=all_movies[0]
    all_movies=all_movies[1:]
    not_liked_movies.append(movie)
    return  jsonify({
        "status":"success"
    }),


@app.route("/did-not-watch",methods=["POST"])
def did_not_watch_movie():

    movie=all_movies[0]
    all_movies=all_movies[1:]
    did_not_watch.append(movie)
    return  jsonify({
        "status":"success"
    }),

if __name__=="__main__":
    app.run()