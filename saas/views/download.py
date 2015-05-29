'''
CSV download view basics.
'''

import csv
from StringIO import StringIO

from django.http import HttpResponse
from django.views.generic import View

class CSVDownloadView(View):
    def get(self, *args, **kwargs):
        content = StringIO()
        csv_writer = csv.writer(content)
        csv_writer.writerow(self.get_headings())
        for record in self.get_queryset(*args, **kwargs):
            csv_writer.writerow(self.queryrow_to_columns(record))
        content.seek(0)
        resp = HttpResponse(content, content_type='text/csv')
        resp['Content-Disposition'] = \
            'attachment; filename="{}"'.format(
                self.get_filename(*args, **kwargs))
        return resp

    def get_headings(self):
        raise NotImplementedError

    def get_queryset(self, *args, **kwargs):
        raise NotImplementedError

    def get_filename(self, *args, **kwargs):
        raise NotImplementedError

    def queryrow_to_columns(self, record):
        raise NotImplementedError
