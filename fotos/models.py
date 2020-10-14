from django.db import models
import datetime as dt

# class Image(models.Model):
#     image_name = models.CharField(max_length =30)
#     image_description = models.TextField()
#     location = models.ForeignKey('Location', on_delete=models.CASCADE, null=True, blank=True)
#     category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)    
#     pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
#     gallery_image = models.ImageField(upload_to = 'gallery/', null=True)

    class Meta:
        '''
        Class method to display images by date published
        '''
        ordering = ['pub_date']

    def save_image(self):
        '''
        Method to save our images
        '''
        self.save()

    def delete_image(self):
        '''
        Method to delete our images
        '''
        self.delete()

    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    @classmethod
    def search_by_category(cls,search_term):
        fotos = cls.objects.filter(category__category__icontains=search_term)
        return fotos

    @classmethod
    def filter_by_location(cls, location):
        image_location = Image.objects.filter(location__name=location).all()
        return image_location
   
    def __str__(self):
        return self.image_description

class Location(models.Model):
    location = models.CharField(max_length =30)

    @classmethod
    def get_all_locations(cls):
        locations = cls.objects.all()
        return locations

    def save_location(self):
        self.save()

    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(location=location)

    @classmethod
    def delete_location(cls,location):
        cls.objects.filter(location=location).delete()

    def __str__(self):
        return self.location

class Category(models.Model):
    category = models.CharField(max_length =30)

    @classmethod
    def get_all_categories(cls):
        categories = cls.objects.all()
        return categories

    def save_category(self):
        self.save()

    @classmethod
    def update_category(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    @classmethod
    def delete_category(cls,category):
        cls.objects.filter(category=category).delete()

    def __str__(self):
        return self.category




# from django.db import models
# import datetime as dt

# class Category(models.Model):
#     type= models.CharField(max_length =30)

# try:
#     category = Category.objects.get(type= 'nature')
#     print('Editor found')
# except DoesNotExist:
#     print('Category was not found') 

#     def __str__(self):
#         return self.type
#     # class Meta:
#     #     ordering = ['type']

#     def save_category(self):
#         self.save()


# class location(models.Model):
#     location = models.CharField(max_length =30)

#     def __str__(self):
#         return self.location


# class Details(models.Model):
#     Who = models.CharField(max_length =60)
#     Occassion = models.TextField()
#     category = models.ForeignKey('Category',on_delete=models.CASCADE,)
#     location = models.ManyToManyField(location)
#     pub_date = models.DateTimeField(auto_now_add=True) 
#     details_image = models.ImageField(upload_to = 'category/')

#     # Testing Save Method
#     def test_save_method(self):
#         self.nature.save_category()
#         categories = Category.objects.all()
#         self.assertTrue(len(editors) > 0)

#     @classmethod
#     def todays_fotos(cls):
#         today = dt.date.today()
#         fotos = cls.objects.filter(pub_date__date = today)
#         return fotos

#     @classmethod
#     def days_fotos(cls,date):
#         fotos = cls.objects.filter(pub_date__date = date)
#         return fotos


#     @classmethod
#     def search_by_title(cls,search_term):
#         fotos = cls.objects.filter(title__icontains=search_term)
#         return fotos
