"""
function countScores(people) {
  const scoresObj = {};

  for (let i = 0; i < people.length; i += 1) {
    let personObj = people[i];
    let name = personObj.name;
    let score = personObj.score;

    if (scoresObj[name]) {
      scoresObj[name] += score;
    } else {
      scoresObj[name] = score;
    }
  }

  return scoresObj;
}
"""
peeps = [
    {"name": 'Pete', "score": 2},
    {"name": 'Dexter', "score": 2},
    {"name": 'Mike', "score": 2},
    {"name": 'Dexter', "score": 2},
    {"name": 'Mike', "score": 2},
    {"name": 'Pete', "score": 2},
    {"name": 'Dexter', "score": 2}
]

def count_scores(people):
    scores = {}
    for i in range(len(people)):
        if people[i]["name"] in scores:
            scores[people[i]["name"]] += people[i]["score"]
        else:
            scores[people[i]["name"]] = people[i]["score"]
    return scores


print(count_scores(peeps))
