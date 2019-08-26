from django.shortcuts import render , HttpResponse ,redirect
from django.contrib.auth.forms import UserCreationForm

from django.template import loader
from .models import Movies
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django import forms

class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
# Create your views here.

def home(request):
	return render(request, 'homepage/home.html')

#@login_required(login_url="/homepage/login")
def loginhome(request):
	data=Movies.objects.all()
	if request.user.is_authenticated:
		print("auth")
		return render(request, 'homepage/loginhome.html',{'data':data})
	else:
		return redirect('/homepage/')
	
	
	print("hi1")
	#print(username)
	#i=request.POST.getlist('username')
	#p=request.POST.getlist('password')
	#if not i:
	#	return redirect('/homepage/')
	#else:
			
	#	return render(request, 'homepage/loginhome.html',{'data':data,'user':i})
	

def register(request):
	if request.method =='POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/homepage/sreg')
		else:
			return render(request,'homepage/failreg.html')

	else:
		form=UserCreationForm()
		args = {'form':form}
		return render(request,'homepage/register.html',args)

def total(request):
	sum=0
	data=Movies.objects.all()
	count=1
	m=[1,2,3,4,5,6,7,8,9,10]
	#inp_value = request.GET.get('key', 'This is a default value')
	i=request.POST.getlist('key')
	
	for movie in data:
		sum=int(movie.price)*int(i[count-1])+sum
		
		#m[count] = Movies.objects.get(pk= count)
		if (movie.seats<int(i[count-1])):
			return render(request, 'homepage/total.html',{'sum':"Insufficient Seats"})
		movie.seats=movie.seats-int(i[count-1])
		count=count+1
	count=1
	sum=0
	for movie in data:
		sum=int(movie.price)*int(i[count-1])+sum
		
		#m[count] = Movies.objects.get(pk= count)
		if (movie.seats<int(i[count-1])):
			return render(request, 'homepage/total.html',{'sum':"Insufficient Seats"})
		movie.seats=movie.seats-int(i[count-1])
		movie.save()
		count=count+1
	return render(request, 'homepage/total.html',{'sum':sum})
