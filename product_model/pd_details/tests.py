from django.test import TestCase
from .models import details
class basicdetail(TestCase):
    def setUp(self):
        details.objects.create(name='Mi mobiles',
                               description='good mobile',
                               costperitem=1000,
                               stockquantity=120,
                               volume=1200000

                                )
    def test_get_method(self):
        url='http://127.0.0.1:8000/product/'
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)
        qs=details.objects.filter(name='Mi mobiles')
        self.assertEqual(qs.count(),1)

