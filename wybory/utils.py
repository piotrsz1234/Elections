from io import BytesIO  # A stream implementation using an in-memory bytes buffer
# It inherits BufferIOBase

from django.http import HttpResponse
from django.template.loader import get_template

# pisa is a html2pdf converter using the ReportLab Toolkit,
# the HTML5lib and pyPdf.

from xhtml2pdf import pisa
# difine render_to_pdf() function
from .models import Wybory
from django.shortcuts import get_object_or_404


def render_to_pdf(template_src, context):
    template = get_template(template_src)
    context = {'node': context}
    context_dict = context
    html = template.render(context_dict)
    result = BytesIO()

    # This part will create the pdf.
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None
