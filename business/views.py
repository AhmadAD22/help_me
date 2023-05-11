from django.views.generic import ListView


from django.shortcuts import render, redirect, get_object_or_404
from .models import Business
from .forms import BusinessForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import logout


class BusinessCreateView(CreateView):
    model = Business
    form_class = BusinessForm
    template_name = 'business_add.html'
    success_url = reverse_lazy('business_list')

class BusinessUpdateView(UpdateView):
    model = Business
    form_class = BusinessForm
    template_name = 'business_edit.html'
    success_url = reverse_lazy('business_list')

class BusinessDeleteView(DeleteView):
    model = Business
    template_name = 'business_delete.html'
    success_url = reverse_lazy('business_list')
class BusinessListView(ListView):
    model = Business
    template_name = 'business_list.html'

    def get_form(self):
        if self.request.method == 'POST':
            return BusinessForm(self.request.POST)
        else:
            return BusinessForm()


def home (request):
    decors=Business.objects.filter(type='ديكور')
    plumbing=Business.objects.filter(type='السباكة')
    elecs=Business.objects.filter(type='الكهربائيات')
    others=Business.objects.filter(type='أخرى')
       
    return render(request,'business/home1.html',{'decors':decors,'plumbings':plumbing,'elecs':elecs,'others':others,"title":"title"})

def contact (request):
    return render(request,'business/contact.html')


def about (request):
    return render(request,'business/about.html')


def dashboard (request):
    username = None
    decors=Business.objects.all()
    if request.user.is_authenticated:
        username = request.user.username
        if request.method=='GET':
            
            return render(request, 'business/dashboard.html', {'username': username,'object_list':decors,'form':BusinessForm()})
        else:
            business=BusinessForm(request.POST)
            business.save(commit=False)
            decors=Business.objects.all()
            return render(request, 'business/dashboard.html', {'username': username,'object_list':decors,'form':BusinessForm()})
    else:
        return render(request, 'business/home1.html', {'username': username,'object_list':decors,'form':BusinessForm()})
    
def logout_user(request):
    logout(request)
    return redirect('home')