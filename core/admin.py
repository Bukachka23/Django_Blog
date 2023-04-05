from django.contrib import admin
from .models import Post, Tag

# A subclass of ModelAdmin that provides a default form for editing model instances.
class PostAdmin(admin.ModelAdmin):      #
    list_display = ('title', 'created_on', 'updated_on')
    list_filter = ('tags', 'created_on', 'updated_on')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    autocomplete_fields = ('tags',)

# A function that registers a model class with the given admin class.
admin.site.register(Post, PostAdmin)

# The admin class for the Tag model.
class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)

admin.site.register(Tag, TagAdmin)
