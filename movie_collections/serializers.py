from rest_framework import serializers
from .models import Collection, Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["title", "description", "genres"]


class CollectionSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)

    class Meta:
        model = Collection
        fields = ["uuid", "title", "description", "movies"]

    def create(self, validated_data):
        movies_data = validated_data.pop("movies")
        collection = Collection.objects.create(**validated_data)

        for movie in movies_data:
            Movie.objects.create(collection=collection, **movie)

        return collection

    def update(self, instance, validated_data):
        movies_data = validated_data.pop("movies")

        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.save()

        instance.movies.all().delete()

        for movie in movies_data:
            Movie.objects.create(collection=instance, **movie)

        return instance
