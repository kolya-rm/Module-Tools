import argparse

animals = ["beavis", "cheese", "cow", "daemon", "dragon", "fox", "ghostbusters","kitty", "meow", "miki", "milk", "octopus", "pig", "stegosaurus", "stimpy", "trex", "turkey", "turtle", "tux"]

parser = argparse.ArgumentParser(
  prog = "cowsay",
  description = "Make animals say things"
)

parser.add_argument("message", help = "The message to say.", nargs = "+")
parser.add_argument("--animal", help = "The animal to be saying things.", choices = animals)

args = parser.parse_args();

print(" ".join(args.message))