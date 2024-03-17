from django.db import models

class Wiki(models.Model):
    subject = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)    # auto_now_add는 최초 저장 시에만 적용, ineditable
    updated_at = models.DateTimeField(auto_now=True)        # auto_now는 객체가 저장될 때마다 적용