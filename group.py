"""An example of how to represent a group of acquaintances in Python."""


jill={"name":"jill","age":26,"job":"biologist","connections":{"friends":["zalika"],"partners":["john"]}}
zalika={"name":"zalika","age":28,"job":"artist","connections":{"friends":["jill"]}}
john = {"name":"john","age":27,"job":"writer","connections":{"partners":["jill"]}}
nash = {"name":"nash","age":34,"job":"chef","connections":{"cousins":["john"],"tenant":["zalika"]}}

my_group =[jill,zalika,john,nash]


### now add some comprehensions

max_age = max([ person["age"] for person in my_group])
n_relations = sum([ len(person["connections"][key]) for person in my_group for key in person["connections"]  ])
mean_relations=n_relations/len(my_group)

print(max_age)
print(mean_relations)




