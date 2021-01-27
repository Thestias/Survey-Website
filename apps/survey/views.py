from django.shortcuts import render

# Create your views here.

def create_survey(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'survey/create_survey.html')
