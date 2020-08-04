import graphene
from graphene_django import DjangoObjectType
from .models import User


class UserType(DjangoObjectType):
  class Meta:
    model = User


class RegisterMutation(graphene.Mutation):
  # Register arguments
  class Arguments:
    email = graphene.String()
    password = graphene.String()
  
  # This is the user field
  user = graphene.Field(UserType)

  # Save the user data and return the user
  def mutate(self, info, email, password):
    user = User(email=email)
    user.set_password(password)
    user.save()
    return RegisterMutation(user=user)
