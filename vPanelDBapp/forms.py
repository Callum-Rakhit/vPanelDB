from django import forms
from .models import Panel, Subpanel, HUGOgene, LogChanges


class HUGOgeneLookupForm(forms.ModelForm):

    class Meta:
        model = HUGOgene
        fields = ('symbol', 'locationSortable', 'ensemblGeneID')


class PanelForm(forms.ModelForm):

    class Meta:
        model = Panel
        fields = ('panelName', 'panelID', 'username', 'panelVersion', 'panelTypes')
        labels = {  # Add custom names to modelform labels
            'panelName': 'Panel Name',
            'panelID': 'Panel ID',
            'username': 'Username',
            'panelVersion': 'Panel Version',
            'panelTypes': 'Panel Type',
        }

    gene1 = forms.CharField(max_length=255)

    # def clean_gene(self):
    #     gene = self.cleaned_data['gene'].strip(';')
    #     return gene

    def __init__(self, *args, **kwargs):
        super(PanelForm, self).__init__(*args, **kwargs)
        self.fields['gene1'].widget.attrs.update({'id': 'gene_list'})


class SubpanelForm(forms.ModelForm):

    class Meta:
        model = Subpanel
        fields = ('subpanelName', 'subpanelID', 'username', 'subpanelVersion', 'panel', 'gene')
        labels = {  # Add custom names to modelform labels
            'subpanelName': 'Subpanel Name',
            'subpanelID': 'Subpanel ID',
            'username': 'Username',
            'subpanelVersion': 'Subpanel Version',
            'panel': 'Panel (Select then click the "Update" button in the bottom right)'
        }

    def __init__(self, *args, **kwargs):

        parent_panel = kwargs.pop('parent_panel')
        print(type(parent_panel))
        super(SubpanelForm, self).__init__(*args, **kwargs)
        # Query if the gene is in the parent_panel (Panel)
        if parent_panel:
            self.fields['gene'].queryset = HUGOgene.objects.filter(panel__id=int(parent_panel))
        else:
            pass


class LogForm(forms.ModelForm):

    class Meta:
        model = LogChanges
        fields = ('prevUsername', 'prevPanelName', 'prevPanelID', 'prevPanelVersion')
        labels = {  # Add custom names to modelform labels
            'prevUsername': 'Previous Username',
            'prevPanelName': 'Previous Panel Name',
            'prevPanelID': 'Previous Panel ID',
            'prevPanelVersion': 'Previous Panel Version',
        }
