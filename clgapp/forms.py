


from django import forms
from .models import Department,Courses

class OrderForm(forms.Form):
    name = forms.CharField(max_length=100, label='Name')
    dob = forms.DateField(label='Date of Birth',)
    age = forms.IntegerField(label='Age')
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female')], label='Gender')
    phone_number = forms.CharField(max_length=15, label='Phone Number')
    mail_id = forms.EmailField(label='Email')
    address = forms.CharField(widget=forms.Textarea, label='Address')
    department = forms.ModelChoiceField(queryset=Department.objects.all(), label='Department')
    # courses = forms.ModelChoiceField(queryset=Courses.objects.all(), label='Course')
    courses = forms.ChoiceField(choices=[], label='Course', required=False)
    purpose = forms.ChoiceField(choices=[
        ('enquiry', 'For Enquiry'),
        ('order', 'Place Order'),
        ('return', 'Return')
    ], label='Purpose')
    materials_provided = forms.MultipleChoiceField(
        choices=[
            ('notebook', 'Notebook'),
            ('pen', 'Pen'),
            ('exam_papers', 'Exam Papers'),
        ],
        widget=forms.CheckboxSelectMultiple,
        label='Materials Provided'
    )



