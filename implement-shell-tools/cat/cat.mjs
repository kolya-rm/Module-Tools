import { program } from "commander";
import { promises as fs } from "node:fs";
import readline from "node:readline";
import process from "node:process";
import console from "node:console";

program
  .name("concatenate-and-print-files-reproduction")
  .description("Print file content in the stdout.")
  .option("-n", "Number the output lines, starting at 1.")
  .option("-b", "Number the non-blank output lines, starting at 1.")
  .argument("[path...]", "the file path to process");

program.parse();

const argv = program.args;
const options = program.opts();

let rl;

start();

function start() {
  console.log(options.n);

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
  printReadBuffer(buffer);
}

async function readFile(path) {
  try {
    const content = await fs.readFile(path, "utf8");
    return content.toString().trim().split("\n");
  } catch (error) {
    return [`cat.js: ${path}: No such file or directory`];
  }
}

function printReadBuffer(buffer) {
  for (const content of buffer) {
    if (content[0].startsWith("cat.js:")) {
      console.error(content[0]);
    } else if (options.b) {
      printWithFlagB(content);
    } else if (options.n) {
      printWithFlagN(content);
    } else {
      printWithoutFlag(content);
    }
  }
}

function printWithFlagB(content) {
  let n = 1;
  for (const string of content) {
    if (string) {
      console.log(`${n.toString().padStart(6, " ")}  ${string}`);
      n++;
    } else {
      console.log();
    }
  }
}

function printWithFlagN(content) {
  let n = 1;
  for (const string of content) {
    console.log(`${n.toString().padStart(6, " ")}  ${string}`);
    n++;
  }
}

function printWithoutFlag(content) {
  for (const string of content) {
    console.log(string);
  }
}
