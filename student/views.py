from django.shortcuts import render, HttpResponseRedirect
from .forms import UserForm
from .models import User
# Create your views here.


def add_show(request):
    student = User.objects.all()
    if request.method == 'POST':
        fm = UserForm(request.POST)
        if fm.is_valid():
            fm.save()
            fm = UserForm()

    else:
        fm = UserForm()
    context = {
        'form': fm,
        'student': student
    }
    return render(request, 'student/addshow.html', context)

def delete(request, pk):
    if request.method == 'POST':
        var = User.objects.get(pk=pk)
        var.delete()
        return HttpResponseRedirect('/')

def update(request,pk):
    if request.method =='POST':
        print("post method")
        var = User.objects.get(pk=pk)
        form = UserForm(request.POST, instance=var)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

        
    else:
        print('not post')
        var = User.objects.get(pk=pk)
        form = UserForm(instance=var)

    context = {
        'form' : form
    }
    return render(request, 'student/update.html', {'form' : form})


