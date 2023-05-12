
from django.shortcuts import render, redirect,get_object_or_404
from .models import Business
from .forms import BusinessForm
from django.urls import reverse_lazy
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.views.generic import ListView


# Business Model 

def create_business(request):
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('business_list')
    else:
        form = BusinessForm()

    context = {'form': form}
    return render(request, 'business/business_add.html', context)


def update_business(request, pk):
    business = get_object_or_404(Business, pk=pk)

    if request.method == 'POST':
        form = BusinessForm(request.POST, instance=business)
        if form.is_valid():
            form.save()
            return redirect('business_list')
    else:
        form = BusinessForm(instance=business)

    context = {'form': form, 'business': business}
    return render(request, 'business/business_edit.html', context)


def delete_business(request, pk):
    business = get_object_or_404(Business, pk=pk)

    if request.method == 'POST':
        business.delete()
        return redirect('business_list')

    context = {'business': business}
    return render(request, 'business/business_delete.html', context)


# Basic pages
def contact (request):
    return render(request,'contact.html')

def about (request):
    return render(request,'about.html')

def home (request):
    decors=Business.objects.filter(type='ديكور')
    plumbing=Business.objects.filter(type='السباكة')
    elecs=Business.objects.filter(type='الكهربائيات')
    others=Business.objects.filter(type='أخرى')
    return render(request,'home1.html',{'decors':decors,'plumbings':plumbing,'elecs':elecs,'others':others,"title":"title"})

def dashboard (request):
    username = None
    business=Business.objects.all()
    if request.user.is_authenticated:
        username = request.user.username
        if request.method=='GET':
            return render(request, 'business/business_list.html', {'object_list':business})
        else:
            business=BusinessForm(request.POST)
            business.save(commit=False)
            decors=Business.objects.all()
            return render(request, 'business/dashboard.html', {'object_list':decors})
    else:
        return redirect('home')
    
    
    
    
    # Another way using views
# class BusinessCreateView(CreateView):
#     model = Business
#     form_class = BusinessForm
#     template_name = 'business/business_add.html'
#     success_url = reverse_lazy('business_list')

# class BusinessUpdateView(UpdateView):
#     model = Business
#     form_class = BusinessForm
#     template_name = 'business/business_edit.html'
#     success_url = reverse_lazy('business_list')

# class BusinessDeleteView(DeleteView):
#     model = Business
#     template_name = 'business/business_delete.html'
#     success_url = reverse_lazy('business_list')
# class BusinessListView(ListView):
#     model = Business
#     template_name = 'business/business_list.html'

#     def get_form(self):
#         if self.request.method == 'POST':
#             return BusinessForm(self.request.POST)
#         else:
#             return BusinessForm()

    
