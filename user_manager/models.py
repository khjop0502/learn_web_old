from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# 사용자 매니저 클래스 정의
class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        # 사용자 생성
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        # 비밀번호 설정 및 저장
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        # 슈퍼유저 생성
        user = self.create_user(
            email,
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


# 커스텀 사용자 모델 정의
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email",
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=20, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()  # 커스텀 사용자 매니저 할당

    USERNAME_FIELD = "email"  # 로그인에 사용할 필드 지정
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
