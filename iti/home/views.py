from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


"""All i need is view and url ??

# views are functions that will be called when a user requests a page

# urls are the paths that users will type in their browsers to access the website

# urls are defined in the urls.py file

# views are defined in the views.py file

# urls.py is the file that maps urls to views"""


def test(request):
    # will be called when a user requests the page
    return HttpResponse("<h1 style='color: red; text-align: center;'>Hello, World!</h1>")



def user_home(request, name):
    """  
    in this view i will print the name of the user
    the name is passed as a parameter to the function
    the name is used to display the user's name
    You must define the url  ?   path('home/<name>', user_home, name='user_home'),
    """
    
    return HttpResponse(f"<h1 style='color: purple; text-align: center;'>Hello, {name}!</h1>")



def user_profile(request, id):
    # this function require id to be an integer only , if not it will return 404
    profiles_details = [{
        'id': 1,
        'name': 'John',
        'age': 20,
        'email': 'john@example.com'
    },
    {
        'id': 2,
        'name': 'Jane',
        'age': 21,
        'email': 'jane@example.com'
    }]

    # once you pass the id , response with dictionary of the user


    usr = {}
    for profile in profiles_details:
        id = int(id)
        if profile['id'] == id:
            usr = profile
            return HttpResponse(f"<h1 style='color: orange; text-align: center;'>Profile of user {usr}</h1>")

    else:
        return HttpResponse(f"<h1 style='color: red; text-align: center;'>User not found</h1>")





def landing(request):
    # render page ??
    # return HttpResponse("landing")
    return render(request, 'home/landing.html')


def index(request):
    return render(request, 'home/index.html')