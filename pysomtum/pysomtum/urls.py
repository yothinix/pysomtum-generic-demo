from django.contrib import admin
from django.urls import path

from leads.views.list_views import BasicListLeadView, GenericListLeadView, TemplateListLeadView
from leads.views.create_views import TemplateCreateLeadView, GenericCreateLeadView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BasicListLeadView.as_view(), name='basic-list-lead-view'),
    path('v2', TemplateListLeadView.as_view(), name='template-list-lead-view'),
    path('v3', GenericListLeadView.as_view(), name='generic-list-lead-view'),
    path('create', TemplateCreateLeadView.as_view(), name='template-create-lead-view'),
    path('create/v2', GenericCreateLeadView.as_view(), name='generic-create-lead-view'),
]
