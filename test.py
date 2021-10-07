import json

with open ("orders.json", "r") as file:
        json_object = json.load(file)
        json_orders = json_object.get("orders")
        #print(json_orders[1])
        
for i in range(len(json_orders)):
    print(i, " - ", json_orders[i])