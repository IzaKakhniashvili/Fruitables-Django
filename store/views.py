# views.py

from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from .models import Product, Category, Tag
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required

class ProductListView(ListView):
    model = Product
    template_name = 'shop.html'
    context_object_name = 'products'
    paginate_by = 9  # Show 9 products per page

    def get_queryset(self):
        # Get the category based on the slug from the URL
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category, slug=slug)
        products = Product.objects.filter(category=category)

        # Filter based on search query
        search_query = self.request.GET.get('search', '')
        if search_query:
            products = products.filter(name__icontains=search_query)

        # Filter based on price range
        price_range = self.request.GET.get('rangeInput', None)
        if price_range:
            products = products.filter(price__lte=price_range)

        # Filter based on selected category
        selected_category = self.request.GET.get('category', None)
        if selected_category:
            products = products.filter(categories__id=selected_category)

        # Filter based on selected tag
        selected_tag = self.request.GET.get('tag', None)
        if selected_tag:
            products = products.filter(tags__name=selected_tag)

        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Add category and tag options for filters
        context['categories'] = Category.objects.all()
        context['all_tags'] = Tag.objects.all()

        # Pass selected filters and search query to the context
        context['search_query'] = self.request.GET.get('search', '')
        context['selected_category'] = self.request.GET.get('category', None)
        context['selected_tag'] = self.request.GET.get('tag', None)

        return context
