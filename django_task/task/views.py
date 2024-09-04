from django.shortcuts import render, redirect
from rest_framework import generics
from .models import Task
from rest_framework.views import APIView
from .serializers import TaskSerializer
class TaskListView(generics.ListAPIView):
	queryset = Task.objects.all()
	serializer_class = TaskSerializer

def task_list(request):
	if request.method == "GET":
		tasks = Task.objects.filter(complete=False).order_by("-created_at")
		return render(request, "task/task_list.html", {"tasks": tasks})


class TaskDetailView(generics.RetrieveAPIView):
	queryset = Task.objects.all()
	serializer_class = TaskSerializer
	lookup_field = "pk"

class TaskCreateView(generics.CreateAPIView):
	queryset = Task.objects.all()
	serializer_class = TaskSerializer


class TaskUpdateView(generics.UpdateAPIView):
	queryset = Task.objects.all()
	serializer_class = TaskSerializer
	lookup_field = "pk"

class TaskDeleteView(generics.DestroyAPIView):
	queryset = Task.objects.all()
	serializer_class = TaskSerializer
	lookup_field = "pk"

def task_delete(request,pk):
	task = Task.objects.get(pk=pk)
	task.delete()
	return redirect("task_list")

