from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def private_chef_nairobi(request):
    return render(request, "private-chef-nairobi.html")


def private_chef_kenya(request):
    return render(request, "private-chef-kenya.html")


def catering_nairobi(request):
    return render(request, "catering-nairobi.html")


def fine_dining_nairobi(request):
    return render(request, "fine-dining-nairobi.html")


def wedding_catering_nairobi(request):
    return render(request, "wedding-catering-nairobi.html")


def cooking_classes_nairobi(request):
    return render(request, "cooking-classes-nairobi.html")


def baking_classes_nairobi(request):
    return render(request, "baking-classes-nairobi.html")


def chef_network_nairobi(request):
    return render(request, "chef-network-nairobi.html")
