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

ppl = [
  {"name": 'Khalid Robinson', "age": 22},
  {"name": 'Ariel Winter', "age": 20},
  {"name": 'Post Malone', "age": 25},
  {"name": 'Willow Smith', "age": 17}
];


def adults(people):
    adult_list = []
    for i in range(len(people)):
        if people[i]["age"] >= 18:
            adult_list.append(people[i])

    return adult_list

print(adults(ppl))

