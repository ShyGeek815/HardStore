from django.shortcuts import render, redirect
# импортирую систему аутинтификации 
from django.contrib.auth import authenticate, login, logout
# импортирую сообщения (о входе/выходе в систему)
from django.contrib import messages
from .models import Record
from .models import HardStore_record
from .models import Storehouse
from .models import Employee
from .forms import AddProductForm, AddRecordForm

def home(request):
    #records = Record.objects.all()
    # проверка входа в систему 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate 
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Успешно. Вход выполнен.")
            return redirect('home')
        else:
            messages.success(request,"Что-то пошло не так. Попробуйте снова.")
            return redirect('home')
    else:
        if 'q' in request.GET:
            q = request.GET['q']
            records = Record.objects.filter(familia__icontains=q)
        else:
            records = Record.objects.all()
    return render(request, 'home.html', {'records':records})


def logout_user(request):
    logout(request)
    messages.success(request, "Выход из системы выполнен!")
    return redirect('home')

# новая страница
def customer_record(request, pk):
    # проверка (вошел ли человек в систему)
    if request.user.is_authenticated:
        # Look Up Records (Получаем нужный id)
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "Необходимо выполнить вход в систему.")
        return redirect('home')
    
# новая страница (товары)
def hardstore_record(request):
    if 'q' in request.GET:
            q = request.GET['q']
            hardstore_record = HardStore_record.objects.filter(name_category__icontains=q)
            #hardstore_record = HardStore_record.objects.filter(name_product__icontains=q)
    else:
        hardstore_record = HardStore_record.objects.all()
        
    return render(request, 'product.html', {'hardstore_record':hardstore_record})


# новая страница (склады)
def storehouse(request):
    if 'q' in request.GET:
        q = request.GET['q']
        storehouse = Storehouse.objects.filter(name_storehouse__icontains=q)
    else:
        storehouse = Storehouse.objects.all()
    return render(request, 'storehouse.html', {'storehouse':storehouse})

# новая страница (сотрудники)
def employee_record(request):
    if 'q' in request.GET:
        q = request.GET['q']
        employee = Employee.objects.filter(familia__icontains=q)
    else:
        employee = Employee.objects.all()
    return render(request, 'employee.html', {'employee_record':employee})

# удаление записи в таблице
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = HardStore_record.objects.get(id=pk)
        delete_it.delete()
        # уведомление об удалении записи
        messages.success(request, "Запись успешно удалена.")
        return redirect('product')
    else:
        messages.success(request, "Необходимо выполнить вход в систему.")
        return redirect('home')
    
# удаление записи в таблице
def delete_record_home(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        # уведомление об удалении записи
        messages.success(request, "Запись успешно удалена.")
        return redirect('home')
    else:
        messages.success(request, "Необходимо выполнить вход в систему.")
        return redirect('home')

# добавление записи в таблице
def add_product(request):
    form = AddProductForm(request.POST or None)
    if request.user.is_authenticated:
        if form.is_valid():
            add_product = form.save()
            messages.success(request, "Товар успешно добавлен!")
            return redirect('product')
        return render(request, 'add_product.html', {'form':form})
    else:
        messages.success(request, "Необходимо выполнить вход в систему.")
        return redirect('home')

# изменение записи в таблице product 
def update_product(request, pk):
	if request.user.is_authenticated:
		current_record = HardStore_record.objects.get(id=pk)
		form = AddProductForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Запись успешно обновлена")
			return redirect('product')
		return render(request, 'update_product.html', {'form':form})
	else:
		messages.success(request, "Необходимо выполнить вход в систему.")
		return redirect('home')
     
# добавление записи в таблице record
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if form.is_valid():
            add_record = form.save()
            messages.success(request, "Покупатель успешно добавлен!")
            return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "Необходимо выполнить вход в систему.")
        return redirect('home')
     
# изменение записи в таблице record 
def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Запись успешно обновлена")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "Необходимо выполнить вход в систему.")
		return redirect('home')
