from django.shortcuts import render
from .forms import ResumeForm
from .models import Resume
from django.views import View

# Create your views here.
class HomeView(View):
    def get(self,request):
        form=ResumeForm()
        return render(request, 'testapp/home.html', {'form':form})
    def Post(self, request):
        form=ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'testapp/home.html', {'form':form})
class CandidateView(View):
    def get(self, request):
        return render(request, 'testapp/candidate.html')         
        
