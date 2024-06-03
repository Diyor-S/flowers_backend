from .models import *
from .serializers import *
from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListAPIView
# Create your views here.


class ConfigView(RetrieveAPIView):
    serializer_class = ConfigSerializer
    queryset = CommonSettings.objects.all()

    def get_object(self):
        return CommonSettings.objects.first()