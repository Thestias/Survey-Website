from django.contrib import admin
from .models import Survey, Submission, Answer, Option
# Register your models here.

admin.site.register(Survey)
admin.site.register(Submission)
admin.site.register(Answer)
admin.site.register(Option)
