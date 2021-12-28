from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from product.models import Category, Product, Comment, Order


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent', 'status']
    list_filter = ['title']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'image_tag', 'price']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('image_tag',)
    list_filter = ['category']


class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ['name', 'email', 'message', 'ip', 'product']
    list_display = ['name', 'email', 'message', 'create_at']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'amount', 'food', 'price', 'status', ]
    list_filter = ['status']


class CategoryAdmin2(DraggableMPTTAdmin):
    list_display = ('tree_actions',
                    'indented_title',
                    'related_products_count',
                    'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}
    mptt_indent_field = "title"

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        qs = Category.objects.add_related_count(
            qs,
            Product,
            'category',
            'products_cumulative_count',
            cumulative=True
        )

        qs = Category.objects.add_related_count(
            qs,
            Product,
            'category',
            'products_count',
            cumulative=False
        )
        return qs

    def related_products_count(self, instance):
        return instance.products_count

    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count

    related_products_cumulative_count.short_description = 'Related products (in tree)'


admin.site.register(Category, CategoryAdmin2)
admin.site.register(Product, ProductAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Order, OrderAdmin)
