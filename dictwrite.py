import csv
details = [{"f_name": "Meena", "l_name": "Natarajan", "phone": "3344455567"}, {"f_name": "Tarush", "l_name": "Pranav", "phone": "3344455990"}]
keys = ["f_name","l_name","phone"]
with open('details.csv','w',newline='') as details_file:
    writer = csv.DictWriter(details_file, filednames=keys)
    writer.writeheader()
    writer.writerows(details)
    
details_file.close()