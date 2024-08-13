from django.db import models
# 부모 유저 클래스, 유저를 생성할 때 사용하는 시스템, 유저의 권한
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from .constant import USER_ROLE

# Create your models here.

# 고객 모델 생성
class CustomManager(BaseUserManager):
    use_in_migrations = True # 무조건 사용
    
    def create_user(self, username, password = None, email = None, role = None): #상속받은 부모 클래스에 create_user가 있다 -> 오버라이딩
        if not email:
            raise ValueError("must have your email")
        
        user = self.model(
            email = self.normalize_email(email)
            , role = role if role in USER_ROLE.__members__ else USER_ROLE.CUST.name
            , username = username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
# 고객 테이블(모델)
# class Custom(AbstractBaseUser, PermissionsMixin):
class Custom(AbstractBaseUser, PermissionsMixin):
    # 고객 모델 불러오기(attribute)
    objects = CustomManager()

    username = models.CharField(max_length=200, unique=True, null=False)
    email = models.EmailField(max_length=200, unique=True, null=False)
    #password는 AbstractBaseUser에서 받아올 거임
    role = models.CharField(max_length=10, null=False, default=USER_ROLE.CUST.name)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "custom" # SQL에 테이블 명을 명시할 때 사용

    is_superuser = models.BooleanField(default=False)    
    s_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    # 로그인 시 사용할 유저 컬럼
    # USERNAME = "username" <- 이거 실수
    USERNAME_FIELD = "username"
    # null이 아닌 필수로 꼭 필요한 것
    REQUIRED_FIELDS = ["email", "role"]