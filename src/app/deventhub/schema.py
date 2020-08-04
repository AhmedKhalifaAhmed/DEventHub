import graphene
import graphql_jwt
from core.schema import RegisterMutation as RegisterMutation


# Create root mutation
class Mutation(graphene.ObjectType):
  # JWT Auth mutations
  token_accounts = graphql_jwt.ObtainJSONWebToken.Field()
  verify_token = graphql_jwt.Verify.Field()
  refresh_token = graphql_jwt.Refresh.Field()
  revoke_token = graphql_jwt.Revoke.Field()
  # User account auth mutations
  register = RegisterMutation.Field()


# Create root query
class Query(graphene.ObjectType):
  pass


# Create schema
schema = graphene.Schema(mutation=Mutation)
