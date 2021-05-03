from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic.base import View, TemplateView

from app.models import Organization, Document


class Login(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        # user = User.objects.get(username=username, password=password)
        if user:
            login(request, user)
            print('login')
            return HttpResponseRedirect(reverse('org_list'))
        return render(request, 'login.html', {'error': True})


class OrganizationList(TemplateView):
    template_name = 'organization/list.html'

    def get_context_data(self, **kwargs):
        organization = Organization.objects.all()
        context = {
            'organizations': organization
        }
        return context


class DocumentList(TemplateView):
    template_name = 'document/list.html'

    def get_context_data(self, **kwargs):
        doc = Document.objects.all()
        context = {
            'docs': doc
        }
        return context