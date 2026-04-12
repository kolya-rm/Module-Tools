jq -r '.[[.[].name] | indices("Daniel") | last + 1 : . | length] | .[].name' ./scores.json
