from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Item

def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    same_category_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=item_id)[0:3]
    return render(request, "item/detail.html", {
        "item": item,
        "same_category_items": same_category_items
    })
    