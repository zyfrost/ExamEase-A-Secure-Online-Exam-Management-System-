from django.contrib import admin
from .models import Exam_Model
from .question_models import Question_DB
from .questionpaper_models import Question_Paper
from django.contrib import admin
from .models import PDFUpload



admin.site.register(Question_DB)
admin.site.register(Question_Paper)
#admin.site.register(Special_Students)
admin.site.register(Exam_Model)


@admin.register(PDFUpload)
class PDFUploadAdmin(admin.ModelAdmin):
    list_display = ('professor', 'uploaded_at', 'processed', 'total_questions_found', 'total_questions_added')
    list_filter = ('processed', 'uploaded_at')
    search_fields = ('professor__username',)