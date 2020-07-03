from django.http import HttpResponse 
from django.shortcuts import  render

def about(request):
    params={'name':'papa','sher':'gao'}
    return render(request,'index.html',params)
    #HttpResponse('<button>hey</button>')


def second(request):
    return HttpResponse('<a href="/">hey</button>')

def npage(request):
    djtext = request.GET.get('text', 'default')
    analyse=""
    punctuation= "!@#$%^&*?><:"
    ck= request.GET.get('punct', 'off')
    print(ck)
    cap= request.GET.get('caps', 'off')
    spc = request.GET.get('spaceremove','off')
    chrc = request.GET.get('charcount','off')
    print(ck)
    if ck=="on":
        for char in djtext:
            if char not in punctuation:
                analyse=analyse+char
        params={'pucn':'searching..','royal':analyse}
        return render(request,'punctu.html',params)

    elif cap=="on":
        for char in djtext:
            if char not in punctuation:
                analyse=analyse+ char.upper()
        return HttpResponse(analyse)

    elif spc=="on":
        analyse = ""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyse = analyse + char
        return HttpResponse(analyse)

    elif chrc=="on":
        return HttpResponse(len(djtext))
    else:
        return HttpResponse(djtext)

def punctu(request):
    s='''<a href ='https://practice.geeksforgeeks.org/explore/?category%5B%5D=Arrays&company%5B%5D=Amazon&page=1'>gfg</a> </br>
     <a href ='https://practice.geeksforgeeks.org/explore/?category%5B%5D=Arrays&company%5B%5D=Amazon&page=1'>gfg</a> </br>
     <a href ='https://practice.geeksforgeeks.org/explore/?category%5B%5D=Arrays&company%5B%5D=Amazon&page=1'>gfg</a> </br>
     <a href ='https://practice.geeksforgeeks.org/explore/?category%5B%5D=Arrays&company%5B%5D=Amazon&page=1'>gfg</a> </br>
     <a href ='https://practice.geeksforgeeks.org/explore/?category%5B%5D=Arrays&company%5B%5D=Amazon&page=1'>gfg</a> </br>
     
     '''

    return HttpResponse(s)

