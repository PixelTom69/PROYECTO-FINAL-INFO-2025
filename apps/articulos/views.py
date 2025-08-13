from django.shortcuts import render, get_object_or_404
from .models import Articulo
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import FormularioCrearArticulo, FormularioModificarArticulo
from genericos.models import Categoria
from django.utils import timezone
from datetime import timedelta
from django.core.paginator import Paginator

# DECORADOR PARA UNA VBF QUE CONTROLA SI EL USUARIO ESTA LOGUEADO
from django.contrib.auth.decorators import login_required
# MIXINS PARA UNA VBC QUE CONTROLA SI EL USUARIO ESTA LOGUEADO
from django.contrib.auth.mixins import LoginRequiredMixin
# Decorador para una VBF para controlar si el usuario es staff
from django.contrib.admin.views.decorators import staff_member_required
# MIXIN PARA UNA VBC PARA CONTROLAR EL TIPO DE USUARIO (lo usamos para ver si es staff)
from django.contrib.auth.mixins import UserPassesTestMixin

# Vista basada en funciones - CORREGIDA
def Listar_Articulos(request):
    # Empezar con todos los artículos
    articulos = Articulo.objects.all()
    categorias = Categoria.objects.all()
    
    # FILTRADO POR PERÍODO
    periodo = request.GET.get('periodo')
    
    if periodo == 'recientes':
        # Artículos de los últimos 30 días
        fecha_limite = timezone.now() - timedelta(days=30)
        articulos = articulos.filter(creado__gte=fecha_limite)
    
    elif periodo == 'antiguos':
        # Artículos anteriores a los últimos 30 días
        fecha_limite = timezone.now() - timedelta(days=30)
        articulos = articulos.filter(creado__lt=fecha_limite)
    
    elif periodo == 'semana':
        # Artículos de esta semana
        fecha_limite = timezone.now() - timedelta(days=7)
        articulos = articulos.filter(creado__gte=fecha_limite)
    
    elif periodo == 'mes':
        # Artículos de este mes
        fecha_limite = timezone.now() - timedelta(days=30)
        articulos = articulos.filter(creado__gte=fecha_limite)
    
    # ORDENAMIENTO
    valor_a_ordenar = request.GET.get("orden", "desc")  # Por defecto descendente
    
    if valor_a_ordenar == 'asc':
        articulos = articulos.order_by('creado')  # Más antiguos primero
    elif valor_a_ordenar == 'desc' or valor_a_ordenar == 'dsc':
        articulos = articulos.order_by('-creado')  # Más recientes primero
    else:
        articulos = articulos.order_by('-creado')  # Por defecto más recientes
    
    # PAGINACIÓN (opcional)
    paginator = Paginator(articulos, 6)  # 6 artículos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'articulos': page_obj,
        'categorias': categorias,
        'is_paginated': page_obj.has_other_pages(),
        'page_obj': page_obj,
    }
    
    return render(request, "articulos/listar.html", context)

# @staff_member_required
def detalle_articulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    context = {
        'articulo': articulo,
    }
    return render(request, 'articulos/detalle.html', context)

class Crear_Articulo(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Articulo
    template_name = "articulos/crear.html"
    form_class = FormularioCrearArticulo
    def get_success_url(self):
        """
        Redirige de vuelta al filtro de categoría si vino desde ahí
        """
        categoria_id = self.request.GET.get('categoria')
        if categoria_id:
            return reverse_lazy("articulos:path_filtro_categoria", kwargs={'pk': categoria_id})
        return reverse_lazy("articulos:path_listar_articulos")
    
    def test_func(self):
        return self.request.user.is_staff
    
    def get_initial(self):
        """
        Preselecciona la categoría si viene como parámetro GET
        Ejemplo: /articulos/crear/?categoria=2
        """
        initial = super().get_initial()
        categoria_id = self.request.GET.get('categoria')
        if categoria_id:
            try:
                # Verificar que la categoría existe
                from .models import Categoria  # Ajusta el import según tu estructura
                categoria = Categoria.objects.get(pk=categoria_id)
                initial['categoria'] = categoria
            except (Categoria.DoesNotExist, ValueError):
                # Si la categoría no existe o el ID no es válido, ignorar
                pass
        return initial
    
    def get_context_data(self, **kwargs):
        """
        Agrega contexto adicional al template si es necesario
        """
        context = super().get_context_data(**kwargs)
        
        # Opcional: agregar información sobre la categoría preseleccionada
        categoria_id = self.request.GET.get('categoria')
        if categoria_id:
            try:
                from .models import Categoria
                categoria = Categoria.objects.get(pk=categoria_id)
                context['categoria_preseleccionada'] = categoria
            except (Categoria.DoesNotExist, ValueError):
                pass
                
        return context

class Modificar_Articulo(UpdateView):
    model = Articulo
    template_name = "articulos/modificar.html"
    form_class = FormularioModificarArticulo
    success_url = reverse_lazy("articulos:path_listar_articulos")

class Borrar_Articulo(DeleteView):
    model = Articulo
    success_url = reverse_lazy("articulos:path_listar_articulos")

def Filtrar_Categoria(request, pk):
    categoria_filtrado = get_object_or_404(Categoria, pk=pk)
    articulos_filtrados = Articulo.objects.filter(categoria=categoria_filtrado)
    
    # AÑADIR ORDENAMIENTO TAMBIÉN AL FILTRO POR CATEGORÍA
    valor_a_ordenar = request.GET.get("orden", "desc")
    
    if valor_a_ordenar == 'asc':
        articulos_filtrados = articulos_filtrados.order_by('creado')
    elif valor_a_ordenar == 'desc' or valor_a_ordenar == 'dsc':
        articulos_filtrados = articulos_filtrados.order_by('-creado')
    else:
        articulos_filtrados = articulos_filtrados.order_by('-creado')
    
    # PAGINACIÓN para filtros por categoría
    paginator = Paginator(articulos_filtrados, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'articulos': page_obj,
        'categoria': categoria_filtrado,
        'is_paginated': page_obj.has_other_pages(),
        'page_obj': page_obj,
    }
    
    return render(request, 'articulos/filtrados.html', context)