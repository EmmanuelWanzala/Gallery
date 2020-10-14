# from django.test import TestCase
# from .models import Category,Details,location
# import datetime as dt

# class CategoryTestClass(TestCase):

#     # Set up method
#     def setUp(self):
#         self.nature= Category(type = 'nature')

# # Testing  instance
#     def test_instance(self):
#         self.assertTrue(isinstance(self.nature,Category))


# class DetailsTestClass(TestCase):

#     def setUp(self):
#         # Creating a new editor and saving it
#         self.nature= Category(type = 'nature')
#         self.nature.save_category()

#         # Creating a new tag and saving it
#         self.new_location = location(name = 'testing')
#         self.new_location.save()

#         self.new_details= Details(title = 'Test Details',post = 'This is a random test Post',category = self.nature)
#         self.new_details.save()

#         self.new_details.location.add(self.new_location)

#     def test_get_fotos_today(self):
#         today_fotos = Details.todays_fotos()
#         self.assertTrue(len(today_fotos)>0)


#     def tearDown(self):
#         Category.objects.all().delete()
#         location.objects.all().delete()
#         Details.objects.all().delete()

# def test_get_fotos_by_date(self):
#         test_date = '2020-10-13'
#         date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
#         fotos_by_date = Details.days_fotos(date)
#         self.assertTrue(len(fotos_by_date) == 0)