"""
function tripler(array) {
  const arr = [];

  for ( i = 0; i < array.length; i += 1) {
    let num = array[i];
    arr.push(num * 3);
  }

  return arr;
}

function oddRange(end) {
  const arr = [];

  for (let i = 1; i <= end; i += 2) {
      arr.push(i);
  }

  return arr;
}
"""

def tripler(array):
  result = []

  for i in range(len(array)):
    num = array[i]
    multiple = num * 3
    result.append(multiple)

  return result

print(tripler([3,9,27]))