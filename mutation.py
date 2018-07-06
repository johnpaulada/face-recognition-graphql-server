import graphene

class AddFace(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        image_data = graphene.List(graphene.String)

    ok = graphene.Boolean()

    def mutate(self, info, name, image_data):
        # TODO: Add face here

        ok = True
        return CreatePerson(ok=ok)

class Mutation(graphene.ObjectType):
    add_face = AddFace.Field()