"""
URL configuration for AttendanceWebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from Website.views import hello,webcam_view,verify_face,student_form_view,student_form_for_attendance

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',hello),
    path('webcam/',webcam_view),
    path('student-form/', student_form_view, name='student_form'),
    path('verify-face/', verify_face, name='verify_face'),
    path('check/',student_form_for_attendance, name='Attendance'),

]
