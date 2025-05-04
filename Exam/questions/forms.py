from django import forms
from .models import PDFUpload

class PDFUploadForm(forms.ModelForm):
    class Meta:
        model = PDFUpload
        fields = ['pdf_file']
        widgets = {
            'pdf_file': forms.FileInput(attrs={'class': 'form-control'})
        }
        
class QuestionBulkActionForm(forms.Form):
    action = forms.ChoiceField(
        choices=[
            ('add_to_db', 'Add to Question Database'),
            ('add_to_paper', 'Add to Question Paper')
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    question_paper = forms.ChoiceField(
        choices=[],
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    def __init__(self, professor, *args, **kwargs):
        super(QuestionBulkActionForm, self).__init__(*args, **kwargs)
        from .questionpaper_models import Question_Paper
        # Populate question papers dropdown with professor's papers
        papers = Question_Paper.objects.filter(professor=professor)
        self.fields['question_paper'].choices = [(p.id, p.qPaperTitle) for p in papers]