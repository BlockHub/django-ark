import graphene
import ark.schema


class Query(ark.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)