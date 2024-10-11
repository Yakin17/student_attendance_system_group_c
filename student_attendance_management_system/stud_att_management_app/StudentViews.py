from django.shortcuts import render

from .models import Attendance,Subjects


def student_home(request):
    return render(request,'student_templates/home_content.html')

def student_view_attendance(request,user_id):
    attendances = Attendance.objects.filter(student_id=user_id)
    subjects = Subjects.objects.all()
    attendance_records = None

    if request.method == "POST":
        subject_id = request.POST.get('subject')
        attendance_records = Attendance.objects.filter(subject_id=subject_id,student_id=user_id)

    return render(request, 'student_templates/student_view_attendance.html',
                  {'attendances': attendances, 'subjects': subjects, 'attendance_records': attendance_records})