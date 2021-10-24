# Movie Lovers API
This project provides the required APIs for creating, updating, receiving, and deleting different movies.

## API details
### Create a new movie
Request type: `POST`

Request URL: https://movie-lovers-vg.herokuapp.com/api/movies

Example input: 
```json
{
    "name": "Bolt",
    "genre": "Animation",
    "year": "2008"
}
```
Example output:
```json
{
    "genre": "Animation",
    "id": "_QItFyNaCrWLiejku1XnL9zYz1aT6tETIxI0g0kFP10",
    "name": "Bolt",
    "year": "2008"
}
```
### Update an existing movie
Request type: `POST`

Request URL: [https://movie-lovers-vg.herokuapp.com/api/movies/\<id>](https://movie-lovers-vg.herokuapp.com/api/movies/\<id>)

Example input: 
```json
{
    "name": "Bolt",
    "genre": "Animation-Comedy",
    "year": "2008"
}
```
Example output:
```json
{
    "genre": "Animation-Comedy ",
    "id": "G0a2gvqodIA2OmTNGh3u5LMApz0R-mXbCGYVPV9RzMk",
    "name": "Bolt",
    "year": "2008"
}
```

### Get all movies
Request type: `GET`

Request URL: https://movie-lovers-vg.herokuapp.com/api/movies

Example output:
```json
[
  {
    "genre": "Romance",
    "id": "eIk7hr-vS-7xj4N-Hh9ODv1Qt9AtPcPJq7-Laafg31Y",
    "name": "Pride & Prejudice",
    "year": "2005"
  },
  {
    "genre": "Animation",
    "id": "_QItFyNaCrWLiejku1XnL9zYz1aT6tETIxI0g0kFP10",
    "name": "Bolt",
    "year": "2008"
  }
]
```
### Get a movie
Request type: `GET`

Request URL: [https://movie-lovers-vg.herokuapp.com/api/movies/\<id>](https://movie-lovers-vg.herokuapp.com/api/movies/\<id>)

Example output: 
```json
{
    "genre": "Romance",
    "id": "eIk7hr-vS-7xj4N-Hh9ODv1Qt9AtPcPJq7-Laafg31Y",
    "name": "Pride & Prejudice",
    "year": "2005"
}
```

### Delete a movie
Request type: `DELETE`

Request URL: [https://movie-lovers-vg.herokuapp.com/api/movies/\<id>](https://movie-lovers-vg.herokuapp.com/api/movies/\<id>)

Example output:
```json
{
    "Success": "Movie ID #UqPfewVQwK4CsD9bkLevqNfPEGAeXPDUbitJvRYug1g has been deleted"
} 
```