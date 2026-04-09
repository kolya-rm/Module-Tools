import scores from "./scores.json" with { type: "json" };

let mi = 0;
for(let i = 1; i < scores.length; i++) {
  if (scores[i].score > scores[mi].score) {
    mi = i;
  }
}

console.log(scores[mi].name);