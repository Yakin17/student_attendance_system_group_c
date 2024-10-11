from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import CustomUser, Course, FacultyMember, Subjects, Student, Attendance


def admin_home(request):
    return render(request,'admin_templates/home_content.html')

def add_faculty_member(request):
    return render(request,'admin_templates/add_faculty_member_template.html')

def add_faculty_member_save(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("first_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        address=request.POST.get("address")

        try:
            user=CustomUser.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password,user_type=2)
            user.facultymember.address=address
            user.save()
            messages.success(request,"Successfully added")
            return HttpResponseRedirect("/add_faculty_member")
        except:
            messages.error(request,"Failed to add")
            return HttpResponseRedirect("/add_faculty_member")

def add_course(request):
    return render(request,'admin_templates/add_course_template.html')

def add_course_save(request):
    if request.method !="POST":
        return HttpResponseRedirect("Method not Allowed")
    else:
        coursename=request.POST.get("coursename")
        try:
            course_model=Course(course_name=coursename)
            course_model.save()
            messages.success(request,"Successfully Added")
            return HttpResponseRedirect("/add_course")
        except:
            messages.error(request,"Failed to add")
            return HttpResponseRedirect("/add_course")

def add_student(request):
    courses=Course.objects.all()
    return render(request,'admin_templates/add_student_template.html',{"courses":courses})

def add_student_save(request):
    if request.method !="POST":
        return HttpResponseRedirect("Method not Allowed")
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        course_id=request.POST.get("course")
        gender=request.POST.get("gender")
        address=request.POST.get("address")
        #try:
        user=CustomUser.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password,user_type=3)
        user.student.address=address
        course_obj=Course.objects.get(id=course_id)
        user.student.course_id=course_obj
        user.student.gender=gender
                #user.student.profile_pic="" part 5
        user.save()
        messages.success(request,"Successfully added")
        return HttpResponseRedirect("/add_student")
        #except:
        messages.error(request,"Failed to add")
        return HttpResponseRedirect("/add_student")

def add_subject(request):
    courses=Course.objects.all()
    fmembers=CustomUser.objects.filter(user_type=2)
    return render(request,"admin_templates/add_subject.html",{"courses":courses,"fmembers":fmembers})
def add_subject_save(request):
    if request.method!="POST":
        return render(request,"method not allowed")
    else:
        subject_name=request.POST.get("subjectname")
        course_id=request.POST.get("course")
        course=Course.objects.get(id=course_id)
        faculty_member_id=request.POST.get("faculty_member")
        faculty_member=CustomUser.objects.get(id=faculty_member_id)

        try:
            subject=Subjects(subject_name=subject_name,course_id=course,facultymember_id=faculty_member)
            subject.save()
            messages.success(request,"Successfully added")
            return HttpResponseRedirect("/add_subject")
        except:
            messages.error(request,"Failed to add")
            return HttpResponseRedirect("/add_subject")

def manage_faculty_member(request):
    fmembers=FacultyMember.objects.all()
    return render(request,'admin_templates/manage_faculty_member_template.html',{"fmembers":fmembers})

def manage_student(request):
    students= Student.objects.all()
    return render(request,'admin_templates/manage_student_template.html',{'students':students})

def manage_course(request):
    courses= Course.objects.all()
    return render(request,'admin_templates/manage_course.html',{'courses':courses})

def manage_subject(request):
    subjects=Subjects.objects.all()
    return render(request,'admin_templates/manage_subject_template.html',{'subjects':subjects})

def edit_faculty_member(request,facultymember_id):
    facultymember=FacultyMember.objects.get(admin=facultymember_id)
    return render(request,'admin_templates/edit_faculty_member_template.html',{'facultymember':facultymember})

def edit_faculty_member_save(request):
    if request.method!="POST":
        return render(request,"method not allowed")
    else:
        facultymember_id=request.POST.get("facultymember_id")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        username=request.POST.get("username")
        address=request.POST.get("address")

        try:
            user=CustomUser.objects.get(id=facultymember_id)
            user.first_name=first_name
            user.last_name=last_name
            user.email=email
            user.username=username
            user.save()

            facultymember_model=FacultyMember.objects.get(admin=facultymember_id)
            facultymember_model.address=address
            facultymember_model.save()
            messages.success(request,"Successfully Edited")
            return HttpResponseRedirect("/edit_faculty_member/"+facultymember_id)
        except:
            messages.error(request,"Failed to edit")
            return HttpResponseRedirect("/edit_faculty_member/"+facultymember_id)

def edit_student(request,student_id):
    student=Student.objects.get(admin=student_id)
    courses = Course.objects.all()
    return render(request,'admin_templates/edit_student_template.html',{'student':student,'courses':courses})

def edit_student_save(request):
    if request.method!="POST":
        return render(request,"method not allowed")
    else:
        student_id=request.POST.get("student_id")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        address = request.POST.get("address")
        course_id=request.POST.get("course")
        gender=request.POST.get("gender")

        try:
            user=CustomUser.objects.get(id=student_id)
            user.first_name=first_name
            user.last_name=last_name
            user.username=username
            user.email=email

            student=Student.objects.get(admin=student_id)
            student.address=address
            student.gender=gender
            course=Course.objects.get(id=course_id)
            student.course_id=course
            student.save()
            messages.success(request,"Successfully edited")
            return HttpResponseRedirect("/edit_student/"+student_id)
        except:
            messages.error(request,"Failed to edit")
            return HttpResponseRedirect("/edit_student/"+student_id)

