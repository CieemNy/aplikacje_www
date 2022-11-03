from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Osoba
from .serializers import OsobaSerializer


@api_view(['GET'])
def osoba_list(request):
    if request.method == 'GET':
        osoby = Osoba.objects.all()
        serializer = OsobaSerializer(osoby, many=True)
        return Response(serializer.data)
