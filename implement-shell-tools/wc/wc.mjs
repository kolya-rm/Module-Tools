import { promises as fs } from "node:fs";
import { program } from "commander";


const NUMBER_PADDING = 8;
const ERROR_PREFIX = "wc.mjs:"
const TOTAL_PATH = "total";


program
  .name("word-count")
  .description("word, line, and character count")
  .option("-l", "The number of lines in each input file is written to the standard output.")
  .option("-w", "The number of words in each input file is written to the standard output.")
  .option("-c", "The number of characters in each input file is written to the standard output.")
  .argument("[path...]", "path to file.");

program.parse();

const argv = program.args;
const options = program.opts();


start();

async function start() {
  const data = await collectData();
  const output = formatOutput(data);

  printOutput(output);
}

async function collectData() {
  const data = [];

  if (!argv.length) {
    const content = await getStdinContent();
    data.push(collectFileData({}, content));
  } else {
    for (const path of argv) {
      const datum = {};
      try {
        const stat = await fs.stat(path)
        if (stat.isDirectory()) {
          datum["s"] = "d";
        }
        if (stat.isFile()) {
          const content = (await fs.readFile(path)).toString();
          collectFileData(datum, content);
        }
      } catch (error) {
        datum["s"] = "e";
      }
      datum["p"] = path;
      data.push(datum);
    }
  }
  return data;
}

async function getStdinContent() {
  return new Promise((resolve) => {
    let content = "";

    process.stdin.on("data", input => {
      content += input;
    });
    process.stdin.on("close", () => {
      resolve(content);
    });
  });
}

function collectFileData(datum, content) {
  const newLineCharacters = content.match(/\n/g);

  datum["s"] = "f";
  datum["l"] = newLineCharacters ? newLineCharacters.length : 0;
  datum["w"] = content.trim().split(/\s+/).length;
  datum["c"] = content.length;

  return datum;
}

function formatOutput(data) {
  const errors = [];
  const files = [];

  for(const datum of data) {
    switch(datum.s) {
      case "d":
        errors.push(`${ERROR_PREFIX} ${datum.p}: Is a directory`);
        break;
      case "f":
        files.push(formatFileOutput(datum));
        break;
      default:
        errors.push(`${ERROR_PREFIX} ${datum.p}: open: No such file or directory`);
        break;
    }
  }
  
  if (data.length > 1) {
    files.push(formatTotalOutput(data));
  }
  
  return errors.concat(files);
}

function formatFileOutput(datum) {
  let result = "";
  
  if (!options.l && !options.w && !options.c) {
    result = `${formatOutputNumber(datum.l)}${formatOutputNumber(datum.w)}${formatOutputNumber(datum.c)}`;
  } else {
    if (options.l) {
      result = `${result}${formatOutputNumber(datum.l)}`;
    }
    if (options.w) {
      result = `${result}${formatOutputNumber(datum.w)}`;
    }
    if (options.c) {
      result = `${result}${formatOutputNumber(datum.c)}`;
    }
  }

  if (datum.p) {
    result = `${result} ${datum.p}`;
  }

  return result;
}

function formatTotalOutput(data) {
  const total = {s: "t", l: 0, w: 0, c: 0, p: TOTAL_PATH};

  for (const datum of data) {
    if (datum.s === "f") {
      total.l += datum.l;
      total.w += datum.w;
      total.c += datum.c;
    }
  }
  
  return formatFileOutput(total);
}

function formatOutputNumber(number) {
  return number.toString().padStart(NUMBER_PADDING, " ");
}

function printOutput(output) {
  for (const string of output) {
    if (string.startsWith(ERROR_PREFIX)) {
      console.error(string);
    } else {
      console.log(string);
    }
  }
}
