import graphene
from graphene_django import DjangoObjectType

from core.models import Category, Post


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "color", "posts")


class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = ("id", "author", "title", "categories", "description")


class Query(graphene.ObjectType):
    all_posts = graphene.List(PostType)
    all_categories = graphene.List(CategoryType)

    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_posts(root, info):
        # We can easily optimize query count in the resolve method
        return Post.objects.prefetch_related("categories").all()

    def resolve_all_categories(root, info):
        return Category.objects.all()

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)
