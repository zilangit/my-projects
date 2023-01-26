from django.urls import path

from managementapp import views

urlpatterns=[
    path('reg',views.reg_fun,name='reg'), # it will redirect to register.html!
    path('regdata',views.regdata_fun), # it will create superuser account!
    path('',views.log_fun,name='log'),# it will display login.html!
    path('logdata',views.logdata_fun),
    path('home',views.home_fun,name='home'),#


    path('add_students',views.add_fun,name='add'),
    path('readdata',views.readdata_fun),


    path('display',views.diplay_fun,name='display'),#it will display.html table datd!

    path('update/<int:id>',views.update_fun,name='up'),#it will update the student details!

    path('delete/<int:id>',views.delete_fun,name='del'),#it will delete the data!

    path('log_out',views.logout_fun,name='log_out')
]