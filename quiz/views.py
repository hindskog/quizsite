# coding: utf-8

from django.shortcuts import render
from quiz.models import Quiz
from django.shortcuts import redirect

def startpage(request):
	context = {
	    	"quiz": Quiz.objects.get(name="puppy"),
	 }
	return render(request, "quiz/start.html", context)

def question(request, name, number):
	number = int(number)
	quiz = Quiz.objects.get(name = "puppy")
	questions = quiz.questions.all()
	if request.POST:
		answer = int(request.POST["answer"])
		saved_answers = {}
		if quiz.name in request.session:
			saved_answers = request.session[quiz.name]
		saved_answers[str(number)] = answer
		request.session[quiz.name] = saved_answers
		if questions.count() == number:
			return redirect("completed_page", quiz.name)
		else:
			return redirect("question_page", quiz.name, number+1)

	question = questions[number - 1]
	context = {
    		"question_number": number,
    		"question": question.question,
	    	"answer1": question.answer1,
    		"answer2": question.answer2,
	    	"quiz": quiz,
	}
	return render(request, "quiz/question.html", context)

def completed(request, name):
	quiz=Quiz.objects.get(name=name)
	questions = quiz.questions.all()
	saved_answers = request.session[name]
	num_correct_answers=0
	for counter, question in enumerate(questions):
		if question.correct == saved_answers[str(counter + 1)]:
			num_correct_answers += 1
	context = {
		"correct":num_correct_answers,
		"total":questions.count(),
	}
	return render(request, "quiz/complete.html", context)
# Create your views here.
