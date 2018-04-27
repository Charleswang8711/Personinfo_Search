from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.views.generic import ListView
from .models import PersonProfile
from .serializer import PersonInfoSerializer
from rest_framework import generics


def index(request):
    return render(request,'personinfo/index.html')

class AddPersonInfo(CreateView):
    model = PersonProfile
    fields = ['name','email']
    template_name = "personinfo/add_person.html"

    def get_context_data(self, **kwargs):
        context = super(AddPersonInfo, self).get_context_data(**kwargs)
        context['add_title_data'] = 'Add Personal Information'
        return context

class UpdateAddPersonInfo(UpdateView):
    model = PersonProfile
    fields = ['name','email']
    template_name = "personinfo/add_person.html"


class DeleteAddPersonInfo(DeleteView):
    template_name = "personinfo/delete_person.html"
    model = PersonProfile
    context_object_name = 'person'
    success_url = reverse_lazy('personinfo:view')

class ViewPersonInfo(ListView):

    def get_context_data(self, **kwargs):
        context = super(ViewPersonInfo, self).get_context_data(**kwargs)
        context['view_title_data'] = 'View Personal Information'
        return context

    template_name = "personinfo/view_person.html"
    context_object_name = 'person'
    def get_queryset(self):
        return PersonProfile.objects.all()


class SearchPersonInfo(ListView):
    template_name = "personinfo/search_person.html"
    context_object_name = 'person'
    search_blank = False
    def get_context_data(self, **kwargs):
        context = super(SearchPersonInfo, self).get_context_data(**kwargs)
        context['search_title_data'] = 'Search Personal Information'
        context['view_title_data'] = 'View Personal Information'
        if self.search_blank:
            context['is_blank'] = True
        return context

    def get_queryset(self):
        if 'username' in self.request.GET and 'useremail' in self.request.GET:
            if  self.request.GET['username']:
                u = self.request.GET['username']
                return PersonProfile.objects.filter(name__icontains=u)
            elif self.request.GET['useremail']:
                e = self.request.GET['useremail']
                return PersonProfile.objects.filter(email__icontains=e)
            else:
                self.search_blank = True
        else:
            return PersonProfile.objects.all()

class PersonInfolist(generics.ListCreateAPIView):
    queryset = PersonProfile.objects.all()
    serializer_class = PersonInfoSerializer
# # Create your views here.
