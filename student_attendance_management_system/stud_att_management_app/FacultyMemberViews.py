from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from .models import Subjects, Student, FacultyMember, Attendance, CustomUser
from django.contrib import messages


def faculty_member_home(request):
    return render(request,'faculty_member_templates/home_content.html')

def faculty_member_take_attendance(request):
    subjects = Subjects.objects.all()
    students = CustomUser.objects.filter(user_type=3)
    return render(request, 'faculty_member_templates/faculty_member_take_attendance_template.html',
                  {'subjects': subjects, 'students': students})

def faculty_member_take_attendance_save(request):
    if request.method!="POST":
        return HttpResponse("method not allowed")
    else:
        date=request.POST.get("date")
        subject_id=request.POST.get("subjectname")
        student_ids=request.POST.getlist("student_id")


        if not date or not subject_id:
            messages.error(request,"Please fill all the fields")
            return HttpResponseRedirect('/faculty_member_take_attendance')

        subject = Subjects.objects.get(id=subject_id)
        for student_id in student_ids:

            student=CustomUser.objects.get(id=student_id)
            presence = request.POST.get(f'presence_{student_id}') # Récupération de la présence pour chaque étudiant
            Attendance.objects.create(subject_id=subject,student_id=student,attendance_date=date,attendance=presence)
        messages.success(request,"Attendance marked successfully")
        return HttpResponseRedirect('/faculty_member_take_attendance')

def faculty_member_view_attendance(request):
    attendances= Attendance.objects.all()
    subjects = Subjects.objects.all()
    attendance_records=None

    if request.method=="POST":
        subject_id = request.POST.get('subject')
        attendance_records=Attendance.objects.filter(subject_id=subject_id)

    return render(request,'faculty_member_templates/faculty_member_view_attendance.html',{'attendances':attendances,'subjects':subjects,'attendance_records':attendance_records})

def faculty_member_edit_attendance(request,attendance_id,attendance_subject_id,attendance_date):
    attendances=Attendance.objects.all()
    student=CustomUser.objects.filter(user_type=3)
    n_student=student.count()
    date_att=attendance_date
    subject=Subjects.objects.get(id=attendance_subject_id)

    att_id=attendance_id
    return render(request,'faculty_member_templates/faculty_member_edit_attendance_template.html',{'n_student':n_student,'attendances':attendances,'subject':subject,'date_att':date_att,'att_id':att_id})

def faculty_member_edit_attendance_save(request):
    if request.method!="POST":
        return render(request,"method not allowed")
    else:
        try:
            attendance_id=request.POST.get("attendance_id")
            subject_id=request.POST.get("subject_id")
            date_appel=request.POST.get("date_appel")


            # la j'obtiens tous les IDs d'étudiants à partir de la requête
            student_ids = request.POST.getlist('student_id')


            # je arcoure chaque étudiant et mettez à jour la présence
            for student_id in student_ids:
                presences = request.POST.getlist('presence')
                for presence in presences:
                    # je mets à jour la présence pour chaque étudiant
                    attendance = Attendance.objects.get(student_id=student_id, attendance_date=date_appel, subject_id=subject_id)
                    attendance.attendance = presence
                    attendance.save()
                    messages.success(request, "Successfully edited")
                    return HttpResponseRedirect(reverse('faculty_member_edit_attendance', args=[attendance_id, subject_id, date_appel]))

        except:
                messages.error(request, "Failed to edit")
                return HttpResponseRedirect(
                    reverse('faculty_member_edit_attendance', args=[attendance_id, subject_id, date_appel]))

def faculty_member_eligible_for_exam(request,attendance_subject_id,attendance_student_id):
    attendances = Attendance.objects.filter(subject_id=attendance_subject_id)
    student = CustomUser.objects.filter(user_type=3)
    n_student = student.count()
    total_attendances = int(attendances.count())/n_student
    p_att = Attendance.objects.filter(subject_id=attendance_subject_id, attendance="P",
                                      student_id=attendance_student_id)
    stud_attendance = int(p_att.count())
    pourcentage_attendance = (stud_attendance * 100) / total_attendances
    return render(request,'faculty_member_templates/eligible_for_exam.html',{'n_student':n_student,'total_attendances':total_attendances,'stud_attendance':stud_attendance,'pourcentage_attendance':pourcentage_attendance})
