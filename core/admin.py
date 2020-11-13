from django.contrib import admin
from .models import Product

# Register your models here.
#@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
	list_display = ('nome', 'preco', 'estoque', 'slug', 'create', 'modificado', 'ativo')

admin.site.register(Product, ProdutoAdmin)