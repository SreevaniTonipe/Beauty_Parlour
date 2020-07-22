from django.shortcuts import render
from . import forms

# Create your views here.
def home_view(request):
    return render(request,'testapp/base.html')

def Products_view(request):
    return render(request,'testapp/Products.html')

def Services_view(request):
    return render(request,'testapp/Services.html')

def Gallery_view(request):
    return render(request,'testapp/Gallery.html')

def ContactUs_view(request):
    form=forms.ContactForm()
    if request.method=='POST':
        form=forms.ContactForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return thanku_view(request)
#    contact_details=Contact.objects.all()
    return render(request,'testapp/ContactUs.html',{'form':form})

def thanku_view(request):
    return render(request,'testapp/thankyou.html')
