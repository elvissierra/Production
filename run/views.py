from msilib.schema import ListView
from pyexpat import model
from urllib import request
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.views import View
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Person, Task, Technician, Tools, Area

#login
class CustomLoginView(LoginView):
    template_name = 'run/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('main')#here i need to direct it to the main page

#register new supervisors/managers
class RegisterView(FormView):
    template_name = 'run/register_super.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('main')#direct to main
        return super(RegisterView, self).get(*args, **kwargs)


#add new people
class RegisterPersons(LoginRequiredMixin, FormView):
    template_name = 'run/register_persons.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('register_persons')

    def valid_register(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPersons, self).valid_register(form)
    
"""

#view all technicians-> info and what area they belong to
class TechPage(ListView):
    model = Technician

    def show_techs(self, *args, **kwargs):
        techs = Technician.objects.all()
        return render(self, 'technicians.html', {'techs': techs})


#display all tools and their info-> cost/ name/ areas their used/ description
class ToolPage():

#display each area- functions/ time/tools/technicians | add tools to area
class AreaPage():
"""    
class ListView(View):
    model = None
    template_name = None
    objects = None

    def get(self, request, *args, **kwargs):
        context = {'object_list': self.objects}
        return render(request, self.template_name, context)
    

#MAIN ATTRACTION | displays the cost for each function --> area --> dept total cost
class Main(ListView):
    model = Technician
    template_name = 'run/main.html'
    objects = model.objects.all()