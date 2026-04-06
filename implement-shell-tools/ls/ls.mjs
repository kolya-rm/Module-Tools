import { program } from "commander";
import { promises as fs} from "node:fs"

const TERMINAL_WIDTH = 120;
const NAME_PADDING = 8;

program
  .name("list")
  .description("list directory contents")
  .option("-a", "Include directory entries whose names begin with a dot (‘.’).")
  .option("-1", "(The numeric digit “one”.) Force output to be one entry per line.")
  .argument("[path...]", "path to entries to list");

program.parse()

const argv = program.args;
const options = program.opts();

start();

async function start() {
  const output = [];
  const files = [];
  const directories = [];
  
  await checkInput(output, files, directories);
  if (files.length) {
    output.push(formatFilesOutput(files));
  }
  await formatDirectoriesOutput(output, directories, files.length);

  for(const string of output) {
    if (string.startsWith("ls.mjs")) {
      console.error(string);
    } else {
      console.log(string);
    }
  }
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
  if (options[1]) {
    return files.join("\n");
  }
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

async function formatDirectoriesOutput(output, directories, isFilesExist) {
  const isSingleDirectory = directories.length === 1;
  for(let i = 0; i < directories.length; i++) {
    let files = await fs.readdir(directories[i]);
    if (options.a) {
      files.push(".", "..");
    } else {
      files = files.filter(file => !file.startsWith("."));
    }
    files.sort();
    let directoryOutput = formatFilesOutput(files);
    if (isFilesExist || !isSingleDirectory) {
      directoryOutput = `${directories[i]}:\n${directoryOutput}`;
    }
    if (isFilesExist || !isSingleDirectory && i) {
      directoryOutput = `\n${directoryOutput}`;
    }
    output.push(directoryOutput);
  }
}
