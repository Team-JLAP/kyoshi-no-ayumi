from django import forms
from .models import Rating

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['semester', 'rate', 'attendance', 'grade', 'comment']
        
    gradeChoices = (
            ('A+', 'A+'), ('A', 'A'), ('A-', 'A-'),
            ('B+', 'B+'), ('B', 'B'), ('B-', 'B-'),
            ('C+', 'C+'), ('C', 'C'), ('C-', 'C-'),
            ('D', 'D'), ('F', 'F'), ('N', 'N'), ('Other', 'Other')
        )
    attendanceChoices = (
            (True, 'YES'),
            (False, 'NO'),
            (None, 'Not Sure'),
        )

    widgets = {
        'semester': forms.TextInput(
            attrs={'class': 'text-red-400', 'placeholder': 'Fall 2022'}
        ),
        'rate': forms.NumberInput(
            attrs={'class': 'border', 'min': 1, 'max': 5, 'value': 3}
        ),
        'attendance': forms.Select(
            attrs={'class': 'border'}, choices=attendanceChoices
        ),
        'grade': forms.Select(
            attrs={'class': 'border'}, choices=gradeChoices
        ),
        'comment': forms.TextInput(
            attrs={'class': 'border', 'placeholder': 'Write you comment'}
        ),
    }