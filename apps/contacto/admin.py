from django.contrib import admin
from .models import Contacto

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ['nombre_completo', 'email', 'asunto', 'fecha_envio', 'leido']
    list_filter = ['leido', 'fecha_envio']
    search_fields = ['nombre_completo', 'email', 'asunto']
    readonly_fields = ['fecha_envio']
    list_editable = ['leido']
    date_hierarchy = 'fecha_envio'
    
    fieldsets = (
        ('Información del Contacto', {
            'fields': ('nombre_completo', 'email', 'asunto', 'fecha_envio')
        }),
        ('Mensaje', {
            'fields': ('mensaje',)
        }),
        ('Estado', {
            'fields': ('leido',)
        }),
    )
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Si es una edición
            return self.readonly_fields + ['nombre_completo', 'email', 'asunto', 'mensaje']  # ← CAMBIO AQUÍ: Lista en lugar de tupla
        return self.readonly_fields