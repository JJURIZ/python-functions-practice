"""
function doesKeyExist(obj, key) {
  return obj[key] !== undefined;
}
"""

def does_key_exist(obj, key):
    if key in obj:
        print(True)
    else: 
        print(False)

print(does_key_exist({"Name": "Harry", "Name": "Larry"}, "Name"))
print(does_key_exist({"Name": "Harry", "Name": "Larry"}, "Banana"))

# Why does None print after each line?
"""
https://www.educative.io/edpresso/how-to-check-if-a-key-exists-in-a-python-dictionary
"""

