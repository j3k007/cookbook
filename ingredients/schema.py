import graphene
from graphene_django import DjangoObjectType
from .models import Category, Ingredients

class CategoryType(DjangoObjectType):
    class Meta:
        model=Category
        fields=("id", "name", "ingredients")
        
class IngredientsType(DjangoObjectType):
    class Meta:
        model=Ingredients
        fields=("id", "name", "notes", "category")
        
class Query(graphene.ObjectType):
    all_ingredients=graphene.List(IngredientsType)
    category_by_name=graphene.Field(CategoryType, 
                                    name=graphene.String(required=True))
    
    def resolve_all_ingregients(root, info):
        return Ingredients.objects.select_related("category").all()
    
    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None
        
schema=graphene.Schema(query=Query)