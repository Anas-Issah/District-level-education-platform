import csv, pathlib, os,random

"""
script that writes data to a csv file for insertion
into a district-education database

"""




# ADDRESS
def create_address()-> str:

    first = random.randint(0,9999)
    second = random.randint(0,9999)

    if first < 10:
        first = '000' + str(first)
    elif first < 100:
        first = '00' + str(first)
    elif first < 1000:
        first = '0' + str(first)

    if second < 10:
        second = '000' + str(second)
    elif second < 100:
        second = '00' + str(second)
    elif second < 1000:
        second = '0' + str(second)

    return 'BS-'+ str(first) + '-' + str(second)

# Write addresses to file
def header_writer():
    path = os.path.join(pathlib.Path.cwd(),'data/seeds/address.csv')
   
    if pathlib.Path(path).exists() == False:
        with open(path,'w') as file:
            file_writer = csv.DictWriter(file,['id','gh_post_gps','area_id'])
            file_writer.writeheader()

def write_address(addrs:list):

    header_writer()
    path = pathlib.Path.cwd()  #parent directory

    # get number of areas
    with open(os.path.join(path,'data/seeds/area.csv'),'r') as file:
        num_areas = len([n for n in csv.DictReader(file,delimiter=',')])

    num = len(get_address())
    with open(os.path.join(path,'data/seeds/address.csv'),'a') as file:
        file_writer = csv.writer(file)
        for adrs in addrs:
            num += 1
            file_writer.writerow([num,adrs,random.randint(1,num_areas)])
            

def write_single_addres():

    header_writer()
    path = pathlib.Path.cwd()  #parent directory

    num = len(get_address())

    with open(os.path.join(path,'data/seeds/area.csv'),'r') as file:
        num_areas = len([n for n in csv.DictReader(file,delimiter=',')])
       

    with open(os.path.join(path,'data/seeds/address.csv'),'a') as file:
        file_writer = csv.writer(file)
        file_writer.writerow([num + 1,create_address(),random.randint(1,num_areas)])

def get_address():
    
    try:
        path = pathlib.Path.cwd()  #parent directory
        with open(os.path.join(path,'data/seeds/address.csv'),'r') as file:
            addresses = [i for i in csv.DictReader(file,delimiter=',')]
            return addresses
        
    except FileNotFoundError:
        return []

