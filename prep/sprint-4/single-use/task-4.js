import scores from "./scores.json" with { type: "json"};

let di = 0;

for (let i = 0; i < scores.length; i++) {
  if (scores[i].name === "Daniel") {
    di = i;
  }
}

for (let i = di + 1; i < scores.length; i++) {
  console.log(scores[i].name);
}