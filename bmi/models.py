from django.db import models

# Create your models here.
# 어떤 데이터를 어떤 형태로 DB에 저장할 것인가

# models.Model : ORM(Object Relation Mapping) 관련 기능을 가지고 있음
# ORM : 실제 데이터를 코드로 추상화해놓고 사용
# 데이터를 저장, 확인, 수정, 삭제하는 액션들을 models.Model에서 상속받아 사용


class BMI(models.Model):
    weight = models.FloatField()
    height = models.FloatField()
    bmi_score = models.FloatField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    # makemigrations bmi : 변경 사항을 추적하여 반영할 내용을 migration 파일로 만들어둔다.
    # migrate bmi 0001 : migration 파일을 실제 DB에 반영한다.

    def __str__(self):
        return "키: "+str(self.height)+" 체중: "+str(self.weight)+" BMI: "+str(self.bmi_score)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):

        self.bmi_score = self.weight / ((self.height/100)**2)

        super(BMI, self).save(force_insert, force_update, using, update_fields)
