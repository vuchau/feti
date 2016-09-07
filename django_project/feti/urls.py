# coding=utf-8
"""URI Routing configuration for this apps."""
from django.conf.urls import patterns, url

# Needed by haystack views
from feti.forms.search import DefaultSearchForm
from haystack.query import SearchQuerySet
from haystack.views import search_view_factory, SearchView
from feti.views.campus import UpdateCampusView
from feti.views.landing_page import LandingPage
from feti.views.api import ApiCampus, ApiCourse, ApiAutocomplete

sqs = SearchQuerySet()

api_urls = patterns(
    '',
    url(
        r'^api/campus',
        ApiCampus.as_view(),
        name='api-campus'),
    url(
        r'^api/course',
        ApiCourse.as_view(),
        name='api-campus'),
    url(
        r'^api/autocomplete/(?P<model>.+)',
        ApiAutocomplete.as_view(),
        name='api-campus-autocomplete'),
)

urlpatterns = patterns(
    '',
    url(
        r'^$',
        LandingPage.as_view(),
        name='landing_page'),
    url(
        r'^search/',
        # include('haystack.urls')),
        'feti.views.search.search'),
    url(
        r'^customsearch/',
        search_view_factory(
            view_class=SearchView,
            template='search/custom_search.html',
            searchqueryset=sqs,
            form_class=DefaultSearchForm),
        name='haystack_search'),
    url(regex='^provider/(?P<pk>\d+)/update/$',
        view=UpdateCampusView.as_view(),
        name='update_campus'),
) + api_urls
