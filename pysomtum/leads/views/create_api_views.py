from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from ..models import Lead
from ..serializers import LeadSerializer


class CreateLeadAPIView(APIView):
    def post(self, request):
        data = request.data

        lead = Lead.objects.create(
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            email=data.get('email'),
            phone=data.get('phone'),
            message=data.get('message')
        )

        data = {
            'id': lead.id,
            'first_name': lead.first_name,
            'last_name': lead.last_name,
            'email': lead.email,
            'phone': lead.phone,
            'message': lead.message
        }

        return Response(data)


class CreateLeadWithSerializerAPIView(APIView):
    def post(self, request):
        serializer = LeadSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()

        return Response(serializer.data)


class GenericCreateLeadAPIView(CreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer


class GenericListCreateLeadAPIView(ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer


class LeadViewSet(ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
