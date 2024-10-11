"""
URL configuration for student_attendance_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from stud_att_management_app import views
from stud_att_management_app import AdminViews,FacultyMemberViews,StudentViews

urlpatterns = [
    path('eligible_for_exam/<str:attendance_subject_id>/<str:attendance_student_id>/',AdminViews.eligible_for_exam,name="eligible_for_exam"),
    path('student_view_attendance/<str:user_id>/',StudentViews.student_view_attendance,name="student_view_attendance"),
    path('edit_attendance_save',AdminViews.edit_attendance_save,name="edit_attendance_save"),
    path('edit_attendance/<str:attendance_id>/<str:attendance_subject_id>/<str:attendance_date>/',AdminViews.edit_attendance,name="edit_attendance"),
    path('view_attendance',AdminViews.view_attendance,name="view_attendance"),
    path('take_attendance_save',AdminViews.take_attendance_save,name="take_attendance_save"),
    path('take_attendance',AdminViews.take_attendance,name="take_attendance"),
    path('faculty_member_edit_attendance_save',FacultyMemberViews.faculty_member_edit_attendance_save),
    path('delete_student/<str:student_id>',AdminViews.delete_student,name="delete_student"),
    path('delete_course/<str:course_id>',AdminViews.delete_course,name="delete_course"),
    path('delete_subject/<str:subject_id>',AdminViews.delete_subject,name="subject_id"),
    path('delete_faculty_member/<str:facultymember_id>',AdminViews.delete_faculty_member,name="delete_faculty_member"),
    path('faculty_member_eligible_for_exam/<str:attendance_subject_id>/<str:attendance_student_id>/',FacultyMemberViews.faculty_member_eligible_for_exam,name="faculty_member_eligible_for_exam"),
    path('faculty_member_edit_attendance/<str:attendance_id>/<str:attendance_subject_id>/<str:attendance_date>/<str:attendance_student_id>/', FacultyMemberViews.faculty_member_edit_attendance, name='faculty_member_edit_attendance'),
    path('edit_subject_save',AdminViews.edit_subject_save,name="edit_subject_save"),
    path('edit_subject/<str:subject_id>',AdminViews.edit_subject,name="edit_subject"),
    path('edit_course_save',AdminViews.edit_course_save,name="edit_course_save"),
    path('edit_course/<str:course_id>',AdminViews.edit_course,name="edit_course"),
    path('faculty_member_view_attendance',FacultyMemberViews.faculty_member_view_attendance,name="faculty_member_view_attendance"),
    path('faculty_member_take_attendance_save',FacultyMemberViews.faculty_member_take_attendance_save,name="faculty_member_take_attendance_save"),
    path('faculty_member_take_attendance',FacultyMemberViews.faculty_member_take_attendance,name="faculty_member_take_attendance"),
    path('student_home',StudentViews.student_home,name="student_home"),
    path('faculty_member_home',FacultyMemberViews.faculty_member_home,name="faculty_member_home"),
    path('edit_student_save',AdminViews.edit_student_save,name="edit_student_save"),
    path('edit_student/<str:student_id>',AdminViews.edit_student,name="edit_student"),
    path('edit_faculty_member_save',AdminViews.edit_faculty_member_save,name="edit_faculty_member_save"),
    path('edit_faculty_member/<str:facultymember_id>',AdminViews.edit_faculty_member,name="edit_faculty_member"),
    path('manage_subject',AdminViews.manage_subject,name="manage_subject"),
    path('manage_course',AdminViews.manage_course,name="manage_course"),
    path('manage_student',AdminViews.manage_student,name="manage_student"),
    path('manage_faculty_member',AdminViews.manage_faculty_member,name="manage_faculty_member"),
    path('add_subject_save',AdminViews.add_subject_save,name="add_subject_save"),
    path('add_subject',AdminViews.add_subject,name="add_subject"),
    path('add_student_save',AdminViews.add_student_save,name="add_student_save"),
    path('add_student',AdminViews.add_student,name="add_student"),
    path('add_course_save',AdminViews.add_course_save,name="add_course_save"),
    path('add_course',AdminViews.add_course,name="add_course"),
    path('add_faculty_member_save',AdminViews.add_faculty_member_save,name="add_faculty_member_save"),
    path('add_faculty_member',AdminViews.add_faculty_member,name="add_faculty_member"),
    path('logout_user',views.logout_user,name="logout_user"),
    path('get_user_details',views.GetUserDetails,name="get_user_details"),
    path('doLogin',views.doLogin,name="doLogin"),
    path('',views.FLoginPage,name=""),
    path('demo/',views.showDemoPage,name="demo"),
    path('admin/', admin.site.urls,name="admin"),
    path('admin_home', AdminViews.admin_home,name="admin_home"),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
