from django import template

register = template.Library()

class SnippetNode(template.Node):
    def __init__(self, snippet_name):
        self.snippet_name = template.Variable(snippet_name)
    
    def render(self, context):
        try:
            name = self.snippet_name.resolve(context)
        except template.VariableDoesNotExist:
            name = self.snippet_name.var
        try:
            from snippets.models import Snippet
            snippet = Snippet.objects.get(name=name)
            return snippet.snippet
        except Snippet.DoesNotExist:
            return ''

@register.tag
def get_snippet(parser, token):
    """
    {% get_snippet <snippet_name> %}
    """
    try:
        tagname, snippet_name = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires a single argument" % token.contents.split()[0])
    return SnippetNode(snippet_name)