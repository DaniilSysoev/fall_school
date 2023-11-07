from django.shortcuts import render, HttpResponse
import random
from . import models


def index(request):
    item = models.Item.objects.get(id=1)
    item.delete()
    return HttpResponse(f'Item deleted: {item.name} - {item.description} - {item.price}')