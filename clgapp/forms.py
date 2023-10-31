


from django import forms


from .models import Department, Courses



class Orderform(forms.Form):
        name = forms.CharField(max_length=100, label='Name')
        dob = forms.DateField(label='Date of Birth',)
        age = forms.IntegerField(label='Age')
        gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female')], label='Gender')
        phone_number = forms.CharField(max_length=15, label='Phone Number')
        mail_id = forms.EmailField(label='Email')
        address = forms.CharField(widget=forms.Textarea, label='Address')


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
        department=forms.ModelChoiceField(queryset=Department.objects.all(),
                                      widget=forms.Select(attrs={"hx-get":"load_courses","hx-target":"#id_courses"}))

        courses=forms.ModelChoiceField(queryset=Courses.objects.none())

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            if "department" in self.data:
                department_id=int(self.data.get("department"))
                self.fields["courses"].queryset=Courses.objects.filter(department_id=department_id)