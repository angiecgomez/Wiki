import re
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from . import util
from random import choice

import markdown

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry_page(request, entry):
    if util.get_entry(entry) is not None:
        content = util.get_entry(entry)
        HTML_content = markdown.markdown(content)
        return render(request, "encyclopedia/wiki.html", {
            "title" : entry, "content" : HTML_content
        })
    else:
        return HttpResponseRedirect("/error_page")

def error_page(request):
    return render(request, "encyclopedia/error_page.html")

def search_encyclopedia(request):
    query = request.GET['q']
    if query == "":
        return HttpResponseRedirect(reversed("index"))
    else:
        entries = util.list_entries()
        findings = []

        if util.get_entry(query) is not None:
            return redirect(entry_page, query)

        for entry in entries:
            if(entry.lower().find(query.lower())==-1):
                pass
            else:
                findings.append(entry)
        return render(request, "encyclopedia/search.html",{
            "exists": len(findings) > 0,
            "query": query,
            "findings": findings
            })


        """ for entry in entries:
            if (query.lower() == entry.lower()):
                content = util.get_entry(entry)
                HTML_content = markdown.markdown(content)
                return render(request, "encyclopedia/wiki.html", {
                    "title" : entry, "content" : HTML_content
                })
            if(entry.lower().find(query.lower())==-1):
                pass
            else:
                findings.append(entry)
        return render(request, "encyclopedia/search.html",{
            "exists": len(findings) > 0,
            "query": query,
            "findings": findings """
            

def create_page(request):
        return render(request, "encyclopedia/create_page.html")
        

def save_newpage(request):
    if request.method == "POST":
        title = request.POST['title']
        
        if util.get_entry(title) is None:
            content = request.POST.get('content')
            util.save_entry(title=title, content=content)
            return redirect(entry_page, title)
        else:
            error_message = "There is already an entry with the title: "
            return render(request, "encyclopedia/create_page.html",{
            "error_message": error_message,
            "title": title
            })

def edit_page(request, entry):
    return render(request, "encyclopedia/edit_page.html", {
        "title": entry,
        "content": util.get_entry(entry)
    })

def update_page(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST.get('content')            
        util.save_entry(title=title, content=content)
        return redirect(entry_page, title)

def random_page(request):
    return redirect(entry_page, choice(util.list_entries()))