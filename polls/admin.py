from django.contrib import admin
from .models import Question
from .models import Choice

# Register your models here.
# admin.site.register(Question)
admin.site.register(Choice)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display=("question_text", "pub_date")
    list_filter = ["pub_date"]

    def get_readonly_fields(self, request, obj=None):
        return ["question_text"]