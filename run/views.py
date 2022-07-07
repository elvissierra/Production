from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from run.forms import PersonsForm

from django.urls import reverse_lazy

from .models import Person, Task, Technician, Tools, Area


class CustomLoginView(LoginView):
    template_name = 'run/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('main')#here i need to direct it to the main page

"""class RegisterView(FormView):
    template_name = 'run/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('')#direct to main
        return super(RegisterView, self).get(*args, **kwargs)"""

class PersonsPage():
    template_name = 'run/register_persons.html'
    context_object_name = 'persons'

    def reg_emp(request):
        if request.method == 'POST':
            form = PersonsForm(request.POST)
            if form.is_valid():
                try:
                    form.save()
                    return redirect('/main')
                except:
                    pass
        else:
            form = PersonsForm()
        return render(request, '---', {'form':form})

    #view all technicians in dept

class ToolPage():
    #display all tools and their info

class AreaPage():
    #display each area/ simply a visual of dept
        #functions- needs time/tools/technicians

class BackendArea():
    #displays the cost for each function --> area --> dept total cost
    #MAIN ATTRACTION
