import graphene
import base64

class AddFace(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        image_data = graphene.List(graphene.String)

    ok = graphene.Boolean()

    def mutate(self, info, name, image_data):
        images = map(base64.decodestring, image_data)

        ok = True
        
        return AddFace(ok=ok)

class Mutation(graphene.ObjectType):
    add_face = AddFace.Field()