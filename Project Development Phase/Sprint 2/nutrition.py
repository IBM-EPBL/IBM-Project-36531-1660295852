import requests

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/479101/information"

headers = {
	"X-RapidAPI-Key": "7a9aa3cba1msh304f811bfeb3713p15bc42jsn1c3eb4c29d4b",
	"X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)