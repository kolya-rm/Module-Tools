import { program } from "commander";
import { promises as fs} from "node:fs"

const TERMINAL_WIDTH = 120;
const NAME_PADDING = 8;

program
  .name("list")
  .description("list directory contents")
  .argument("[path...]", "path to file");

program.parse()

const argv = program.args;

start();

async function start() {
  const output = [];
  const files = [];
  const directories = [];
  
  await checkInput(output, files, directories);

  output.push(formatFilesOutput(files));

  console.log("output:", output);
  console.log("files:", files);
  console.log("directories:", directories);
}

async function checkInput(output, files, directories) {
  if (!argv.length) {
    directories.push(".");
    return;
  }
  for (const path of argv) {
    try {
      const stat = await fs.stat(path);
      if (stat.isFile()) {
        files.push(path);
      }
      if (stat.isDirectory()) {
        directories.push(path);
      }
    } catch (error) {
      output.push(`ls.mjs:  ${path}: No such file ore directory`);
    }
  }
  files.sort();
  directories.sort();
}

function formatFilesOutput(files) {
  let maxLength = 0;
  for (const name of files) {
    if (maxLength < name.length) {
      maxLength = name.length;
    }
  }

  let padLength = 0;
  while (padLength < maxLength) {
    padLength += NAME_PADDING;
  }

  let output = "";
  let lineLength = 0;
  for (const name of files) {
    output += name.padEnd(padLength, " ");
    lineLength += padLength;
    if (TERMINAL_WIDTH - lineLength < padLength) {
      output += "\n";
      lineLength = 0;
    }
  }
  return output;
}

async function readDirAndPrintFiles() {
  let path = argv[0] ? argv[0] : ".";

  const rawFiles = await fs.readdir(path);
  const files = rawFiles.filter(file => !file.startsWith("."));

  let maxLength = 0;
  for (const name of files) {
    if (maxLength < name.length) {
      maxLength = name.length;
    }
  }

  let padLength = 0;
  while (padLength < maxLength) {
    padLength +=8;
  }

  let output = "";
  let lineLength = 0;
  for (const name of files) {
    output += name.padEnd(padLength, " ");
    lineLength += padLength;
    if (TERMINAL_WIDTH - padLength < lineLength) {
      output += "\n";
      lineLength = 0;
    }
  }

  console.log(output)
}