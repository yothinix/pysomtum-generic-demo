from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from ..models import Lead


class TemplateCreateLeadView(TemplateView):
    template_name = 'create_lead.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        data = request.POST

        Lead.objects.create(
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            email=data.get('email'),
            phone=data.get('phone'),
            message=data.get('message')
        )

        return redirect('template-list-lead-view')


class GenericCreateLeadView(CreateView):
    model = Lead
    fields = ['first_name', 'last_name', 'email', 'phone', 'message']
