from django.db import models
import datetime

# Create your models here.
class Task(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	complete = models.BooleanField(default=False)
	due_date = models.DateField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title
	
	class Meta():
		ordering = ["-created_at"]
	
	def is_overdue(self):
		return self.due_date < datetime.date.today()

