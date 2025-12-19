from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .models import Collection
from .serializers import CollectionSerializer
from collections import Counter

class CollectionListCreateView(APIView):
    permission_classes = [IsAuthenticated]

 

    def get(self, request):
        collections = Collection.objects.filter(user=request.user)
        serializer = CollectionSerializer(collections, many=True)

        # gather all genres
        genre_list = []
        for c in collections:
            for movie in c.movies.all():
                # multiple genres may be comma separated
                parts = [g.strip() for g in movie.genres.split(",")]
                genre_list.extend(parts)

        # find top 3
        favourite_genres = [g for g, _ in Counter(genre_list).most_common(3)]

        return Response({
            "is_success": True,
            "data": serializer.data,
            "favourite_genres": favourite_genres
        })


    def post(self, request):
        data = request.data
        data["user"] = request.user.id

        serializer = CollectionSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        return Response({
            "collection_uuid": serializer.data["uuid"]
        })


class CollectionDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, uuid):
        collection = get_object_or_404(Collection, uuid=uuid, user=request.user)
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)

    def put(self, request, uuid):
        collection = get_object_or_404(Collection, uuid=uuid, user=request.user)

        serializer = CollectionSerializer(collection, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"message": "Collection updated"})

    def delete(self, request, uuid):
        collection = get_object_or_404(Collection, uuid=uuid, user=request.user)
        collection.delete()
        return Response({"message": "Collection deleted"})
