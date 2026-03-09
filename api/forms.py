from django import forms

from core.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["color"]
