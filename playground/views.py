from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .forms import FormForFileUpload
from bs4 import BeautifulSoup
import re



#Views are Request handler, for a request send a response
def handle_uploaded_file(f):   
    with open('playground/HTMLuploads/'+f.name, 'wb+') as destination:   
        for chunk in f.chunks(): 
            destination.write(chunk) 
    with open('playground/HTMLuploads/'+f.name, 'rb') as file:
        soup = BeautifulSoup(file, 'lxml')
        parse_text=soup.get_text()
    print(parse_text)    
    print(soup.title.string)

   
    matched_name=re.findall(r'(?:Dr|Mr|Ms|Mrs| )[.][a-zA-Z ]+\b',soup.title.string)
    matched_name_no_title=re.findall(r'[- ]?[A-Za-z ]+$\b',soup.title.string)
    #print(result_name)
    if(matched_name):
        for name in matched_name:
            print('Name: '+name)
    else:
         for name in matched_name_no_title:    
            print('Name: '+name)

    # prof_regex = r'([a-zA-Z ]+Professor\b)'
    # lecturer_regex= r'([a-zA-Z ]+Lecturer\b)'
    # matched_title =re.compile(prof_regex | lecturer_regex ,parse_text)
    # for title in matched_title:
    #     print("Title: " +title) 
    




# Create your views here.
def hello(request):
    context={}
    if request.POST: 
        form = FormForFileUpload(request.POST, request.FILES) 
        if form.is_valid(): 
            handle_uploaded_file(request.FILES["file_field"]) 
    else: 
        form = FormForFileUpload() 
    context['form'] = form 
    return render(request, "hello.html", context) 
    

