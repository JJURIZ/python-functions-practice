"""
function valuePair(obj1, obj2, key) {
    let val1 = obj1[key];
    let val2 = obj2[key];
    const arr = [val1, val2];
  
    return arr;
}
"""
first_pair = {"name": "One", "location": "Remote", "age": 1}
second_pair = {"name": "Two", "location": "San Francisco"}

def value_pair(dict1, dict2, key):
    print(dict1)
    print(dict1[key])
    print(dict2)
    print(dict2[key])

    return [dict1[key], dict2[key]]

print(value_pair(first_pair, second_pair, "name"))

