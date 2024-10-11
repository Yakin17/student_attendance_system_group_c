from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend



class EmailBackEnd(ModelBackend): #La classe hérite de ModelBackend, qui est le backend d'authentification par défaut de Django
    def authenticate(self,username=None,password=None,**kwargs):
        UserModel=get_user_model() #get_user_model() est une fonction fournie par Django qui permet de récupérer le modèle utilisateur actuellement utilisé dans votre projet.
        try:
            user=UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
            return None