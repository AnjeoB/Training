 vehicles = [
	{'name':'Mark-X','cost':1200000},
	{'name':'Crown','cost':800000},
	{'name':'Prado','cost':4500000},
	{'name':'X4','cost':8000000},
	{'name':'CX5',:2900000}
	]

sorted_vehicles = sorted(vehicles, keys=lamda x: x('cost'), reverse=True)

for vehicle in sorted_vehicles:
	print(vehicle['name'],'-',vehicle['cost'])
