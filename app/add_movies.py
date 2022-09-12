import requests
from bs4 import BeautifulSoup

# link = "https://m.arabseed.sbs/category/%d8%a7%d9%81%d9%84%d8%a7%d9%85-%d8%aa%d8%b1%d9%83%d9%8a%d8%a9/"


        

# # check if film in the db while add more films
# for i in range(len(data['name'])) :
#     if models.Film.objects.filter(name=data['name'][i]).exists() :
#         print('in the db : ', data['name'][i])
#     else :
#         kind = models.Category.objects.get(name='تركي')
#         models.Film.objects.create(
#             name=data['name'][i],
#             des=data['desc'][i],
#             image=data['img'][i],
#             url=data['film'][i],
#             kind=kind
#         )


# #  --> SAVE FILM <-- 
# # get_category = models.Category.objects.get(name='انيميشن')
# # for i in range(len(data['name'])) :
# #     models.Film.objects.create(
# #         name=data['name'][i],
# #         des=data['desc'][i],
# #         image=data['img'][i],
# #         url=data['film'][i],
# #         kind=get_category,
# #     )



# ##delete repated films
# # f = models.Film.objects.all()
# # for i in f :
# #     film = models.Film.objects.filter(name=i.name)
# #     if len(film) > 1 :
# #         models.Film.objects.get(id=i.id).delete()
# #         print('Done')
# #     else :
# #         pass

# #remove 'embed-embed' from the iframe url
# f = models.Film.objects.all()
# for i in f :
#     url = str(i.url).split('embed')
#     new_url = 'embed'.join(url)
#     if len(url) != 2 :
#         url.remove('-')
#         edit = models.Film.objects.get(id=i.id)
#         newOne = 'embed'.join(url)
#         edit.url = newOne
#         edit.save()
#         print('Done')
#     else :
#         pass
# # return JsonResponse(data="Done",safe=False)
# print('Mission Complete')

# # if request.user.is_staff :

# #     return render(request,'add.html')


# # else :
# #     return redirect('home')




