from django.contrib import admin
from cmdb.models import Article
from cmdb.models import Comment
admin.site.register(Article)
admin.site.register(Comment)