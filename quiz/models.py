from django.db import models

class Quiz(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	def __unicode__(self):
		return self.name

class Question(models.Model):
	quiz = models.ForeignKey(Quiz, related_name="questions")
	question = models.CharField(max_length=100)
	answer1 = models.CharField(max_length=100)
	answer2 = models.CharField(max_length=100)
	correct = models.PositiveIntegerField()
	def __unicode__(self):
		return self.quiz.name + " / " + self.question

# Create your models here.
