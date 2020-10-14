from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from .models import Image, Location, Category
from django.core.exceptions import ObjectDoesNotExist

# def welcome(request):
#     '''
#     Method to return our images, locations & categories
#     '''
#     images = Image.objects.all()
#     location = Location.objects.all()
#     categories = Category.get_all_categories()
#     return render(request, 'welcome.html', {"images":images[::-1], "location":location, "categories":categories})

def search_results(request):
    
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"image.html", {"image":image})

def image_location(request, location):
    images = Image.filter_by_location(location)
    print(images)
    return render(request, 'location.html', {'image': image})

















# from django.shortcuts import render,redirect
# from django.http  import HttpResponse,Http404
# import datetime as dt
# from .models import Details

# # Create your views here.

# def fotos_of_day(request):
#     date = dt.date.today()
#     return render(request, 'all-fotos/today-fotos.html', {"date": date,})

#     # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
#     day = convert_dates(date)
#     html = f'''
#         <html>
#             <body>
#                 <h1>Photos for {day} {date.day}-{date.month}-{date.year}</h1>
#             </body>
#         </html>
#             '''
#     return HttpResponse(html)
      
# def convert_dates(dates):

#     # Function that gets the weekday number for the date.
#     day_number = dt.date.weekday(dates)

#     days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

#     # Returning the actual day of the week
#     day = days[day_number]
#     return day
# # View Function to present news from past days

# def past_days_fotos(request, past_date):

#     try:
#         # Converts data from the string Url
#         date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

#     except ValueError:
#         # Raise 404 error when ValueError is thrown
#         raise Http404()
#         assert False

#     if date == dt.date.today():
#         return redirect(fotos_today)

#     fotos = Details.days_fotos(date)
#     return render(request, 'all-fotos/past-fotos.html',{"date": date,"fotos":fotos})    


# # def past_days_fotos(request,past_date):

# #     try:
# #         # Converts data from the string Url
# #         date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

# #     except ValueError:
# #         # Raise 404 error when ValueError is thrown
# #         raise Http404()
# #     day = convert_dates(date)
# #     html = f'''
# #         <html>
# #             <body>
# #                 <h1>Photos for {day} {date.day}-{date.month}-{date.year}</h1>
# #             </body>
# #         </html>
# #             '''
# #     return HttpResponse(html)

# def fotos_today(request):
#     date = dt.date.today()
#     fotos = Details.todays_fotos()
#     return render(request, 'all-fotos/today-fotos.html', {"date": date,"fotos":fotos})  


# def search_results(request):

#     if 'details' in request.GET and request.GET["details"]:
#         search_term = request.GET.get("details")
#         searched_details = Details.search_by_title(search_term)
#         message = f"{search_term}"

#         return render(request, 'all-fotos/search.html',{"message":message,"detailss": searched_detailss})

#     else:
#         message = "You haven't searched for any term"
#         return render(request, 'all-fotos/search.html',{"message":message})     