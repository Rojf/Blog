from django.contrib import admin


class PostAdmin(admin.ModelAdmin):
    list_display = [ 'title', 'slug', 'author', 'publish', 'active' ]
    list_filter = [ 'active', 'created', 'publish', 'author' ]
    search_fields = [ 'title', 'description' ]
    prepopulated_fields = { 'slug': ('title',) }
    raw_id_fields = [ 'author' ]
    date_hierarchy = 'publish'
    ordering = [ 'active', 'publish' ]
