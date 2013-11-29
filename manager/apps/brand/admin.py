from django.contrib import admin
from django import forms
from .models import Brand, BrandOwner, BrandType

#customized delete button to be placed on each row of the ModelAdmin
def delete_button(obj):
    #TODO: need a better name other than 'soft delete' or 'delete'
    return "<input type='button' value='Soft Delete' id='customized_delete_button' onClick='softDeleteConfirmation()'/>"

#TODO: need a better name other than 'soft delete' or 'delete'
delete_button.short_description = 'Soft Delete'
delete_button.allow_tags = True

class BrandTypeAdmin(admin.ModelAdmin):
    actions = None

    # Never delete a brand, update its BSIN
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(BrandType, BrandTypeAdmin)


class BrandOwnerAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('owner_nm', 'owner_logo_admin', 'owner_link',delete_button)
    fields = (
        'owner_nm', 'owner_link', 'owner_wiki_en', 'owner_logo')
    search_fields = ['owner_nm']

    class Media:
        js = (
            'brand/js/customized_admin.js',   
        )

    # Never delete a brand, update its BSIN
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(BrandOwner, BrandOwnerAdmin)


class BrandAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('bsin', 'brand_nm', 'brand_logo_admin', 'flag_delete',delete_button)
    fields = (
        'bsin', 'brand_nm', 'owner_cd', 'brand_type_cd', 'brand_link',
        'brand_logo', ('flag_delete', 'comments'), 'last_modified')
    readonly_fields = ('bsin', 'last_modified')
    search_fields = ['bsin', 'brand_nm', 'owner_cd__owner_nm']
    list_filter = ('flag_delete', )

    class Media:
        js = (
            'brand/js/customized_admin.js',   
        )

    # Never delete a brand, update its BSIN
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Brand, BrandAdmin)
