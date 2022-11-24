import  json #vključimo json

podatki = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
#izpišemo podatke v json obliki
print(json.dumps(podatki))
