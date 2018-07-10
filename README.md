# Face Recognition GraphQL Server
GraphQL Server for Facial Recognition. Work in Progress.

[![forthebadge](https://forthebadge.com/images/badges/powered-by-electricity.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/gluten-free.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![Made With GraphQL](https://img.shields.io/badge/made%20with-graphql-e00082.svg?longCache=true&style=for-the-badge)](http://graphene-python.org/)

## Installing
1. Install Pipenv.
2. Install cmake.
3. Run `pipenv install`. You're all set!

## Using the Server
To start the server, run `pipenv run python server.py`.
When you see something like:

```
Running on http://0.0.0.0:8000/ (Press CTRL+C to quit)
```

then the server is running and open it in `http://localhost:8000/graphql`.

### Adding Faces
To add faces to the server, use this mutation:

```graphql
mutation AddFace($name: String!, $imageData: String!) {
  addFace(name: $name, imageData: $imageData) {
    ok
  }
}
```

Add the name and base64 of an image to the `$name` and `$imageData` parameters, respectively.
`ok` will be `true` if the operation succeeds.

### Recognizing Faces

To recognize faces, use this mutation:

```graphql
mutation RecognizeFaces($imageData: String!) {
    recognizeFaces(imageData: $imageData) {
        names
    }
}
```

and use the base64 of an image as the argument to `$imageData`.

You'll get a response similar to this:

```json
{
  "data": {
    "recognizeFaces": {
      "names": [
        "Lisa (BlackPink)"
      ]
    }
  }
}
```

where `names` is a list of possible matches.

## Known Issues
1. Can't handle duplicate names yet.

## License
MIT