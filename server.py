import graphene
from flask import Flask
from flask_graphql import GraphQLView
from schema import schema
from waitress import serve


GRAPHQL_ENDPOINT = '/graphql'

app = Flask(__name__)
app.add_url_rule(GRAPHQL_ENDPOINT, view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == "__main__":
    serve(app, listen='*:8000')