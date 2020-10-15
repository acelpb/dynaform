from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView

from .forms import MessageForm
from .models import Message


class TemporaryView(TemplateView):
    template_name = "twenty_five/welcome.html"


class DisplayMessagesView(ListView):
    model = Message
    ordering = ('-created_at')
    paginate_by = 25

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            self.template_name = "twenty_five/simple_message_list.html"
        return super().get(request, *args, **kwargs)


class UploadMessageView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("twenty_five_years")
