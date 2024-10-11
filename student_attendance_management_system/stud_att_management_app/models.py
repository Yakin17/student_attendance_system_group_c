from email.policy import default
from symtable import Class
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class CustomUser(AbstractUser):
    user_type_data=((1,"ADM"),(2,"FMEMB"),(3,"Student"))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=10)
#I deleted the attributes name,pwd and email from student,admin and facult member because those informations already asked into default django user which is CustomUser
class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager() #models.Manager une classe fournie par Django qui vous permet d'interagir avec la base de données pour votre modèle. Elle fournit des méthodes pour récupérer, créer, mettre à jour et supprimer des instances de votre modèle.Objects est le nom par défaut de l'instance de models.Manager qui est associée à chaque modèle.


class FacultyMember(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()


class Course(models.Model):
    id=models.AutoField(primary_key=True)
    course_name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Subjects(models.Model):
    id=models.AutoField(primary_key=True)
    subject_name=models.CharField(max_length=100)
    course_id=models.ForeignKey(Course,on_delete=models.CASCADE,default=1)
    facultymember_id=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    gender=models.CharField(max_length=100)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE) #on_delete=models.CASCADE : Cela spécifie le comportement à adopter lorsque l'objet référencé (dans ce cas, un membre du corps professoral) est supprimé. Avec CASCADE, la suppression d'un membre du corps professoral entraînera la suppression de tous les objets qui y sont liés.
    course_id=models.ForeignKey(Course,on_delete=models.CASCADE)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects=models.Manager()


class Attendance(models.Model):
    id=models.AutoField(primary_key=True)
    subject_id=models.ForeignKey(Subjects,on_delete=models.DO_NOTHING)
    student_id=models.ForeignKey(CustomUser,on_delete=models.DO_NOTHING)
    attendance_date=models.DateField(auto_now_add=False)
    attendance=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()



@receiver(post_save,sender=CustomUser)
#Le décorateur @receiver relie un signal à une fonctio
#post_save : C'est un signal qui est envoyé après qu'un objet a été sauvegardé dans la base de données.
#sender : Cela spécifie quel modèle envoie le signal. Dans ce cas, CustomUser est le modèle qui déclenche le signal
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            Admin.objects.create(admin=instance)
        if instance.user_type==2:
            FacultyMember.objects.create(admin=instance)
        if instance.user_type==3:
            Student.objects.create(admin=instance,course_id=Course.objects.get(id=1),address="", gender="")

@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.admin.save()
    if instance.user_type==2:
        instance.facultymember.save()
    if instance.user_type==3:
        instance.student.save()
