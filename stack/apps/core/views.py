from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect, get_object_or_404
from django.views.generic import TemplateView
from django.views import View
from django.views.generic.edit import FormView
from django.urls import reverse, reverse_lazy
from core.forms import StackSearchForm
from core.utils import call_api as call_api_with_check_time_limit
import requests


class StackListView(TemplateView):
    # specify name of template
    template_name = 'core/stack_list.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['list_page'] = True

        """Get all response data from session and append with context"""
        context['stack_data'] = request.session.get('stack_data')
        if context['stack_data'] and 'items' in context['stack_data']:
            context['items'] = context['stack_data']['items']
        else:
            context['items'] = []
        
        return self.render_to_response(context)

class SearchPageView(FormView):
    # specify the Form you want to use
    form_class = StackSearchForm

    # specify name of template
    template_name = "core/stack_search.html"


    def form_valid(self, form):
        if form.is_valid():
            query_param = f'site=stackoverflow&{form.data.urlencode()}'
            url = f"https://api.stackexchange.com/2.3/search/advanced?{query_param}&filter=default"

            payload={}
            headers = {}

            """This is the method for check limit """
            response = call_api_with_check_time_limit(url, payload, headers)
            if 'is_limit_exceeds' in response and response['is_limit_exceeds']:
                self.request.session['remaining_time'] = response['remaining_time']
                return redirect('core:api_limit')

            """Set or Assign response data in session"""
            self.request.session['stack_data'] = response.json()

            return redirect('core:stack_list')
        else:
            form.invalid()
        return render(self.request, self.template_name, {'form': form})


class RateLimitErrorPage(TemplateView):
    template_name = '429.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        """Get remaining time from session"""
        context['remaining_time'] = request.session.get('remaining_time')
        return self.render_to_response(context)