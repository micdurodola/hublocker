from django.test import TestCase
from .models import Locker

#Test Case
class TestLocker(TestCase):

    @classmethod

    def setUpTestData(cls):
        locker = Locker.objects.create(specification='H295 * W460 * D520mm',address='50 Lekki road, Lekki', city='Lekki',
        state='Lagos',featured='S',price='N450 per item/mo N15,000, XX no of orders online only price',
            first_price='1N For First Rent',quantity='2')
        locker.save()

    def test_locker(self):
        locker = Locker.objects.get(id=1)
        specification = f'{locker.specification}'
        price = f'{locker.price}'
        first_price = f'{locker.first_price}'
        quantity = f'{locker.quantity}'

        self.assertEqual(specification,'H295 * W460 * D520mm')
        self.assertEqual(price,'N450 per item/mo N15,000, XX no of orders online only price')
        self.assertEqual(first_price,'1N For First Rent')
        self.assertEqual(quantity,'2')
