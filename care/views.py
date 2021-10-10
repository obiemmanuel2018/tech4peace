from django.shortcuts import render

# Create your views here.


def login_page(request):
    return render(request, 'login.html')


def payment(request):
    return render(request, 'payment.html')


def routines(request):
    return render(request, 'routines.html')


def details(request):
    return render(request, 'details.html')


# def nutrient(request, id):

#     nutrients = [{
#         'id': 1,
#         'image': 'static/images/nutrient1.png',
#         'description': 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Numquam quo modi porro, ut fugiat vero Lorem ipsum dolor sit amet consectetur adipisicing elit. Dignissimos adipisci eaque voluptates velit delectus reprehenderit repudiandae enim numquam nihil aliquid'
#     },
#         {
#         'id': 2,
#         'image': 'static/images/nutrient2.png',
#         'description': 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Numquam quo modi porro, ut fugiat vero Lorem ipsum dolor sit amet consectetur adipisicing elit. Dignissimos adipisci eaque voluptates velit delectus reprehenderit repudiandae enim numquam nihil aliquid'
#     },
#         {
#         'id': 3,
#         'image': 'static/images/nutrient3.png',
#         'description': 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Numquam quo modi porro, ut fugiat vero Lorem ipsum dolor sit amet consectetur adipisicing elit. Dignissimos adipisci eaque voluptates velit delectus reprehenderit repudiandae enim numquam nihil aliquid'
#     },
#         {
#         'id': 4,
#         'image': 'static/images/nutrient4.png',
#         'description': 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Numquam quo modi porro, ut fugiat vero Lorem ipsum dolor sit amet consectetur adipisicing elit. Dignissimos adipisci eaque voluptates velit delectus reprehenderit repudiandae enim numquam nihil aliquid'
#     }]

#     nutrient = {}

#     for nt in nutrients:
#         if nt['id'] == id:
#             print('found')
#             nutrient = nt
#             break

#     print(nutrient)

#     return render(request, 'nutrient.html', {'nutrient': nutrient})


# def exercise(request, id):
#     pass
