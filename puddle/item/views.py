from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .form import AddItemForm
# Create your views here.
from .models import Item

def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    same_category_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=item_id)[0:3]
    return render(request, "item/detail.html", {
        "item": item,
        "same_category_items": same_category_items
    })

@login_required
def addNewItem(request):
    if request.method == "POST":
        form = AddItemForm(request.POST, request.FILES)
        item = form.save(commit=False)
        item.created_by = request.user
        item.save()
        return redirect("item:detail", item_id=item.id)

    else:
        form = AddItemForm()

        return render(request, "item/form.html", {
            'form': form
        })
    