# Mersenne Twister Randomizer :

Full python implementation of the Mersenne Twister PRNG version 32bits (MT19937).

This randomizer has the particularity to wait for a seed before starting generating random values,
it's current seed can also be retrieved by the __get_seed()__ method to store it for reproductions.

## How to import the Randomizer :

Multiple instance of the Randomizer can be created to generate values from different seed at the same time

![How to import the randomizer image](./pictures/how-to-import-it.png?raw=true "Importation of the Randomizer")

## How to set the seed to use :

You always need to set the seed to use before generating random values to do it just call __.set_seed(your_seed)__.

![How to set the seed to use image](./pictures/set_seed.png?raw=true "Set the seed to use")

## How to randomize the values generated :

To randomize the values generated a simple solution is to get a value changing everytime the code is run.
One of the simplest way to do it is to take the current computer time with __time.time()__ and convert it to an int.

![How to randomize the values image](./pictures/how-to-randomize-the-values.png?raw=true "Get the current time")

## How to get the current seed used by the Randomizer :

To get the current seed used by the Randomizer call the __.get_seed()__ method, it will return the current seed.

![How to get the current seed used image](./pictures/get_seed.png?raw=true "Get the current seed")

## Available method(s) :

The available methods for the Randomizer are :
   - __set_seed(number)__: set the seed for the random generation
   - __get_seed()__: to get the current seed used by the Randomizer
   - __random()__: return a uniform random between 0 and 1
   - __randint(a, b)__: return a random integer between a and b
   - __shuffle(element)__: shuffle a list or a str and return the shuffled items
   - __sample(element, number_of_items = 1)__: pick a given number of items from the element and return them
   - __boolean(probability = 0.5)__: return a boolean with probability the probability to return True

![Available method(s) image](./pictures/methods.png?raw=true "Methods available")

## Available exception(s) :

For the moment only one exception is necessary :
  - __RandomizerNoSeedError__ : this error happens when a method of the randomizer was called before a seed was set
  
![Available exception(s) image](./pictures/exceptions.png?raw=true "Exceptions available")
