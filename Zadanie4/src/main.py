class FizzBuzz:

    def game(self, num):
        if type(num) is int: 
            if num % 15 == 0:
                return "FizzBuzz"
            if num % 5 == 0:
                return "Buzz"
            if num % 3 == 0:
                return "Fizz"
            else:
                return num
        else:
            raise Exception("Error in FizzBuzz")
