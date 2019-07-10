from django.contrib import admin
from django.urls import path

from leads.views.list_views import BasicListLeadView, GenericListLeadView, TemplateListLeadView
from leads.views.create_views import TemplateCreateLeadView, GenericCreateLeadView
from leads.views.list_api_views import (
    ListLeadAPIView,
    ListLeadWithSerializerAPIView,
    ListLeadGenericAPIView
)
from leads.views.create_api_views import (
    CreateLeadAPIView,
    CreateLeadWithSerializerAPIView,
    GenericCreateLeadAPIView,
    GenericListCreateLeadAPIView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BasicListLeadView.as_view(), name='basic-list-lead-view'),
    path('v2/', TemplateListLeadView.as_view(), name='template-list-lead-view'),
    path('v3/', GenericListLeadView.as_view(), name='generic-list-lead-view'),
    path('create/', TemplateCreateLeadView.as_view(), name='template-create-lead-view'),
    path('create/v2/', GenericCreateLeadView.as_view(), name='generic-create-lead-view'),
    path('api/', ListLeadAPIView.as_view(), name='basic-api-list-lead-view'),
    path('api/v2/', ListLeadWithSerializerAPIView.as_view(), name='basic-serializer-api-list-lead-view'),
    path('api/v3/', ListLeadGenericAPIView.as_view(), name='generic-api-list-lead-view'),
    path('api/create/', CreateLeadAPIView.as_view(), name='basic-create-api-view'),
    path('api/create/v2/', CreateLeadWithSerializerAPIView.as_view(), name='serializer-create-api-view'),
    path('api/create/v3/', GenericCreateLeadAPIView.as_view(), name='generic-create-api-view'),
    path('api/v4/', GenericListCreateLeadAPIView.as_view(), name='list-create-lead-api-view'),
]
