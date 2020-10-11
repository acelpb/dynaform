from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .forms import MessageForm
from .models import Message


# Create your views here.
class DisplayMessagesView(ListView):
    model = Message
    ordering = ('-created_at')
    paginate_by = 25


class UploadMessageView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("twenty_five_years")
