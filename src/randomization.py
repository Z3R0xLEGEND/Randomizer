class RandomizerNoSeedError (Exception) :
    """Exception raised when no seed was set for the Randomizer

            Attributes:
                message -- explanation of the error
    """

    def __init__ (self,
                      message = "No seed was set for the Randomizer use .set_seed(int) before calling method !") : #Initialization of the class
        """Init the RandomizerNoSeedSetError wit the message attribute"""

        self.message = message #The explanation showed
        super().__init__(self.message) #Reinit the exception with the message

    def __str__ (self) : #Showed on raise
        return f"{self.message}" #Return the message error

class Randomizer :
    """Implementation of the Mersenne Twister PRNG version 32bits (MT19937)
        This algorithm has a repetition period of 2^(19937) − 1 and is very fast
        The particularity of this implementation is that the randomizer is waiting for a seed and you can retrieve it with the get_seed() method.

            Attributes:
                w, n, m, r, a, b, c, s, t, u, d, l, f, loyer_mask, upper_mask -- private constants of the algorithm they never change
                current_seed -- the seed used to generate the random numbers
                matrix -- the matrix used to store the random values
                index, n -- privates indexes to get the value from the list

            Methods:
                set_seed(seed):
                    set the seed used by the algorithm
                get_seed ():
                    get the current seed used by the algorithm
                twist ():
                    regenerate the matrix when a number is not in it's range
                extract_number():
                    extract a number from the matrix
                random():
                    return a random floating point between 0 and 1
                randint(a, b):
                    return a random integer between a and b
                shuffle(element):
                    shuffle a given list and return it
                sample(element, number_of_items = 1):
                    pick random items in the elements, number_of_items define how many items needs to be picked
                boolean(probability = 0.5):
                    return True or False with probability the probability to have a True

            Exceptions:
                RandomizerNoSeedSetError: the class raises this exception when no seed was given to the Randomizer
    """

    def __init__(self):
        """Initialize the Randomizer class and all it's parameters"""

        self.__w = 32 #Word size in number of bits
        self.__n = 624 #Degree of recurrence
        self.__m =  397 #Middle word
        self.__r = 31 #Separation point of one word or the number of bits of the lower bitmask, 0 ≤ r ≤ w - 1
        self.__a = 0x9908B0DF #Coefficients of the rational normal form twist matrix

        self.__b, self.__c = 0x9D2C5680, 0xEFC60000 #Tempering bitmasks
        self.__s, self.__t = 7, 15 #Tempering bit shifts

        self.__u = 11 #Additional Mersenne Twister tempering bit shifts/masks
        self.__d = 0xFFFFFFFF #Additional Mersenne Twister tempering bit shifts/masks
        self.__l = 18 #Constant
        self.__f = 1812433253 #Constant

        self.__lower_mask = 0xFFFFFFFF #Lower bit mask
        self.__upper_mask = 0x00000000 #Upper bit mask

        self.__current_seed = None #The current generation seed

    def set_seed(self,
                    seed):
        """
        Set the current generation seed to use for the randomization

            Parameters:
                seed (string): the seed to use for the randomization
            Returns:
                None
            Raises:
                None
        """

        self.__current_seed = seed
        self.__matrix = [None for i in range(self.__n)] #Array to store the state of the generator
        self.__matrix[0] = seed #Set the first item in the matrix as the seed number
        self.__index = self.__n #Set the index as default

        for index in range(1, self.__n): #For the range of the matrix
            generated = self.__f * (self.__matrix[index - 1] ^ (self.__matrix[index - 1] >> (self.__w-2))) + index #Get the value for the index in the matrix
            self.__matrix[index] = generated & 0xffffffff #Set the value of the item

    def get_seed (self) :
        """
        Get the current randomization seed

            Parameters:
                None
            Returns:
                seed (string): the seed used by the randomizer
            Raises:
                None
        """

        return self.__current_seed

    def __twist(self):
        """
        Regenerate a matrix for new values outside the matrix

            Parameters:
                None
            Returns:
                None
            Raises:
                None
        """

        for index in range(0, self.__n): #For the range of the matrix
            x = (self.__matrix[index] & self.__upper_mask) + (self.__matrix[(index + 1) % self.__n] & self.__lower_mask) #Shift the x value
            xA = x >> 1 #hift again the value

            if (x % 2) != 0: #If the value is not pair
                xA = xA ^ self.__a #Shift again the value

            self.__matrix[index] = self.__matrix[(index + self.__m) % self.__n] ^ xA #Set the value of the item in the matrix

        self.__index = 0 #Set the current index to 0

    def __extract_number(self):
        """
        Extract a number from the matrix and shift it

            Parameters:
                None
            Returns:
                number (float): return the extracted number from the matrix
            Raises:
                None
        """

        if self.__current_seed == None :
            raise RandomizerNoSeedError()

        if self.__index >= self.__n: #If the index is not in the matrix
            self.__twist() #Twist the matrix

        #Tempering the number as defined by the Mersenne Twister algorithm
        y = self.__matrix[self.__index] #Get the value
        y = y ^ ((y >> self.__u) & self.__d)
        y = y ^ ((y << self.__t) & self.__c)
        y = y ^ ((y << self.__s) & self.__b)
        y = y ^ (y >> self.__l)

        self.__index += 1 #Add one number to the index

        return y & 0xffffffff #Return the number added to the bitmask

    def random(self):
        """
        Get a uniform floating number between 0 and 1

            Parameters:
                None
            Returns:
                number (float): the random number
            Raises:
                None
        """

        return self.__extract_number() / 4294967296  #Return the extracted number divided by 2**w

    def randint(self,
                    a,
                    b):
        """
        Get a random integer between a and b

            Parameters:
                None
            Returns:
                number (int): the random number between a and b
            Raises:
                None
        """

        number = self.random() #Get a random number

        return int(number / (1 / (b - a)) + a) #Get the number in the range of a and b

    def shuffle(self,
                    element):
        """
        Shuffle an element

            Parameters:
                element (list): element to shuffle
            Returns:
                shuffled (lit): the shuffled elements
            Raises:
                None
        """

        shuffled = list(element) #Create a list if the element is not a list

        for i in range(10*len(X)): #Do 10*len(list) iterations to be sure to shuffle all elements
            a = self.randint(0, len(X)) #Get a random int
            b = self.randint(0, len(X)) #Get a random int
            shuffled[a], shuffled[b] = shuffled[b], shuffled[a] #Shuffle the two elements between them

        return shuffled #Return the shuffled list

    def sample (self,
                    element,
                    number_of_items=1):
        """
        Pick one or more element randomly from a list or str

            Parameters:
                element (list / str): the element to pick the random items from
                number_of_items (int): the number of items to pick from the element
            Returns:
                picked (list): the list of the choosen elements
            Raises:
                None
        """

        elements = list(element) #Create a list if the element is not a list

        if number_of_items == 1: #If only one item need to be returned
            return elements[self.randint(0, len(elements))] #Get the random item in the list
        else: #If more than one item need to be returned by the list
            picked = [] #The list of the picked elements
            for number in range(number_of_items): #For the number of elements to pick
                if len(elements) != 0: #If the list to pick the element from is not empty
                    a = self.randint(0, len(elements)) #Get the index of the element to pick
                    picked.append([elements[a]]) #Append the new picked element to the list to return
                    elements.remove(elements[a]) #Remove the picked element to don't get it again

            return picked #Return the picked elements

    def boolean(self,
                    probability = 0.5):
        return self.random() <= probability #Return True or False depending on the probability to return True
