from django.contrib import admin
from apps.main.models import Sponsor, Charity, Raffle, Entry, CharityImage, RaffleLevel,UserExtend, RaffleImage


class RaffleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Sponsor)
admin.site.register(Charity)
admin.site.register(Raffle, RaffleAdmin)
admin.site.register(Entry)
admin.site.register(CharityImage)
admin.site.register(RaffleLevel)
admin.site.register(UserExtend)
admin.site.register(RaffleImage)
 