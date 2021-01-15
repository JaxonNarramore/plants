from django.shortcuts import render


class Plant:
    def __init__(self, species, color, description, age):
        self.species = species
        self.color = color
        self.description = description
        self.age = age


plants = [
    Plant('Aloe', 'light green',
          'Suculent type plant with think leaves and is known to heal burns', 2),
    Plant('Christmas Cactus', 'dark green',
          'Cactus that blooms in the winter', 1),
    Plant('Orchid', 'Dark gren leaves with many different colors of flowers',
          'Beautiful flowers that are very hard to bloom', 2)
]


def about(request):
    return render(request, 'about.html')


def index(request):
    return render(request, 'index.html')


def plants_index(request):
    return render(request, 'plants/index.html', {'plants': plants})
