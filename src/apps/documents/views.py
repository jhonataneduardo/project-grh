from django.views.generic.edit import CreateView
from .models import Document


class DocumentCreate(CreateView):
    model = Document
    fields = ['description', 'file']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.belongs_to = self.request.user.employee
        obj.save()
        return super(DocumentCreate, self).form_valid(form)
