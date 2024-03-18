from django.contrib import admin
from .models import Category,Movie

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','slug']
    prepopulated_fields = {'slug':('title',)}
admin.site.register(Category,CategoryAdmin)


class MovieAdmin(admin.ModelAdmin):
    list_display = ['title','release_date','category','actors']
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 20
admin.site.register(Movie,MovieAdmin)