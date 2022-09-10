from django.shortcuts import render
from django.views import generic

from .models import Receipt

class IndexView(generic.ListView):
    template_name = 'receipts/index.html'
    context_object_name = "receipts_list"

    def get_queryset(self):
        return Receipt.objects.all()

class DetailView(generic.DetailView):
    model = Receipt
    template_name = 'receipts/detail.html'