def edit_course(request,course_id):
    course=Course.objects.get(id=course_id)
    return render(request,'admin_templates/edit_course_template.html',{'course':course})
def edit_course_save(request):
    if request.method !="POST":
        return HttpResponse("Method not allowed")
    else:
        course_id=request.POST.get("course_id")
        course_name=request.POST.get("course_name")
        try:
            cours=Course.objects.get(id=course_id)
            cours.course_name=course_name
            cours.save()
            messages.success(request, "Successfully edited")
            return HttpResponseRedirect("/edit_course/"+ course_id)
        except:
            messages.error(request, "Failed to edit")
            return HttpResponseRedirect("/edit_course/"+course_id)

def edit_subject(request,subject_id):
    subject=Subjects.objects.get(id=subject_id)
    courses=Course.objects.all()
    fmembers = CustomUser.objects.filter(user_type=2)
    return render(request,"admin_templates/edit_subject_template.html",{"subject":subject,'courses':courses,'fmembers':fmembers})

def edit_subject_save(request):
    if request.method !="POST":
        return HttpResponse("Method not allowed")
    else:
        subject_id=request.POST.get("subject_id")
        subject_name=request.POST.get("subject_name")
        course_id=request.POST.get("course_id")
        fmember_id=request.POST.get("fmember_id")

        try:
            subject=Subjects.objects.get(id=subject_id)
            subject.subject_name=subject_name
            cours_instance=Course.objects.get(id=course_id)
            subject.course_id=cours_instance
            fmember_instance=CustomUser.objects.get(id=fmember_id)
            subject.facultymember_id=fmember_instance
            subject.save()
            messages.success(request, "Successfully edited")
            return HttpResponseRedirect("/edit_subject/" + subject_id)
        except:
            messages.error(request, "Failed to edit")
            return HttpResponseRedirect("/edit_subject/" + subject_id)

def delete_faculty_member(request, facultymember_id):
    fmember = get_object_or_404(FacultyMember, admin__id=facultymember_id)

        # Supprimer le membre
    fmember.delete()
    return HttpResponseRedirect('/manage_faculty_member')


def delete_subject(request, subject_id):
    subject=Subjects.objects.filter(id=subject_id)
   # Supprimer le membre
    subject.delete()
    return render(request, 'admin_templates/manage_subject_template.html')

def delete_course(request, course_id):
    course=Course.objects.filter(id=course_id)
    course.delete()
    return HttpResponseRedirect('/manage_course')

def delete_student(request,student_id):
    student = get_object_or_404(Student, admin__id=student_id)
    student.delete()
    return HttpResponseRedirect("/manage_student")

def take_attendance(request):
    subjects = Subjects.objects.all()
    students = CustomUser.objects.filter(user_type=3)
    return render(request, 'admin_templates/take_attendance_template.html',
                  {'subjects': subjects, 'students': students})

def take_attendance_save(request):
    if request.method!="POST":
        return HttpResponse("method not allowed")
    else:
        date=request.POST.get("date")
        subject_id=request.POST.get("subjectname")
        student_ids=request.POST.getlist("student_id")


        if not date or not subject_id:
            messages.error(request,"Please fill all the fields")
            return HttpResponseRedirect('/take_attendance')

        subject = Subjects.objects.get(id=subject_id)
        for student_id in student_ids:

            student=CustomUser.objects.get(id=student_id)
            presence = request.POST.get(f'presence_{student_id}') # Récupération de la présence pour chaque étudiant
            Attendance.objects.create(subject_id=subject,student_id=student,attendance_date=date,attendance=presence)
        messages.success(request,"Attendance marked successfully")
        return HttpResponseRedirect('/take_attendance')

def view_attendance(request):
    attendances = Attendance.objects.all()
    subjects = Subjects.objects.all()
    attendance_records = None

    if request.method == "POST":
        subject_id = request.POST.get('subject')
        attendance_records = Attendance.objects.filter(subject_id=subject_id)

    return render(request, 'admin_templates/view_attendance.html',
                  {'attendances': attendances, 'subjects': subjects, 'attendance_records': attendance_records})

def edit_attendance(request,attendance_id,attendance_subject_id,attendance_date):
    attendances = Attendance.objects.filter(subject_id=attendance_subject_id, attendance_date=attendance_date)
    date_att = attendance_date
    subject = Subjects.objects.get(id=attendance_subject_id)

    att_id = attendance_id
    return render(request, 'admin_templates/edit_attendance_template.html',
                  {'attendances': attendances, 'subject': subject, 'date_att': date_att, 'att_id': att_id})

def edit_attendance_save(request):
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
                    return HttpResponseRedirect(reverse('edit_attendance', args=[attendance_id, subject_id, date_appel]))

        except:
                messages.error(request, "Failed to edit")
                return HttpResponseRedirect(
                    reverse('edit_attendance', args=[attendance_id, subject_id, date_appel]))

def eligible_for_exam(request,attendance_subject_id,attendance_student_id):
    attendances = Attendance.objects.filter(subject_id=attendance_subject_id)
    student = CustomUser.objects.filter(user_type=3)
    n_student = student.count()
    total_attendances = int(attendances.count())/n_student
    p_att = Attendance.objects.filter(subject_id=attendance_subject_id, attendance="P",
                                      student_id=attendance_student_id)
    stud_attendance = int(p_att.count())
    pourcentage_attendance = (stud_attendance * 100) / total_attendances
    return render(request,'admin_templates/eligible_for_exam.html',{'n_student':n_student,'total_attendances':total_attendances,'stud_attendance':stud_attendance,'pourcentage_attendance':pourcentage_attendance})