from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from ..models import Lead


class BasicListLeadView(View):
    def get(self, request, *args, **kwargs):
        leads = Lead.objects.all()

        response = '<h1>Applicant List</h1>'
        response += '<ul>'
        for lead in leads:
            response += f'<li>'
            response += f'<h3>Applicant ID {lead.id}: {lead.first_name} {lead.last_name}</h3>'
            response += f"<p>Email: <a href='mailto:{lead.email}'>{lead.email}</a></p>"
            response += f"<p>Phone: {lead.phone}</p>"
            response += f"<p>Message: {lead.message}</p>"
            response += f'</li>'
        response += '</ul>'

        return HttpResponse(response)


class TemplateListLeadView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        leads = Lead.objects.all()

        context = {'leads': leads}

        return render(request, self.template_name, context)


class GenericListLeadView(ListView):
    model = Lead
