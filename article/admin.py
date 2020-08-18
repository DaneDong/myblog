from django.contrib import admin
from .models import Article

# Register your models here.
# admin.site.register(Article)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    ordering=('id',)
    list_display=('id','title','content','created_time','last_updated_time','is_deleted','author','readed_num')