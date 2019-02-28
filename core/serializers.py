from django.db.models.fields.related import ManyToManyField, OneToOneField, ForeignKey
from rest_framework import serializers
from .models import Ingredient, Recipe, Cooker
from drf_writable_nested import WritableNestedModelSerializer

#class IngredientSerializer(serializers.HyperlinkedModelSerializer):
from rest_framework.relations import PrimaryKeyRelatedField


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        #fields = ('url', 'id', 'name') #url field is additional resource to link the model as hyperlink
        fields = ('id', 'name')


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ('url', 'id', 'ingredients', 'name', 'directions', 'description')
        #fields = '__all__'

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        recipe = Recipe.objects.create(**validated_data)

        for ingredient in ingredients_data:
            ingredient, created = Ingredient.objects.get_or_create(name=ingredient['name'])
            recipe.ingredients.add(ingredient)
        return recipe

    def update(self, instance, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        instance.name = validated_data['name']
        instance.description = validated_data['description']
        instance.directions = validated_data['directions']

        for ingredient in ingredients_data:
            ingredient, created = Ingredient.objects.update_or_create(name=ingredient['name'])
            instance.ingredients.add(ingredient)
        return instance


class CookerSerializer(WritableNestedModelSerializer):
    recipes = RecipeSerializer(many=True)
    #recipes = PrimaryKeyRelatedField(queryset=Recipe.objects.all())
    #recipes = ManyToManyField(Recipe)

    #ingredients = PrimaryKeyRelatedField(queryset=Ingredient.objects.all())
    ingredients = IngredientSerializer(many=True, read_only=True)

    #tmp = Cooker.objects.values("name").contains({'key': '3'})
    #if tmp.count() > 0:
    #    item_id = tmp[0].id

    class Meta:
        model = Cooker
        #fields = '__all__'
        fields = ( 'age', 'name', 'recipes', 'ingredients')