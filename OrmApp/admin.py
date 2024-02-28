from django.contrib import admin
from . import models


@admin.register(models.Musician)
class MusicianAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Membership)
class MembershipAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Album)
class AlbumAdmin(admin.ModelAdmin):
    pass
