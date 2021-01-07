"""
function adults(people) {
  const names = [];

  for (let i = 0; i < people.length; i += 1) {
    let person = people[i];
    if (person.age >= 18) {
      names.push(person.name);
    }
  }

  return names;
}
"""

def adults(people):
    names = []
    for