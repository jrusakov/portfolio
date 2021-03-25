from django.contrib import admin

from .models import Post, Education, Experience, Certificates, Skills


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'publish', 'slug']
    list_filter = ['publish']
    prepopulated_fields = {'slug': ['title', ]}


admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Certificates)
admin.site.register(Skills)

