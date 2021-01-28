from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework import status
from django.http import Http404
from .models import GameList
from .serializers import GameListSerializer


class GameDetail(APIView):
    """
    Serializers define the API representation.
    """
    parser_class = (FileUploadParser,)

    def get_object(self, pk):
        try:
            return GameList.objects.get(pk=pk)
        except GameList.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            game = self.get_object(pk)
            serializer = GameListSerializer(game)
        else:
            game = GameList.objects.all().select_related('id')
            serializer = GameListSerializer(game, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk=None):
        serializer = GameListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        game = self.get_object(pk)
        serializer = GameListSerializer(game, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        game = self.get_object(pk)
        game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

