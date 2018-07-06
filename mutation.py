import graphene
from add_face import add_face
from recognize_faces import recognize_faces

class AddFace(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        image_data = graphene.String()

    ok = graphene.Boolean()

    def mutate(self, info, name, image_data):
        add_face(name, image_data)

        ok = True

        return AddFace(ok=ok)

class RecognizeFaces(graphene.Mutation):
    class Arguments:
        image_data = graphene.String()

    names = graphene.List(graphene.String)

    def mutate(self, info, image_data):
        names = recognize_faces(image_data)

        return RecognizeFaces(names=names)

class Mutation(graphene.ObjectType):
    add_face = AddFace.Field()
    recognize_faces = RecognizeFaces.Field()