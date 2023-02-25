from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .form import AddItemForm, EditItemForm
# Create your views here.
from .models import Item, Category


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
            'form': form,
            'title': "New Item"
        })


def items(request):
    query = request.GET.get('query', '')
    items = Item.objects.filter(is_sold=False)
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    if query:
        items = items.filter(Q(name__icontains=query) | Q(description_icontains=query))

    return render(request, 'item/browse.html', {
        "items": items,
        "query": query,
        "categories": categories,
        "category_id": int(category_id)
    })


@login_required
def editItem(request, item_id):
    item = get_object_or_404(Item, pk=item_id, created_by=request.user)
    if request.method == "POST":
        form = EditItemForm(request.POST, request.FILES, instance=item)
        form.save()

        return redirect("item:detail", item_id=item.id)

    else:
        form = EditItemForm(instance=item)

        return render(request, "item/form.html", {
            'form': form,
            'title': "Edit Item"
        })


@login_required
def delete(request, item_id):
    item = get_object_or_404(Item, pk=item_id, created_by=request.user)
    item.delete()

    return redirect("dasboard:index")
