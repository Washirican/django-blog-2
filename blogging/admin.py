from django.contrib import admin
from blogging.models import Post, Category

# FIXME: Reference Django ModelAdmin documentation
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     pass


admin.site.register(Post)
admin.site.register(Category)
