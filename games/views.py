from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Game
from .serializers.common import GameSerializer

# Create your views here.
class GameListCreateView(APIView):
    #Index route
    def get(self, request):
        games = Game.objects.all()
        serialized_games = GameSerializer(games, many = True)
        return Response(serialized_games.data)