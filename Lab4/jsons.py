# import json
# with open('sample-data.json', 'r') as file:
#     data = json.load(file)

# output = {
#     "totalCount": str (len(data['imdata'])),
#     "imdata": []
# }

# for item in data ['imdata']:
#     l1_phys_if = item ['l1PhysIf']['attributes']

# format_interface = "{:<36} {:<36} {:<36}".format (
#     l1_phys_if ['adminSt'],
#     l1_phys_if ['bw'],
#     l1_phys_if ['mode']
# )

# print(format_interface)
# print("="*80)
# print(f"Total count {output['totalCount']}")


import json

#dn / fecMode / mtu

with open("sample-data.json", "r") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 85)
print("{:<50} {:<20} {:<8} {}".format("DN", "Description", "Speed", "MTU"))
print("-" * 85)

for interface in data['imdata']:
    dn = interface['l1PhysIf']['attributes']['dn']
    description = interface['l1PhysIf']['attributes'].get('descr', '')
    speed = interface['l1PhysIf']['attributes'].get('speed', '')
    mtu = interface['l1PhysIf']['attributes'].get('mtu', '')

    print("{:<50} {:<20} {:<8} {}".format(dn, description, speed, mtu))