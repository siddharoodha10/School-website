from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Teacher,Student,Attendance
from django.contrib.auth.models import User, auth
from school import models


# Create your views here.
def index(request):
	return render(request,"index.html")

def adminlogin(request):
	return render(request,"adminlogin.html")

def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/adminview")

        else:
            return redirect('index')
    else:
        return render(request,'index.html')
def adminview(request):
    teachercount=Teacher.objects.all().count()
    studentcount=Student.objects.all().count()
    mydict={
        "teachercount":teachercount,
        "studentcount":studentcount
    }
    return render(request,"admin.html",mydict)

def logout(request):
	return render(request,"index.html")

def teacherclick_view(request):
    return render(request,'teacherlogin.html')

def teacherloginD(request):
	return render(request,"teacherlogin.html")

def teacherlogin(request):
	if request.method=="POST":
		T_id=request.POST["T_id"]
		password=request.POST["password"]
		try:
			Teach=Teacher.objects.get(T_id=T_id)
		except:
			print("Wrong_ID")
			return render(request,"teacherlogin.html")
		if Teach.password==password:
			mydict={
			"first":Teach.F_name+" "+Teach.L_name,
			"salary":Teach.Sallary,
			"mobile":Teach.Mobile_no,
			"date":Teach.Join_date
			}
			return render(request,"Teacher.html",context=mydict)
		else:
			return render(request,"Wrong_password.html")
	else:
		return render(request,"index.html")

		
def studentloginD(request):
	return render(request,"studentlogin.html")
def studentlogin(request):
	if request.method=="POST":
		S_id=request.POST["S_id"]
		password=request.POST["password"]
		try:
			Stud=Student.objects.get(S_id=S_id)
		except:
			print("Wrong_ID")
			return render(request,"studentlogin.html")
		attendance=Attendance.objects.all()
		count=0
		for i in attendance:
			if i.S_id==Stud:
				count+=1
		if Stud.password==password:
			mydict={
			"first":Stud.F_name+" "+Stud.L_name,
			"fees":Stud.S_fee,
			"roll":Stud.S_id,
			"mobile":Stud.Contact,
			"att":count,

			}
			return render(request,"student.html",context=mydict)
		else:
			return render(request,"Wrong_password.html")
	else:
		return render(request,"index.html")




def newteacher(request):
    if request.method == 'POST':
        T_id = request.POST['T_id']
        F_name = request.POST['F_name']
        Sallary = request.POST['Sallary']
        Join_date = request.POST['Join_date']
        Mobile_no = request.POST['Mobile_no']
        password = request.POST['password']
        L_name = request.POST['L_name'] 
        
        teach =  Teacher.objects.create(T_id=T_id,F_name=F_name,L_name=L_name,Sallary=Sallary,Join_date=Join_date,Mobile_no=Mobile_no,password=password )
        teach.save()
        return render(request,'registered.html')

    else:
        return render(request, 'newteacher.html')

def newstudent(request):
    if request.method == 'POST':
        S_id = request.POST['S_id']
        F_name = request.POST['F_name']
        Class = request.POST['Class']
        Contact = request.POST['Contact']
        S_fee = request.POST['S_fee']
        password = request.POST['password']
        L_name = request.POST['L_name'] 
        
        std =  Student.objects.create(S_id=S_id,F_name=F_name,L_name=L_name,Contact=Contact, S_fee=S_fee,Class=Class,password=password)
        std.save()
        return render(request,'registeredS.html')

    else:
        return render(request, 'newstudent.html')



def succ(request):
	return render(request,"registered.html")

def succS(request):
	return render(request,"registeredS.html")

def attendance(request):
    if request.method == 'POST':
        S_id = Student.objects.get(S_id=request.POST['S_id'])
        Date = request.POST['Date']
        status = request.POST['status']
	
        atd =  Attendance.objects.create(S_id=S_id,Date=Date,status=status)
        atd.save()
        return render(request,'taken.html')

    else:
        return render(request, 'attendance.html')

def view_teacher(request):
    teach=Teacher.objects.all()
    return render(request,"view_teacher.html",{"teach":teach})

def view_student(request):
    stud=Student.objects.all()
    return render(request,"view_student.html",{"stud":stud})
def view_studentT(request):
    stud=Student.objects.all()
    return render(request,"view_studentT.html",{"stud":stud})
	