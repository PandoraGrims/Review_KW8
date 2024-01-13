from django.shortcuts import get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from webapp.models import Review, Product
from webapp.forms import ReviewForm
from django.urls import reverse


class ReviewListView(ListView):
    model = Review
    template_name = 'products/product_detail.html'
    context_object_name = 'reviews'

    def get_queryset(self):
        product = get_object_or_404(Product, pk=self.kwargs['product_id'])
        return Review.objects.filter(product=product, moderated=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = get_object_or_404(Product, pk=self.kwargs['product_id'])
        return context


class CreateReviewView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review_create.html'

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs['product_id'])
        form.instance.author = self.request.user
        form.instance.product = product
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('webapp:review_list', kwargs={'product_id': self.kwargs['product_id']})


class UpdateReviewView(LoginRequiredMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review_edit.html'

    def test_valid(self):
        review = self.get_object()
        return self.request.user == review.author

    def get_success_url(self):
        return reverse_lazy('webapp:product_detail_view', kwargs={'product_id': self.kwargs['product_id']})


class DeleteReviewView(LoginRequiredMixin, DeleteView):
    model = Review
    template_name = 'reviews/review_delete.html'

    def test_valid(self):
        review = self.get_object()
        return self.request.user == review.author

    def get_success_url(self):
        return reverse_lazy('webapp:review_list', kwargs={'product_id': self.kwargs['product_id']})
