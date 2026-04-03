from django.shortcuts import render, HttpResponse

def home(request):
    # return HttpResponse("Hello, welcome to the Cars site!")
    return HttpResponse("""
    <h1>Welcome to the Cars site!</h1>
    <ul>
        <li><a href="/cars/">View Cars</a></li>
        <li><a href="/cars/add/">Add a Car</a></li>
        <li><a href="/cars/search/">Search Cars</a></li>
    </ul> 
    <p>This is a simple Django app for managing car information.</p>
    <p>Use the navigation menu to explore different features.</p>                  
    """)

def cars(request):
    return HttpResponse("""
    <h1>Cars List</h1>
    <a href="/">Back to Home</a>
    <ul>
        <li>Car 1: Toyota Camry</li>
        <li>Car 2: Honda Accord</li>
        <li>Car 3: Ford Mustang</li>
    </ul>
    """)

def add_cars(request):
    return HttpResponse("""
    <h1>Add a New Car</h1>
    <a href="/">Back to Home</a>
    <form method="post" action="/cars/add/">
        <label for="make">Make:</label><br>
        <input type="text" id="make" name="make"><br>
        <label for="model">Model:</label><br>
        <input type="text" id="model" name="model"><br>
        <label for="year">Year:</label><br>
        <input type="number" id="year" name="year"><br><br>
        <input type="submit" value="Add Car">
    </form>
    """)

def search_cars(request):
    return HttpResponse("""
    <h1>Search Cars</h1>
    <a href="/">Back to Home</a>
    <form method="get" action="/cars/search/">
        <label for="query">Search by Make or Model:</label><br>
        <input type="text" id="query" name="query"><br><br>
        <input type="submit" value="Search">
    </form>
    """)

# Create your views here.
