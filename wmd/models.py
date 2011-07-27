
from django.db import models
from django.contrib.admin import widgets as admin_widgets
from wmd import widgets as wmd_widgets
try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^wmd.models.MarkDownField"])
except ImportError:
    pass


class MarkDownField(models.TextField):
    def formfield(self, **kwargs):
        defaults = {'widget': wmd_widgets.MarkDownInput}
        defaults.update(kwargs)
        
        if defaults['widget'] == admin_widgets.AdminTextareaWidget:
            defaults['widget'] = wmd_widgets.AdminMarkDownInput
        
        return super(MarkDownField, self).formfield(**defaults)
