import { program } from "commander";
import { promises as fs } from "node:fs";
import { constants } from "node:fs";
import process from "node:process";

program
  .name("concatenate-and-print-files-reproduction")
  .description("Print file content in the stdout.")
  .argument("<path>, the file path to process");

program.parse();

const argv = program.args;

printFile(argv[0]);

function printFile(path) {
  fs.access(path, constants.R_OK).then(() => {
    fs.readFile(path, "utf8").then( data => {
      console.log(data.toString().trim());
    }).catch(error => {
      console.error(`cat.js: ${path}: ${error}}`);
    })
  }).catch(() => {
    console.error(`cat.js: ${path}: No such file or directory`);
  })
}