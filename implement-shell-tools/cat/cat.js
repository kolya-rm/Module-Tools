import { program } from "commander";
import { promises as fs } from "node:fs";
import readline from "node:readline";
import process from "node:process";

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
  for(const content of buffer) {
    if (content[0].startsWith("cat.js:")) {
      console.error(content[0]);
    } else {
      let n = 1; 
      for(const string of content) {
        if (options.n) {
          console.log(`${n.toString().padStart(6, " ")}  ${string}`);
          n++;
        } else if (options.b) {
          if (string) {
            console.log(`${n.toString().padStart(6, " ")}  ${string}`);
            n++;
          } else {
            console.log();
          }
        } else {
          console.log(string);
        }
      }
    }
  }
}

async function readFile(path) {
  try {
    const content = await fs.readFile(path, "utf8");
    return content.toString().trim().split("\n");
  } catch (error) {
    return [`cat.js: ${path}: No such file or directory`];
  }
}
