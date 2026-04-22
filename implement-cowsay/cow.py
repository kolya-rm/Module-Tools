import argparse
import cowsay


animals = ["beavis", "cheese", "cow", "daemon", "daemon", "fox", "ghostbusters", "kitty", "meow", "miki", "milk", "octopus", "pig", "stegosaurus", "stimpy", "trex", "turkey", "turtle", "tux"]

parser = argparse.ArgumentParser(
  prog = "cowsay",
  description = "Make animals say things"
)

parser.add_argument("message", help = "The message to say.", nargs = "+")
parser.add_argument("--animal", help = "The animal to be saying things.", choices = animals)

args = parser.parse_args();

animal = args.animal
message = " ".join(args.message)

if animal == "beavis":
  cowsay.beavis(message)
elif animal == "cheese":
  cowsay.cheese(message)
elif animal == "daemon":
  cowsay.daemon(message)
elif animal == "fox":
  cowsay.fox(message)
elif animal == "ghostbusters":
  cowsay.ghostbusters(message)
elif animal == "kitty":
  cowsay.kitty(message)
elif animal == "meow":
  cowsay.meow(message)
elif animal == "miki":
  cowsay.miki(message)
elif animal == "milk":
  cowsay.milk(message)
elif animal == "octopus":
  cowsay.octopus(message)
elif animal == "pig":
  cowsay.pig(message)
elif animal == "stegosaurus":
  cowsay.stegosaurus(message)
elif animal == "stimpy":
  cowsay.stimpy(message)
elif animal == "trex":
  cowsay.trex(message)
elif animal == "turkey":
  cowsay.turkey(message)
elif animal == "turtle":
  cowsay.turtle(message)
elif animal == "tux":
  cowsay.tux(message)
else:
  cowsay.cow(message)
  