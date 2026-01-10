import csv, pathlib, os,random

"""
script that writes data to a csv file for insertion
into a district-education database

"""

path = pathlib.Path.cwd()  #parent directory



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

def write_address(addrs:list):
    num = 1
    with open(os.path.join(path,'data/seeds/address.csv'),'w') as file:
        file_writer = csv.DictWriter(file,['id','gh_post_gps','area_id'])
        file_writer.writeheader()
        for adrs in addrs:
            file_writer.writerow({'id':num,'gh_post_gps':adrs,'area_id':random.randint(1,32)})

