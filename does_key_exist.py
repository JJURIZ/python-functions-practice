"""
function doesKeyExist(obj, key) {
  return obj[key] !== undefined;
}
"""

def does_key_exist(dict, key):
    return dict[key] != None # Something wrong here if condition is False

print(does_key_exist({"Name": "Harry", "Name": "Larry"}, "Name"))
print(does_key_exist({"Name": "Harry", "Name": "Larry"}, "Banana"))
