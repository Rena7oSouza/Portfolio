from django.shortcuts import render
import markdown2
from django import forms
from . import util
from django.shortcuts import redirect
import random


class NewPageForm(forms.Form):
    title = forms.CharField(label="Title")
    description = forms.CharField(label="Description")
    
    
def index(request):
    
    return render(request, "encyclopedia/index.html", {
        "entries": hiperlink(util.list_entries())
    })

def getentry(request, name):
    name, page = convertToHTML(request, name)
    return render(request, "encyclopedia/content.html", {"title": name, "content": page})


def convertToHTML(request, name):
    md = util.get_entry(name)
    if md == None:
        return isNone()
    else:
        request.session["name"] = name
        request.session["description"] = md
        output = markdown2.markdown(md)
        return name, output

def isNone():
    name = "Error"
    page = "<h1><b>Page was not found!</b></h1>"
    return name, page

def hiperlink(list):
    newlist = []
    for item in list:
        newitem = '<a href="wiki/'+item+'">'+item+"</a>"
        newlist.append(newitem)
    return newlist


class SearchForm(forms.Form):
    q = forms.CharField(label='Search Encyclopedia')

def search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['q']
            if query in util.list_entries():
                return redirect(f'/wiki/{query}')
            else:
                newlist = []
                for item in util.list_entries():
                    if query.lower() in item.lower():
                        newlist.append(item)
                return render(request, "encyclopedia/index.html", {"entries": hiperlink(newlist)})
            
def randomPage(request):
    randomindex = random.choice(util.list_entries())
    return redirect(f"wiki/{randomindex}")

def addPage(request):
    if request.method == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            if title not in util.list_entries():
                util.save_entry(title, description)
                return redirect(f'/wiki/{title}')
            else:
                return render(request, "encyclopedia/content.html", {"title": "Error", "content": "<h1>This page already exists!</h1>"})
        else:
            return render(request, "encyclopedia/form.html", {"form": form})
    return render(request, "encyclopedia/form.html", {"form": NewPageForm()})

def editPage(request):
    return render(request, "encyclopedia/edit.html", {"title": request.session["name"], "description": request.session["description"]})


def savePage(request):
    if request.method == "POST":
        form = NewPageForm(request.POST)
        title = request.session["name"]
        if form.is_valid():
            description = form.cleaned_data["description"]
        else:
            description = form.cleaned_data["description"]
        util.save_entry(title, description)
        return redirect(f'/wiki/{title}')