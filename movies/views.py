from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .services import get_movies


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def movies_list(request):
    page = request.GET.get("page", 1)

    try:
        movies = get_movies(page)
        return Response({"movies": movies})
    except Exception:
        return Response(
            {"error": "Movie service unavailable"},
            status=503
        )
