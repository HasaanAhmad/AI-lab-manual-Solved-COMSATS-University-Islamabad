# LAB 5 (HASAAN AHMAD SP22-BSE-017 )
sample_dict = {
    "name": "Hasaan",
    "age": 21,
    "salary": 12000,
    "city": "Islamabad"
}

keys = ["name", "salary"]

new_dict = {key: sample_dict[key] for key in keys}

print(new_dict)
