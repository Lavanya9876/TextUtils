from django.http import HttpResponse
from django.shortcuts import render

def welcome(request):
    # params={'name':'harry','place':'mars'}             # we can also pass dictionary like return render(request,'index.html',params)
    return render(request, 'index.html')                 # using templates
    # return HttpResponse('''<h1>WELCOME TO MY WEBSITE .... click next to go to instagram...</h1> <a href="/insta"><button>Next</button>''')            # piping


# def instagram(request):
#     print(request.GET.get('text','default'))                 # returns the text ... which you have given in input area...if there is no text then they retrun default
#
#     return HttpResponse(''' <h1>Click next to go to facebook</h1> <a href ="/"> <button> Back </button></a>  <a href="/face"><button> Next</button></a>''')        # piping

#
# def facebook(request):
#     return HttpResponse('''<h1>Click next to go to youtube</h1><a href="/"><button>Back</button></a><a href="/youtube"><button>Next</button></a>''')           # piping


# def youtube(request):
#     return HttpResponse('''<h1>Click below button to return to home page</h1> <a href="/"><button>Back</button></a> <a href="http://127.0.0.1:8000/"><button>Return</button></a>''')             # piping



def analyse(request):
     #Get the text
     djtext = request.POST.get('text','default')


     #check checkbox values
     removepunc = request.POST.get('removepunc','off')  # checkbox
     fullcaps = request.POST.get('fullcaps','off')      # second checkbox
     newlineremover = request.POST.get('newlineremover','off')
     extraspaceremover = request.POST.get('extraspaceremover','off')
     charcounter = request.POST.get('charcounter','off')


     # check which checkbox is on
     if removepunc == "on":
        punctuations='''!()-[]{};:'"\,<>./!@#$%^&*_~'''
        analysed=""
        for char in djtext:
            if char not in punctuations:
                analysed = analysed + char
        params={'purpose':'removed punctuation','analysed_text':analysed}
        djtext=analysed
        # return render(request,'analyse.html',params)

     if fullcaps=="on":
         analysed =""
         for char in djtext:
             analysed= analysed + char.upper()
         params = {'purpose': 'change to uppercase', 'analysed_text': analysed}
         djtext = analysed
         # return render(request, 'analyse.html', params)

     if newlineremover=='on':
         analysed=""
         for char in djtext:
             if char !="\n" and char!="\r":            #in network the new line will be \n\r
                 analysed = analysed + char
         params = {'purpose': 'removed newlines', 'analysed_text': analysed}
         djtext = analysed
         # return render(request, 'analyse.html', params)

     if extraspaceremover=='on':
         analysed=""
         for index, char in enumerate(djtext):
             if not(djtext[index]==" " and djtext[index+1]==" "):
                 analysed = analysed + char
         params = {'purpose': 'removed newlines', 'analysed_text': analysed}
         djtext = analysed
         # return render(request, 'analyse.html', params)

     if charcounter=='on':
         analysed=0
         for char in djtext:
             if char.isalpha():
                 analysed = analysed + 1
         params = {'purpose': 'removed newlines', 'analysed_text': analysed}
         return render(request, 'analyse.html', params)

     if(removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charcounter != "on"):
         return HttpResponse("please select any operation! and try again")


     return render(request, 'analyse.html', params)

def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    return render(request, 'contactus.html')