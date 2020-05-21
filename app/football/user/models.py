from django.db import models
from django.core.validators import MinLengthValidator

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext as _


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=False, is_admin=False):
        if not email:
            raise ValueError(_("users nust have email"))
        user = self.model(
            email=UserManager.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, is_active=False, is_admin=False):
        user = self.create_user(email,password)
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)

        return user




class MyUsermodel(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, null=True, unique=True)
    id = models.AutoField(primary_key=True)
    email = models.EmailField(_("email"), max_length=254, unique=True)
    password = models.CharField(MinLengthValidator(8, message=_("password must have more than 8 charactors")), max_length=254)
    date_of_birth = models.DateField(null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'email'


    def get_full_name(self):
        pass

    def get_short_name(self):
        pass

    def has_perm(self, perm, obj=None):
       return self.is_admin

    def has_module_perms(self, app_label):
       return self.is_admin

