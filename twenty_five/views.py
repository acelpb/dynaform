from django.views.generic import CreateView, ListView

from .forms import MessageForm
from .models import Message


# Create your views here.
class DisplayMessagesView(ListView):
    model = Message


class UploadMessageView(CreateView):
    model = Message
    form_class = MessageForm

    success_url = "/"
