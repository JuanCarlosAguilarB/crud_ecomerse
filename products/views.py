# from django.shortcuts import render

# # Instanciamos las vistas genéricas de Django 
# from django.views.generic import ListView, DetailView 
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
 
# # Instanciamos el modelo 'Postres' para poder usarlo en nuestras Vistas CRUD
# from .models import Postres

# # Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
# from django.urls import reverse
 
# # Habilitamos el uso de mensajes en Django
# from django.contrib import messages 
 
# # Habilitamos los mensajes para class-based views 
# from django.contrib.messages.views import SuccessMessageMixin 
 
# # Habilitamos los formularios en Django
# from django import forms 

# class PostresListado(ListView): 
#     model = Postres # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'

# class PostreCrear(SuccessMessageMixin, CreateView): 
#     model = Postres # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'
#     form = Postres # Definimos nuestro formulario con el nombre de la clase o modelo 'Postres'
#     fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
#     success_message = 'Postre Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre
 
#     # Redireccionamos a la página principal luego de crear un registro o postre
#     def get_success_url(self):        
#         return reverse('leer') # Redireccionamos a la vista principal 'leer'

# class PostreDetalle(DetailView): 
#     model = Postres # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'

# class PostreActualizar(SuccessMessageMixin, UpdateView): 
#     model = Postres # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py' 
#     form = Postres # Definimos nuestro formulario con el nombre de la clase o modelo 'Postres' 
#     fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
#     success_message = 'Postre Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
#     # Redireccionamos a la página principal luego de actualizar un registro o postre
#     def get_success_url(self):               
#         return reverse('leer') # Redireccionamos a la vista principal 'leer'


                
# Django         
from django.views.generic.edit import FormView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView 
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

# Apps
from .forms import FruitsForm
from .models import Fruits


class ViewProdutsView(ListView): 

    template_name = 'index.html'
    queryset  = Fruits # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'
    # paginate_by = 10
    model = Fruits
    
    def get_queryset(self):
        return super().get_queryset()
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        fruits = self.queryset.objects.filter(status=True)
        context['fruits'] = fruits
        return context

class RegisterProductFormView(FormView):
    template_name = 'form.html'
    form_class = FruitsForm
    success_url = '/'

    def form_valid(self, form):
        if form.is_valid():
            
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            descriptions = form.cleaned_data.get('descriptions')
            photo = form.cleaned_data.get('photo')

            fruit = self.form_class.Meta().model(
                name=name, 
                price=price, 
                descriptions=descriptions,
                photo=photo)
            
            fruit.save()
            form.save()
        return super().form_valid(form)
    

class ProductosDeleteView(DeleteView):
    # specify the model you want to use
    model = Fruits
     
    success_url ="/"
    
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)

class UpdateProductFormView(UpdateView):

    model = Fruits
    template_name = 'form.html'
    form_class = FruitsForm
    success_url = '/'

    def post(self, request, *args, **kwargs) :
        
        name = request.POST.get('name')
        price = request.POST.get('price')
        descriptions = request.POST.get('descriptions')
        photo = request.POST.get('photo')

        fruit = Fruits.objects.get(id=kwargs['pk'])
        
        if fruit:
            if name: fruit.name = name
            if price: fruit.price = price
            if descriptions: fruit.descriptions = descriptions
            if photo: fruit.photo = photo
            fruit.save()
            
        return HttpResponseRedirect(self.success_url)    
    
    
    def form_valid(self, form):
        if form.is_valid():
            
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            descriptions = form.cleaned_data.get('descriptions')
            photo = form.cleaned_data.get('photo')

            fruit = self.form_class.Meta().model(
                name=name, 
                price=price, 
                descriptions=descriptions,
                photo=photo)
            
            fruit.save()
            form.save()
        return super().form_valid(form)
 