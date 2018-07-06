import graphene

class Query(graphene.ObjectType):
    henlo = graphene.String(name=graphene.String(default_value="master"))

    def resolve_henlo(self, info, name):
        return 'henlo ' + name