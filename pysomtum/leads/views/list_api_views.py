from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Lead
from ..serializers import BasicLeadSerializer, LeadSerializer


class ListLeadAPIView(APIView):
    def get(self, request):
        leads = Lead.objects.all()

        lead_list = []
        for lead in leads:
            data = {
                'id': lead.id,
                'first_name': lead.first_name,
                'last_name': lead.last_name,
                'email': lead.email,
                'phone': lead.phone,
                'message': lead.message
            }
            lead_list.append(data)

        return Response(lead_list)


class ListLeadWithSerializerAPIView(APIView):
    def get(self, request):
        leads = Lead.objects.all()

        # Method 1:
        lead_list = []
        for lead in leads:
            serializer = BasicLeadSerializer(lead)
            lead_list.append(serializer.data)

        # Method 2:
        serializer = BasicLeadSerializer(leads, many=True)
        lead_list = serializer.data

        return Response(lead_list)


class ListLeadGenericAPIView(ListAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
