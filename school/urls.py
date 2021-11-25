
from django.urls import path
from . import views
urlpatterns=[
path("",views.index, name="index"),
path("index",views.index, name="index"),
path("adminlogin",views.adminlogin),
path("login",views.login,name="login"),
path('logout', views.logout,name='logout'),
path("adminview",views.adminview),
#path("admindashboard",views.admin_dashboard_view),

path('teacherclick', views.teacherclick_view),
path('teacherlogin', views.teacherloginD),
path("teacherloginD",views.teacherlogin),
path("newteacher",views.newteacher),
path("succ",views.succ),
path("view_teacher",views.view_teacher),

path("studentclick",views.studentloginD),
path("studentloginD",views.studentlogin),
path("newstudent",views.newstudent),
path("succS",views.succS),
path("view_student",views.view_student),
path("view_studentT",views.view_studentT),

path("attendance",views.attendance)


]