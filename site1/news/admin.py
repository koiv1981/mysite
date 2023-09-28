from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


from .models import News, Category


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ("id", "title", 'category', "created_at", "updated_at", "is_published", "views")
    list_display_links = ("id", "title")
    search_fields = ("title", 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')
    readonly_fields = ("views",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")
    search_fields = ("title",)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
