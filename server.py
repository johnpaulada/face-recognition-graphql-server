import graphene
from flask import Flask
from flask_graphql import GraphQLView
from schema import schema

GRAPHQL_ENDPOINT = '/graphql'

app = Flask(__name__)
app.add_url_rule(GRAPHQL_ENDPOINT, view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)