from django.shortcuts import render, redirect
from .models import Training, Project
from django.contrib.auth.decorators import login_required


def dashboard(request):
    return render(request, 'students/dashboard.html')


def add_training(request):
    if request.method == 'POST':
        if request.POST['company_name'] and request.POST['role'] and request.POST['place'] and request.POST['description']:
            training = Training()
            training.company_name = request.POST['company_name']
            training.role = request.POST['role']
            training.place = request.POST['place']
            training.description = request.POST['description']
            training.start_date = request.POST['start_date']
            training.end_date = request.POST['end_date']
            training.student_id = request.user
            training.save()
            # return redirect('training')
            return redirect('home')

        else:
            return render(request, 'students/add_training.html', {'error': 'All fields are required!'})

    else:
        return render(request, 'students/add_training.html')


def add_project(request):
    if request.method == "POST":
        if request.POST['project_name'] and request.POST['description']:
            project = Project()
            project.project_name = request.POST['project_name']
            project.student_id = request.user
            project.description = request.POST['description']
            project.start_date = request.POST['start_date']
            project.end_date = request.POST['end_date']
            project.save()

            return render(request, 'students/dashboard.html')

        else:
            return render(request, 'students/add_project.html', {'error': 'All fields are required!'})

    else:
        trainings = Training.objects
        return render(request, 'students/add_project.html', {'trainings': trainings})


def all_projects(request):
    projects = Project.objects
    return render(request, 'students/all_projects.html', {'projects': projects})
