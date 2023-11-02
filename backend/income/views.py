from .models import Income
from .serializers import IncomeSerializer
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from django.conf import settings
from mindee import Client, documents
from .forms import IncomeUploadForm
from .utils import import_income_from_csv, clear_csv_data
import csv

class IncomeViewSet(viewsets.ModelViewSet):
    serializer_class = IncomeSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Income.objects.all()

    def get_queryset(self):
        user = self.request.user
        query_set = self.queryset
        return query_set.filter(user=user)

    @action(detail=False, methods=['POST'], permission_classes=[permissions.IsAuthenticated])
    def upload_receipt(self, request):
        form = IncomeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            receipt_image = request.FILES['receipt_image']
            if not receipt_image.content_type.startswith('image/'):
                return Response({"error": "Invalid file type. Please upload an image."}, status=status.HTTP_400_BAD_REQUEST)

            try:
                process_mindee_api(receipt_image, request)
            except Exception as e:
                return Response({"error": f"Error with Mindee API: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Response({"message": "Income receipt processed successfully."}, status=status.HTTP_200_OK)

        return Response({"error": "Invalid form submission."}, status=status.HTTP_400_BAD_REQUEST)

def process_mindee_api(receipt_image, request):
    mindee_client = Client(api_key=settings.MINDEE_API_KEY)
    input_doc = mindee_client.doc_from_file(receipt_image)
    result = input_doc.parse(documents.TypeInvoiceV4)

    invoice = result.document

    supplier_name = invoice.supplier_name if hasattr(invoice, 'supplier_name') else None
    invoice_date = invoice.invoice_date if hasattr(invoice, 'invoice_date') else None
    total_amount = invoice.total_amount if hasattr(invoice, 'total_amount') else None
    category = invoice.document_type if hasattr(invoice, 'document_type') else None

    try:
        write_to_income_csv(request.user.username, supplier_name, invoice_date, total_amount, category)
        import_income_from_csv(settings.CSV_FILE_INCOME)
        clear_csv_data(settings.CSV_FILE_INCOME)
    except Exception as e:
        raise Exception(f"Error writing to CSV: {e}")


def write_to_income_csv(username, supplier_name, invoice_date, total_amount, category):
    with open(settings.CSV_FILE_INCOME, 'a', newline='') as csvfile:
        fieldnames = ['user', 'income_source', 'date', 'amount', 'category']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if csvfile.tell() == 0:
            writer.writeheader()

        writer.writerow({
            'user': username,
            'income_source': supplier_name,
            'date': invoice_date,
            'amount': total_amount,
            'category': category
        })