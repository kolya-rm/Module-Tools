import { program } from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";

program
  .name("concatenate-and-print-files-reproduction")
  .description("Print file content in the stdout.")
  .argument("<path>, the file path to process");

program.parse();

const argv = program.args;