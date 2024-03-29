from django.contrib import admin
from .models import Image
from django.db.models import Count

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display=['title','slug','image','created','total_likes']
    list_filter=['created']
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(total_likes_count=Count('users_like'))
        return queryset
    
    def display_total_likes(self, obj):
        return obj.total_likes
    display_total_likes.short_description = 'Total Likes'


# admin.site.register(Image, ImageAdmin)