from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from .resources import PersonResource
from tablib import Dataset
# Create your views here.
def export(request):
    person_resource = PersonResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="persons.csv"'
    return response
def simple_upload(request):
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = person_resource.import_data(dataset, dry_run=True) 

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False) 

    return render(request, 'simpleapp/import.html')