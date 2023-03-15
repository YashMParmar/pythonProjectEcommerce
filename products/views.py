from django.shortcuts import render

def about(request):
    context={}
    return render(request,'products/about.html', context)

def blog(request):
    context={}
    return render(request,'products/blog.html', context)

def contact(request):
    context={}
    return render(request,'products/contact.html', context)

def info(request):
    context={}
    return render(request,'products/info.html', context)

def main(request):
    context={}
    return render(request,'products/main.html', context)

def store(request):
    context={}
    return render(request,'products/store.html', context)


