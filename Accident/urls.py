"""Accident_Detection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.loginn),
    path('login_post',views.login_post),
    path('admin_home',views.admin_home),
    path('hospital_home',views.hospital_home),
    path('policestation_home',views.policestation_home),
    path('logout',views.logout),
    path('view_registered_hospital',views.view_registered_hospital),
    path('registered_hospital_approve/<id>/<email>',views.registered_hospital_approve),
    path('registered_hospital_reject/<id>/<email>',views.registered_hospital_reject),
    path('view_approved_hospital',views.view_approved_hospital),
    path('view_doctorin_hospital',views.view_doctorin_hospital),
    path('view_registered_policestation',views.view_registered_policestation),
    path('registered_policestation_approve/<id>/<email>',views.registered_policestation_approve),
    path('registered_policestation_reject/<id>/<email>',views.registered_policestation_reject),
    path('view_approved_policestation',views.view_approved_policestation),
    path('view_registered_user',views.view_registered_user),
    path('view_accident_detection',views.view_accident_detection),

#########################################################################################################

    path('register',views.register),
    path('register_post',views.register_post),
    path('add_doctor',views.add_doctor),
    path('add_doctor_post',views.add_doctor_post),
    path('view_doctor',views.view_doctor),
    path('update_doctor/<id>',views.update_doctor),
    path('update_doctor_post/<id>',views.update_doctor_post),
    path('delete_doctor/<id>',views.delete_doctor),
    path('fecility_add',views.fecility_add),
    path('fecility_add_post',views.fecility_add_post),
    path('feciity_view',views.feciity_view),
    path('fecility_update/<id>',views.fecility_update),
    path('fecility_update_post/<id>',views.fecility_update_post),
    path('fecility_delete/<id>',views.fecility_delete),
    path('update_accident_report',views.update_accident_report),
    path('update_report/<id>/<aid>',views.update_report),
    path('view_accident_detections',views.view_accident_detections),
    path('view_policestation',views.view_policestation),

#######################################################################################

    path('police_registration',views.police_registration),
    path('police_registration_post',views.police_registration_post),
    path('view_nearby_hospital',views.view_nearby_hospital),
    path('view_accidents',views.view_accidents),
    path('Notitfication_to_hospital/<lattitude>/<longitude>',views.Notitfication_to_hospital),
    path('send_email/<email>/<lattitude>/<longitude>',views.send_email),

########################################################################

    # User module(Android)

    path('android_login',views.android_login),
    path('android_user_registration',views.android_user_registration),
    path('android_view_nearby_hospital',views.android_view_nearby_hospital),
    path('android_view_doctor',views.android_view_doctor),
    path('android_view_fecility',views.android_view_fecility),
    path('android_view_nearby_policestation',views.android_view_nearby_policestation),
    path('android_view_accident_detection',views.android_view_accident_detection),
    path('android_delete_accident',views.android_delete_accident),
    path('accident_detection',views.accident_detection),

]
