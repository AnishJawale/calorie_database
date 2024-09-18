from django.shortcuts import render, redirect
from .models import FoodItem
import json
import requests

def home(request):
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(
            api_url + query, headers={'X-Api-Key': 'ugj5Leh6Jh+DmQisFLwgpg==FKoUpnhdW5bpAwgG'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)

            # Loop through the API data and save each food item to the database
            for item in api:
                food_item = FoodItem(
                    user=request.user,  # Assuming the user is logged in
                    name=item.get('name', 'Unknown'),
                    calories=item.get('calories', 'Not available') if item.get('calories') != "Only available for premium subscribers." else 'Not available',
                    fat_total_g=item.get('fat_total_g', 0),
                    fat_saturated_g=item.get('fat_saturated_g', 0),
                    protein=item.get('protein_g', 'Not available') if item.get('protein_g') != "Only available for premium subscribers." else 'Not available',
                    sodium_mg=item.get('sodium_mg', 0),
                    potassium_mg=item.get('potassium_mg', 0),
                    cholesterol_mg=item.get('cholesterol_mg', 0),
                    carbohydrates_total_g=item.get('carbohydrates_total_g', 0),
                    fiber_g=item.get('fiber_g', 0),
                    sugar_g=item.get('sugar_g', 0)
                )
                food_item.save()  # Save the data in the database

        except Exception as e:
            api = "oops! There was an error"
            print(e)

        return render(request, 'home.html', {'api': api})
    else:
        return render(request, 'home.html', {'query': 'Enter a valid query'})
    

def database_view(request):
    # Fetch food items saved by the logged-in user
    food_items = FoodItem.objects.filter(user=request.user)

    # Render the template and pass the food items to the context
    return render(request, 'database_view.html', {'food_items': food_items})
