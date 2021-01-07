"""
function valuePair(obj1, obj2, key) {
    let val1 = obj1[key];
    let val2 = obj2[key];
    const arr = [val1, val2];
  
    return arr;
}
"""

def value_pair(dict1, dict2, key):
    val1 = dict1.keys
    val2 = dict2.keys
    array = [val1, val2]

    print(array)

value_pair({"Joe"},{"Larry"},"Harry")
