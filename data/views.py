from django.shortcuts import render, get_object_or_404, redirect
from .models import DataSet
from .forms import RecordForm
from django.db.models import Max


def home_page(request):
    data = DataSet.objects.filter(author='Max').order_by('id')
    return render(request, 'data/home_page.html', {'data': data})


def data_details(request, pk):
    data_number = get_object_or_404(DataSet, pk=pk)
    return render(request, 'data/data_details.html', {'data_number': data_number})


def new_record(request):
    if request.method == 'POST':
        record_form = RecordForm(request.POST)
        if record_form.is_valid():
            record = record_form.save(commit=False)
            record.id = int(DataSet.objects.aggregate(Max('id'))['id__max']) + 1
            record.save()
            return redirect('data_details', pk=record.pk)
    else:
        record_form = RecordForm()
    return render(request, 'data/new_record.html', {'record': record_form})


def record_edit(request, pk):
    number_record = get_object_or_404(DataSet, pk=pk)
    if request.method == 'POST':
        record = RecordForm(request.POST, instance=number_record)
        if record.is_valid():
            update_record = record.save(commit=False)
            update_record.save()
            return redirect('data_details', pk=update_record.pk)
    else:
        record = RecordForm(instance=number_record)
        return render(request, 'data/new_record.html', {'record': record})