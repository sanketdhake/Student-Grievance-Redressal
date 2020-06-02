from django.db import models

from user.models import Student, Member

class Complain(models.Model):
	id = models.CharField(max_length = 12, primary_key = True)
	category = models.CharField(max_length = 30)
	sub_category = models.CharField(max_length = 30)
	brief = models.TextField()
	student = models.ForeignKey(Student, on_delete = models.CASCADE)
	solver = models.ForeignKey(Member, on_delete =  models.CASCADE, blank = True, null = True)
	solve_date = models.DateField()
