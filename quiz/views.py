from django.shortcuts import render

def startpage(request):
	return render(request, "quiz/start.html")

def question(request):
	return render(request, "quiz/question.html")

def completed(request):
	return render(request, "quiz/complete.html")
# Create your views here.
