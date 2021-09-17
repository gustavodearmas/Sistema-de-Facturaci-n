from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, FormView
from core.erp.form import ContactForm
from core.erp.models import Contact, Dptos


class ContactListView(ListView):
    model = Contact
    template_name = 'contact/list_contact.html'
    context_object_name = 'contacts'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Contact.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de contactos'
        context['tool'] = 'Opciones de contenido'
        context['list_url'] = reverse_lazy('contact_create')
        return context

class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact/create_contact.html'
    success_url = reverse_lazy('contact_list')

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            #elif action == 'search_product_id':
            #    data = []
            #    for i in Dptos.objects.filter(country_id=request.POST['id']):
            #        data.append({'id': i.id_dpto, 'name': i.name_dpto})
            else:
                data['error'] = 'no ha ingresado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar cliente'
        context['options'] = 'Opciones de contenido '
        context['list_url'] = reverse_lazy('contact_list')
        context['action'] = 'add'
        return context

class ContactUpdateView(UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact/create_contact.html'
    success_url = reverse_lazy('contact_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'no ha ingresado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar contacto'
        context['list_url'] = reverse_lazy('contact_list')
        context['action'] = 'edit'
        return context

class ContactDeleteView(DeleteView):
    model = Contact
    template_name = 'contact/delete_contact.html'
    success_url = reverse_lazy('contact_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar cliente'
        context['list_url'] = reverse_lazy('contact_list')
        return context

class ContactDetailView(DetailView):
    model = Contact
    template_name = 'contact/view_contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = 'pendiente'
        return context

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'contact/create_contact.html'
    success_url = reverse_lazy('contact_list')

    def form_valid(self, form):
        print(form.is_valid())
        print(form.errors)
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.is_valid())
        print(form.errors)
        return super().form_invalid(form)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Form | Cliente'
        context['options'] = 'Opciones de contenido '
        context['list_url'] = reverse_lazy('contact_list')
        context['action'] = 'add'
        return context

