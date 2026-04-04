import { program } from "commander";
import { promises as fs } from "node:fs";
import readline from "node:readline";
import process from "node:process";

program
  .name("concatenate-and-print-files-reproduction")
  .description("Print file content in the stdout.")
  .argument("[path...]", "the file path to process");

program.parse();

const argv = program.args;

let rl;

start();

function start() {
  if (argv.length === 0) {
    rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout,
    });
    recursiveReadlineAndPrint();
  } else {
    readAndPrintFiles();
  }
}

function recursiveReadlineAndPrint() {
  rl.on("SIGINT", () => {
    rl.close();
    process.exit(0);
  }); 
  rl.question("", input => {
    console.log(input);
    recursiveReadlineAndPrint();
  });
}

async function readAndPrintFiles() {
  const buffer = [];
  for (const path of argv) {
    buffer.push(await readFile(path));
  }
  for(const content of buffer) {
    if (content.startsWith("cat.js:")) {
      console.error(content);
    } else { 
      console.log(content);
    }
  }
}

async function readFile(path) {
  try {
    const content = await fs.readFile(path, "utf8");
    return content.toString().trim();
  } catch (error) {
    return `cat.js: ${path}: No such file or directory`;
  }
}
