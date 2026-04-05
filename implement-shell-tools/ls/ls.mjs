import { program } from "commander";
import { promises as fs} from "node:fs"

const TERMINAL_WIDTH = 120;

program
  .name("list")
  .description("list directory contents")
  .argument("[path]", "path to file", ["."]);

program.parse()

const argv = program.args;

readDirAndPrintFiles();

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