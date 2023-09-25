from django import forms
from .models import Categories, News


class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = "__all__"


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"
        widgets = {
            "categories": forms.CheckboxSelectMultiple(),
            "created_at": forms.DateInput(attrs={"type": "date"}),
        }
