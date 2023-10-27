from django.shortcuts import render, HttpResponse
import random
from . import models


#def index(request):
#    return HttpResponse('Hello world!')


#def item(request, name, id):
#    data = f"Item name: {name}, id: {id}"
#    return HttpResponse(data)


#def new_index(request):
#    return render(request, 'myapp/index.html')


#def some_data(request):
#    array = models.Item.objects.all().values_list()
#    context = {'data': 'Hello world!', 'array': array}
#    return render(request, 'myapp/some_data.html', context)


#def random_data(request, start, end):
#    random_number = random.randint(int(start), int(end))
#    context = {'random_number': random_number}
#    return render(request, 'myapp/random_data.html', context)


#def new_instance(request, name, description, price):
#    new_item = models.Item.objects.create(name=name, description=description, price=price)
#    return HttpResponse(f'New item created: {new_item.name}')


#def update_instance(request, id, name, description, price):
#    item = models.Item.objects.get(id=id)
#    item.name = name
#    item.description = description
#    item.price = price
#    item.save()
#    return HttpResponse(f'Item updated: {item.name}')


#def delete_instance(request, id):
#    item = models.Item.objects.get(id=id)
#    item.delete()
#    return HttpResponse(f'Item deleted: {item.name}')
def index(request):
    item = models.Item.objects.get(id=3)
    item.delete()
    return HttpResponse(f'Item deleted: {item.name}')