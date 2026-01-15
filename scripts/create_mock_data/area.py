import csv, pathlib, os

"""
script that writes data to a csv file for insertion
into a district-education database

"""

path = pathlib.Path.cwd()  #parent directory


sunyani_municipal_areas = [
    "Sunyani","Abesim","New Dormaa","Area 2",
    "Area 4","Zongo","Atronie","Asuakwa","Asufufu",
    "Baakoniaba","Kotokrom","New Town","Nkwabeng",
    "Watchman","Educational zone","Mireku","Gyaase",
    "Dominase","Penkwase West","Tonsuom","Nwawasua",
    "Sunyanitifi","Yawsae","Penkwase East","Nkrankrom",
    "Magazine","Ankobea","Ahenboboano","Atoase",
    "Atuahne","Antwikrom-Benu Nkwanta","Abetifi",
    "Airport","Nkwabeng North","Akuoko","Akokorakwadwo",
    "Lowcost","Abonsuam"
]

# write areas to file
num = 1
with open(os.path.join(path,'data/seeds/area.csv'),'w') as file:
    file_writer = csv.DictWriter(file,['id','name'])
    file_writer.writeheader()

    for area in sunyani_municipal_areas:
        file_writer.writerow({'id':num,'name':area})
        num += 1
