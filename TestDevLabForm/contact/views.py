from django.views.generic.edit import CreateView
from .models import SimpleForm

# Create your views here.

class ContactUs(CreateView):
    model = SimpleForm
    fields = ['email', 'text', 'first_name', 'last_name']

