from django import forms

class TestForm(forms.Form):
    addr_in = forms.CharField(label='addr in', max_length=100)
    addr_in2 = forms.CharField(label='addr in', max_length=100)
    name_in = forms.CharField(label='addr in', max_length=100)
    name_in2 = forms.CharField(label='addr in', max_length=100)

class FileForm(forms.Form):
	YoN_CHOICES = (
	(1, ("yes")),
    (2, ("no"))
	)

	TYPE_CHOICES = (
    (1, ("CVS")),
    (2, ("Docx")),
    (3, ("Automatic"))
	)	

	data = forms.FileField()

	#status = forms.ChoiceField(choices = YoN_CHOICES, label="", initial='', widget=forms.Select(), required=True)
	#relevance = forms.ChoiceField(choices = TYPE_CHOICES, required=True)

	data_type = forms.ChoiceField(choices=TYPE_CHOICES)
	data_zip = forms.ChoiceField(choices=YoN_CHOICES)
	export = forms.ChoiceField(choices=YoN_CHOICES)
