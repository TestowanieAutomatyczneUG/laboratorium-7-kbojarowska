class FizzBuzz:
    def game(self, num):
        """Take one integer number and if it's divisible by 15 it returns FizzBuzz,
        if it's divisible by 5 it return Buzz, if it's divisible by 3 it returns Fizz. In other cases it
        returns this number.
        # >>> f = FizzBuzz()
        >>> f.game(5)
        'Buzz'
        >>> f.game(3)
        'Fizz'
        >>> f.game(15)
        'FizzBuzz'
        >>> f.game(10)
        'Buzz'
        >>> f.game(9)
        'Fizz'
        >>> f.game(45)
        'FizzBuzz'
        >>> f.game(11)
        11
        >>> f.game(-4)
        -4
        >>> f.game(-12)
        'Fizz'
        >>> f.game(4.2)
        Traceback (most recent call last):
        ...
        Exception: Error in FizzBuzz
        >>> f.game([1,2,3])
        Traceback (most recent call last):
        ...
        Exception: Error in FizzBuzz
        >>> f.game({})
        Traceback (most recent call last):
        ...
        Exception: Error in FizzBuzz
        >>> f.game((1,3,5,2))
        Traceback (most recent call last):
        ...
        Exception: Error in FizzBuzz
        >>> f. game(5+5j)
        Traceback (most recent call last):
        ...
        Exception: Error in FizzBuzz
        >>> f.game(-5.2963)
        Traceback (most recent call last):
        ...
        Exception: Error in FizzBuzz
        """
        if type(num) is int: 
            if num % 15 == 0:
                return 'FizzBuzz'
            if num % 5 == 0:
                return 'Buzz'
            if num % 3 == 0:
                return 'Fizz'
            else:
                return num
        else:
            raise Exception("Error in FizzBuzz")

if __name__ == "__main__":
    # f = FizzBuzz()
    # print(f.game(3))
    import doctest
    # doctest.testmod()
    doctest.testmod(extraglobs={'f': FizzBuzz()})


    

