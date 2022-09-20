from django.contrib import admin

from.models import  Post,Category,Location,Breed


admin.site.register(Breed)
admin.site.register(Location)
# admin.site.register(User)
admin.site.register(Category)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['name','location_pet','category_id']

# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display=['user','content', 'created_at']

# @admin.register(Reply)
# class ReplyAdmin(admin.ModelAdmin):
#     list_display=['user','content','created_at']
