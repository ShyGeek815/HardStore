from django import forms
from .models import HardStore_record, Record

# Форма добавления записи HardStore_record
class AddProductForm(forms.ModelForm):
	name_category = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Артикул", "class":"form-control"}), label="")
	name_product = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Наименование товара", "class":"form-control"}), label="")
	brand = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Бренд", "class":"form-control"}), label="")
	model_product = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Модель", "class":"form-control"}), label="")
	warranty = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Гарантия", "class":"form-control"}), label="")
	contry_product = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Страна производитель", "class":"form-control"}), label="")
	price_product = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Цена", "class":"form-control"}), label="")
	description_product = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Описание", "class":"form-control"}), label="")

	class Meta:
		model = HardStore_record
		exclude = ("user",)


# Форма добавления записи Record
class AddRecordForm(forms.ModelForm):
	familia = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Фамилия", "class":"form-control"}), label="")
	imya = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Имя", "class":"form-control"}), label="")
	otchestvo = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Отчество", "class":"form-control"}), label="")
	email = forms.EmailField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Электронный адрес", "class":"form-control"}), label="")
	phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Телефон", "class":"form-control"}), label="")
	male_choice = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Пол", "class":"form-control"}), label="")
	date_of_birth = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Дата рождения", "class":"form-control"}), label="")
	#date_pockypki = forms.DateField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Дата последней покупки", "class":"form-control"}), label="")

	class Meta:
		model = Record
		exclude = ("user",)