from django.contrib import admin

# Register your models here.
from .models.post import Post

# Alterar o modo de visualização dos Modelos no Django Admin
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
