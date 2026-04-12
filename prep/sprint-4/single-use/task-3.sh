jq -r "sort_by(-.score) | .[0].name" ./scores.json
