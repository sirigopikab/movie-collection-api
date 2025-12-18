from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .services import fetch_movies


class MoviesListView(APIView):
    def get(self, request):
        try:
            page_url = request.query_params.get("page")
            data = fetch_movies(page_url)
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            print("Movie API error:", e)
            return Response(
                {"error": "Movie service unavailable"},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
    )

            
        
