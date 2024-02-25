data = [{"name": "anne", "experiance": 2, "age": 24, "qualification": "bachelors", "languages": ["python", "java", "c#"]},
        {"name": "Kane", "experiance": 3, "age": 28, "qualification": "bachelors", "languages": ["java", "c#", "c++"]},
        {"name": "jane", "experiance": 7, "age": 34, "qualification": "master", "languages": ["c#", "html"]},
        {"name": "John", "experiance": 6, "age": 29, "qualification": "bachelors", "languages": ["python", "java", "HTML"]},
        {"name": "Jenny", "experiance": 5, "age": 23, "qualification": "master", "languages": ["c#", "html", "python", "java"]}]

min_expo =2
qual = ["bachelors", "master", "PHD"]
min_age = 22
exp_lang = ["python", "java"]
selected = []

for cv in data:
    if (cv["age"] >= min_age) and (cv["experiance"] > min_expo) and (cv["qualification"] in qual) and (set(exp_lang).issubset(set(cv["languages"]))):
     selected.append(cv["name"])
print(selected)
