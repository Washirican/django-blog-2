from django.contrib import admin
from blogging.models import Post, Category

# FIXME
# @admin.register(Category)
# class Category(admin.Category):
#     pass


admin.site.register(Post)
admin.site.register(Category)
