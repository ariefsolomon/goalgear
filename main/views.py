from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app_name': 'GoalGear',
        'student_name': 'Muhammad Arief Solomon',
        'student_class': 'PBP E',
    }
    return render(request, 'main.html', context)