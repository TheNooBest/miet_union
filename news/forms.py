from django_summernote.widgets import SummernoteWidget

from .models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
        widgets = {
            'text': SummernoteWidget(
                attrs={'summernote': {'width': '100%', 'height': '350px'}}),
        }
