from .serializers import AuthSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

"""
register view using view set 
serializer class is to be converted to model instances to json or xml datatype
"""


class RegisterView(GenericViewSet):
    serializer_class = AuthSerializer

    def create(self, request):
        """

        :param request:  passed endpoint to response
        :return: response when serializer data valid
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": serializer.data}, status=status.HTTP_400_BAD_REQUEST)