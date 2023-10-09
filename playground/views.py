from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.shortcuts import render
from .forms import FormForFileUpload
from bs4 import BeautifulSoup
import re

def send_file(response):
    file=open('playground/HTMLuploads/text.txt','rb')
    response=FileResponse(file)
    return response



def write(val):
    with open('playground/HTMLuploads/text.txt','a') as file:
        file.write(val+"\n")

#Views are Request handler, for a request send a response
def handle_uploaded_file(f):   
    with open('playground/HTMLuploads/'+f.name, 'wb+') as destination:   
        for chunk in f.chunks(): 
            destination.write(chunk) 
    with open('playground/HTMLuploads/'+f.name, 'rb') as file:
        soup = BeautifulSoup(file, 'lxml')
        parse_text=soup.get_text()
    #print(parse_text)    
    #print(soup.title.string)

    print('\n')

    matched_name=re.findall(r'(?:Dr|Mr|Ms|Mrs| )[.][a-zA-Z ]+\b',soup.title.string)
    matched_name_no_title=re.findall(r'[- ]?[A-Za-z ]+$\b',soup.title.string)
    #print(result_name)
    write('Name')
    if(matched_name):
        for name in matched_name:
            write(name)
            print('Name \n'+name)
    else:
         for name in matched_name_no_title:    
            print('Name \n'+name)

    print('\n')

    # prof_regex = r'([a-zA-Z ]+Professor\b)'
    # lecturer_regex= r'([a-zA-Z ]+Lecturer\b)'
    write('Title')
    matched_title =re.findall(r'[a-zA-Z ]*(?:Professor|Lecturer)+',parse_text)
    for title in matched_title:
        write(title)
        print("Title \n" +title) 

    print('\n')

    div_research_interest=soup.find("div",{"class":"col-md-12 col-sm-11 col-xs-12"}).get_text()
    div_research_interest=[s for s in div_research_interest.splitlines() if s]
    for interest in div_research_interest:
        write(interest)
        print(interest)
    
    print('\n')

    div_education=soup.find_all("div",{"class":"col-md-12 col-sm-11 col-xs-12"})[1].get_text()
    div_education=[s for s in div_education.splitlines() if s]
    for education in div_education:
        write(education)
        print(education)

    print('\n')

    div_office=soup.find("div",{"class":"col-md-4 col-sm-12 col-xs-12"}).get_text()
    div_office=[s for s in div_office.splitlines() if s]
    for office in div_office:
        write(office)
        print(office)

    print('\n')    

    




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
    
    

