import graphene
from flask import Flask, jsonify, request, redirect
from flask_graphql import GraphQLView

app = Flask(__name__)

class Query(graphene.ObjectType):
    henlo = graphene.String(name=graphene.String(default_value="master"))

    def resolve_henlo(self, info, name):
        return 'henlo ' + name

schema = graphene.Schema(query=Query)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)