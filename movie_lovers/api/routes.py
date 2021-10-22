from flask import Blueprint, request, jsonify
from movie_lovers.helpers import token_required
from movie_lovers.models import User, Movie, db, movie_schema, movies_schema


api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/getdata')
def getdata():
    return {'item_1': 'hello', 'item_2': 'worlds'}


# CRUD functionality below

@api.route('/movies', methods=['POST'])
@token_required
def create_movie(current_user_token):
    name = request.json['name']
    genre = request.json['genre']
    year= request.json['year']
    token = current_user_token.token


    movie = Movie(name,genre,year,user_token = token)

    db.session.add(movie)
    db.session.commit()

    response = movie_schema.dump(movie)
    return jsonify(response)



@api.route('/movies', methods = ['GET'])
@token_required
def get_movies(current_user_token):
    owner = current_user_token.token
    movies = Movie.query.filter_by(user_token = owner).all()
    response = movies_schema.dump(movies)
    return jsonify(response)


@api.route('/movies/<id>', methods= ['GET'])
@token_required
def get_movie(current_user_token, id):
    movie = Movie.query.get(id)
    if movie:
        response = movie_schema.dump(movie)
        return jsonify(response)
    else:
        return jsonify({'Error': 'That movie does not exist!'})



@api.route('/movies/<id>', methods= ['POST', 'PUT'])
@token_required
def update_movie(current_user_token, id):
    movie = Movie.query.get(id)
    print(movie)
    if movie:
        movie.name = request.json['name']
        movie.genre = request.json['genre']
        movie.year = request.json['year']
        movie.token_token = current_user_token.token
        db.session.commit()

        response = movie_schema.dump(movie)
        return jsonify(response)
    else:
        return jsonify({'Error': 'That movie does not exist!'})

# DELETE ROUTE
@api.route('/movies/<id>', methods= ['DELETE'])
@token_required
def delete_movies(urrent_user_token, id):
    movie = Movie.query.get(id)
    if movie:
        db.session.delete(movie)
        db.session.commit()
        return jsonify({'Success': f'Movie ID #{movie.id} has been deleted'})
    else:
        return jsonify({'Error': 'That movie does not exist!'})
