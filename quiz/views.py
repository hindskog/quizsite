# coding: utf-8

from django.shortcuts import render

quizzes = {
	"klassiker": {
   		"name": u"Klassiska böcker",
	   	"description": u"Hur bra kan du dina klassiker?"
	},
	"fotboll": {
	   	"name": u"Största fotbollslagen",
	   	"description": u"Kan du dina lag?"
	},
	"kanda-hackare": {
	    	"name": u"Världens mest kända hackare",
	    	"description": u"Hackerhistoria är viktigt, kan du den?"	},
}



def startpage(request):
	context = {
		"quizzes": quizzes,
	}
	return render(request, "quiz/start.html", context)

def question(request, number):
	context = {	
	"question_number": number,
	"question": u"Hur många bultar har ölandsbron?",
	"answer1": u"12",
	"answer2": u"66 400",
	"answer3": u"7 428 954",
	}
	return render(request, "quiz/question.html", context)

def completed(request, slug):
	context = {
	"correct": 12,
	"total" :  20,
	"quiz_slug": slug,
	}
	return render(request, "quiz/complete.html", context)
# Create your views here.
