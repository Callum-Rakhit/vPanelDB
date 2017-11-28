from ajax_select import register, LookupChannel
from .models import Panel


@register('panel')
class PanelLookup(LookupChannel):

    model = Panel

    def get_query(self, q, request):
          return self.model.objects.filter(title__icontains=q).order_by('title')

    def format_item_display(self, item):
        return u"<span class='tag'>%s</span>" % item.name