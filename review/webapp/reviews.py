from django.shortcuts import get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from webapp.models import Review
from webapp.forms import ReviewForm
from django.urls import reverse


class ReviewListView(ListView):
    model = Review
    template_name = 'products/product_detail.html'
    context_object_name = 'reviews'

    def get_queryset(self):
        if self.request.user.is_staff:
            return Review.objects.all()
        return Review.objects.filter(author=self.request.user)


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:product_detail', kwargs={'pk': self.kwargs['pk']})


class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review_edit.html'

    def get_success_url(self):
        return reverse_lazy('webapp:product_detail', kwargs={'pk': self.kwargs['pk']})

    def get_object(self, queryset=None):
        return get_object_or_404(Review, pk=self.kwargs['review_pk'], product_id=self.kwargs['pk'])

    def test_func(self):
        return self.request.user == self.get_object().author or self.request.user.is_staff


class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    template_name = 'reviews/review_delete.html'
    success_url = reverse_lazy('webapp:product_detail')

    def test_func(self):
        review = get_object_or_404(Review, pk=self.kwargs['review_pk'])
        return self.request.user == review.author or self.request.user.has_perm('webapp.delete_review')

    def get_object(self, queryset=None):
        return get_object_or_404(Review, pk=self.kwargs['review_pk'], product_id=self.kwargs['pk'])

    def get_success_url(self):
        return reverse_lazy('webapp:product_detail', kwargs={'pk': self.kwargs['pk']})
