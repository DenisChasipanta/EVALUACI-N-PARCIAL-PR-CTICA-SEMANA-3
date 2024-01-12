from django.shortcuts import render, HttpResponse

htmlBase="""
    <h1>Mi proyecto Web</h1>
    <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/about/">Productos</a></li>
        <li><a href="/store/">Tienda</a></li>
        <li><a href="/contact/">Contacto</a></li>
    </ul>
"""

# Create your views here.
def home(request):
    return render(request, "core/index.html")
def store(request):
    return render(request, "core/store.html")
def contact(request):
    return render(request, "core/contact.html")
