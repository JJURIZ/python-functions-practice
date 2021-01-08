"""
function oddRange(end) {
  const arr = [];

  for (let i = 1; i <= end; i += 2) {
      arr.push(i);
  }

  return arr;
}
"""

def odd_range(start, end):
    arr = []
    for num in range(start, end + 1):
        if num % 2 != 0:
            arr.append(num)
    return arr

print(odd_range(0, 13))