import process from "node:process";
import { promises as fs } from "node:fs";

const argv = process.argv.slice(2);

if (argv.length != 1) {
  console.error(`Expected exactly 1 argument (a path) to be passed but got ${argv.length}`);
  process.exit(1);
}

const path = argv[0];

const content = await fs.readFile(path, "utf-8");
const countOfWordsContainingEs = content
  .split(" ")
  .filter(word => word.includes("e"))
  .length;

  console.log(countOfWordsContainingEs);