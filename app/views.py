from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.decorators import APIView
from .models import Category, Film
from .serializors import FilmSer, CategorySer
from rest_framework.response import Response
from rest_framework import status
from django.views import generic
import requests
from bs4 import BeautifulSoup
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import requests
from bs4 import BeautifulSoup
from django.db.models import Q



class ManageFilm (APIView) :
    def get (self, request) :
        object_list = Film.objects.all().order_by('?').values('id','name','image')
        paginator = Paginator(object_list, 20)  # 3 posts in each page
        page = request.GET.get('page')
        try:
            post_list = paginator.page(page)
        except PageNotAnInteger:
            post_list = paginator.page(1)
        except EmptyPage:
            post_list = paginator.page(paginator.num_pages)
        return JsonResponse(data=list(post_list),safe=False)
    



def home (request) :
    # for search
    if 'key' in request.GET :
        key = request.GET['key']
        films = Film.objects.filter(Q(des__icontains=key)|Q(name__icontains=key)).order_by('-date').values('id','name','image')
        return JsonResponse(data=list(films),safe=False)
        
    return render(request,'index.html')


def categoy (request):

    if 'type' in request.GET:
        kind = request.GET['type']
        catg = Category.objects.get(name=kind)
        object_list = Film.objects.all().filter(kind=catg).values('id','name','image').order_by('-date')
        paginator = Paginator(object_list, 20)  # 3 posts in each page
        page = request.GET.get('page')
        try:
            post_list = paginator.page(page)
        except PageNotAnInteger:
            post_list = paginator.page(1)
        except EmptyPage:
            post_list = paginator.page(paginator.num_pages)
        return JsonResponse(data=list(post_list),safe=False)

    category = Category.objects.all().values('name')

    return JsonResponse(data=list(category),safe=False)

def get_film_by_catg (request) :
    kind = request.GET['type']
    catg = Category.objects.get(name=kind)
    object_list = Film.objects.all().filter(kind=catg).values('id','name','image').order_by('-date')
    paginator = Paginator(object_list, 20)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return JsonResponse(data=list(post_list),safe=False)


def watch_video (request, videoid) :
    vid = Film.objects.get(id=videoid)
    req = requests.get(vid.url)
    soup = BeautifulSoup(req.text,'html.parser')
    video_url = soup.find('source').get('src')
    
    context = {
        'url':video_url,
        'films':Film.objects.all().order_by("?")[:10],
        'info':vid,
    }
    return render(request,'watch_film.html',context)


def test (request) :
     
    # most_common = [
    #     'a space Odyssey' 
    #     'creation',   
    #     'predestination',
    #     'darkest hour', 
    #     'milion Dollar baby', 
    #     'the skin I live in',
    #     'the room',
    #     'in time',
    #     'the lake house',
    #     'a beautiful mind',
    #     'still Alice',
    #     'i am Sam',
    #     'forgtoten',
    #     'old',
    #     'tenet',
    #     'ex machina',
    #     'american beauty',
    #     'the road',
    #     'mirage',
    #     'donnie darko',
    #     'eternal sunshine to the Spotless mind',
    #     'disobedience',
    #     'midnight in Paris',
    #     'her',
    #     'the guerncey literally',
    #     'law abiding citizen ',
    #     'children of men',
    #     'lucy ',
    #     'the father ',
    #     'forrest gump ',
    #     'rain man ',
    #     'silive linings playboo', 
    #     'as good as it gets ',
    #     'the purge',
    #     'movie (1917)',
    #     'fury',
    #     'saving private Ryan',
    #     'idiocracy',
    #     'equals',
    #     'lion',
    #     'the tomorrow war',
    #     'alph',
    #     'the mountain between us',
    #     'the impossible',
    #     'parasite',
    #     'free guy',
    # ]

    # links = []
    # for most in most_common :

    #     req = requests.get('https://m.arabseed.sbs/find',{'find':most})

    #     soup = BeautifulSoup(req.text,'html.parser')

    #     Results = soup.findAll('div',{'class':'MovieBlock'})



    #     for i in Results :
    #         film_text = i.find('a').find('h4').text
    #         film_url = i.find('a').get('href')
    #         if "فيلم" in film_text :
    #             check = Film.objects.filter(name=film_text)
    #             if check.exists() :
    #                 pass
    #             else :
    #                 links.append(film_url)

    # for link in links:

    #     req = requests.get(link)
    #     soup = BeautifulSoup(req.text,'html.parser')

    #     poster =  soup.find('div',{'class':'Poster'})
    #     film_image = poster.find('img').get('data-src')
    #     catg = str(soup.find('div',{'class':'MetaTermsInfo'}).find('a').text).split()
    #     if len(catg) > 1 :
    #         catg = catg[1]
    #     else :
    #         catg = catg[0]

    #     get_catg = Category.objects.get_or_create(name=catg)

    #     film_title = soup.find('h1',{'class':'Title'}).text
    #     film_des = str(soup.find('p',{'class':'descrip','style':''}).text).replace('Arabseed','').replace('عرب سيد','كوكب الافلام')




    #     new_film_url = link + 'watch/'
    #     if new_film_url == 'https://m.arabseed.sbs/%d9%83%d9%84%d9%8a%d8%a8-%d9%85%d9%88%d8%b3%d9%8a%d9%82%d9%8a-%d9%81%d9%8a%d9%84%d9%85-mission-impossible-4/watch/' :
    #         pass
    #     else :
    #         r = requests.get(new_film_url)
    #         s = BeautifulSoup(r.text,'html.parser')
    #         try : 
    #             get_video = str(s.find('iframe').get('src')).split('/')[-1].replace('-embed-','-')
    #             film_url = f"https://m.seeeed.xyz/{get_video}"
    #         except Exception as error :
    #             print('ERROR  : ', error)
    #             print('Link : ', new_film_url)
    #             print(s.find('iframe'))
    #             break


    #     if Film.objects.filter(name=film_title).exists():
    #         print(film_title, ' -> on the db')
    #     else :
    #         print('Category : ', get_catg[0])
    #         # Film.objects.create(
    #         #     name=film_title,
    #         #     des=film_des,
    #         #     image=film_image,
    #         #     url = film_url,
    #         #     kind=Category.objects.get(name=get_catg[0]),
    #         # )
    #         print(f'{film_title} ==> Added !')



    return HttpResponse('ok')




# handle errors

def Pagehandler404 (request, error) :
    return render(request,'error.html')
    
