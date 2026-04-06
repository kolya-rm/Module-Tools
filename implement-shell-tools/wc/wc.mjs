import { promises as fs, readFile } from "node:fs";
import { program } from "commander";

program
  .name("word-count")
  .description("word, line, and character count")
  .argument("[path...]", "path to file.");

program.parse();

const argv = program.args;
const options = program.opts();

start();

async function start() {
  const data = await collectData();
  console.log(data);
}

async function collectData() {
  if (!argv.length) {
    return [];
  }
  const data = [];
  for (const path of argv) {
    const datum = {};
    try {
      const stat = await fs.stat(path)
      if (stat.isDirectory()) {
        datum["s"] = "d";
      }
      if (stat.isFile()) {
        datum["s"] = "f";
        const content = (await fs.readFile(path)).toString();
        datum["l"] = content.match(/\n/g).length;
        datum["w"] = content.match(/\s/g).length;
        datum["c"] = content.length;
      }
    } catch (error) {
      datum["s"] = "e";
    }
    data.push(datum);
  }
  return data;
}