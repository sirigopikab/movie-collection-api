from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from monitoring.models import RequestCount


class RequestCountView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        obj = RequestCount.objects.get(key="global")
        return Response({"requests": obj.count})


class ResetRequestCountView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        RequestCount.objects.filter(key="global").update(count=0)
        return Response({"message": "request count reset successfully"})
