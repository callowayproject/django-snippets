from django.test import TestCase
from django import template

class snippetsTest(TestCase):
    """
    Tests for django-snippets
    """
    def test_snippets(self):
        from snippets.models import Snippet
        s = Snippet(name='test1', snippet='my test snippet')
        s.save()
        tmpl = "{% load snippet_tags %}{% get_snippet test1 %}"
        ctxt = template.Context({})
        out = template.Template(tmpl).render(ctxt)
        self.assertEqual(out, 'my test snippet')