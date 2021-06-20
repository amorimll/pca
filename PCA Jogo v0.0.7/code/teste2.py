import json
with open('data/form.json') as f:
        form = json.load(f)

def write_data(new_data, filename='data/data_teste.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        temp = file_data["players"]
        temp.append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)

y = {"nome":form['nome'],
     "pontos": 50
    }
     
write_data(y)