import unittest

class Password:
    def ValidPasswordUnittest(self,psw):
        numCounter = 0
        bigLetterCounter = 0
        strnumbers = ["1","2","3","4","5","6","7","8","9","0"]
        specialCharacters = ["!","@","#","$","%","^","&","*","(",")","-","+","?","_","=",",","<",">","/"]
        specialCharacterCounter = 0
        if type(psw) is str:
            for i in psw:
                if i in strnumbers:
                    numCounter+=1
                if i.isupper():
                    bigLetterCounter+=1
                if i in specialCharacters:
                    specialCharacterCounter+=1
            if numCounter>=3 and bigLetterCounter >=1 and specialCharacterCounter>=1:
                return True
            else:
                return False
        else:
            raise Exception("Bad password type!")

    def ValidPasswordDocTest(self, psw):
        """ Takes password as a string and if it contains 3 or more numbers, 1 or more capital letter and 1 or more
        special character it returns True, in other cases it returns False.
        #p = Password()
        >>> p.ValidPasswordDocTest('123Slowo_')
        True
        >>> p.ValidPasswordDocTest('+_1S2l3O4W5o_+')
        True
        >>> p.ValidPasswordDocTest('++++++++13171461UUCFSKBJS')
        True
        >>> p.ValidPasswordDocTest('421S+')
        True
        >>> p.ValidPasswordDocTest('')
        False
        >>> p.ValidPasswordDocTest('12Slowo_')
        False
        >>> p.ValidPasswordDocTest('123slowo_')
        False
        >>> p.ValidPasswordDocTest('123Slowo')
        False
        >>> p.ValidPasswordDocTest(4628)
        Traceback (most recent call last):
        ...
        Exception: Bad password type!
        >>> p.ValidPasswordDocTest(-4926)
        Traceback (most recent call last):
        ...
        Exception: Bad password type!
        >>> p.ValidPasswordDocTest(-5)
        Traceback (most recent call last):
        ...
        Exception: Bad password type!
        >>> p.ValidPasswordDocTest(-24.42)
        Traceback (most recent call last):
        ...
        Exception: Bad password type!
        >>> p.ValidPasswordDocTest(['123Slowo_'])
        Traceback (most recent call last):
        ...
        Exception: Bad password type!
        >>> p.ValidPasswordDocTest([34])
        Traceback (most recent call last):
        ...
        Exception: Bad password type!
        >>> p.ValidPasswordDocTest({})
        Traceback (most recent call last):
        ...
        Exception: Bad password type!
        >>> p.ValidPasswordDocTest(('123','Slowo','_'))
        Traceback (most recent call last):
        ...
        Exception: Bad password type!
        """
        numCounter = 0
        bigLetterCounter = 0
        strnumbers = ["1","2","3","4","5","6","7","8","9","0"]
        specialCharacters = ["!","@","#","$","%","^","&","*","(",")","-","+","?","_","=",",","<",">","/"]
        specialCharacterCounter = 0
        if type(psw) is str:
            for i in psw:
                if i in strnumbers:
                    numCounter+=1
                if i.isupper():
                    bigLetterCounter+=1
                if i in specialCharacters:
                    specialCharacterCounter+=1
            if numCounter>=3 and bigLetterCounter >=1 and specialCharacterCounter>=1:
                return True
            else:
                return False
        else:
            raise Exception("Bad password type!")

validPassword = Password().ValidPasswordUnittest

class ValidPasswordTest(unittest.TestCase):
    def test_good_password(self):
        self.assertTrue(validPassword("123Slowo_"))
    
    def test_good_password_many_characters(self):
        self.assertTrue(validPassword("14917-29350272007SLOFAHOANVFA_-+="))

    def test_good_password_short(self):
        self.assertTrue(validPassword("125S_"))

    def test_good_password_mixed_characters(self):
        self.assertTrue(validPassword("+_1S2l3O4W5o_+"))

    def test_good_password_special_characters_first(self):
        self.assertTrue(validPassword("++++++++13171461UUCFSKBJS"))

    def test_bad_password_empty_string(self):
        self.assertFalse(validPassword(""))

    def test_bad_password_too_little_numbers(self):
        self.assertFalse(validPassword("12Slowo_"))

    def test_bad_password_no_number(self):
        self.assertFalse(validPassword("Slowo_"))

    def test_bad_password_no_big_letter(self):
        self.assertFalse(validPassword("1412_-+="))

    def test_bad_password_no_special_character(self):
        self.assertFalse(validPassword("75214SHGSJNHifhsh"))

    def test_bad_password_without_needed_characters(self):
        self.assertFalse(validPassword("hslidfhyiafaghdghspahfiafaluhfiahyfaoifyaihfafoiahyfi"))


    def test_exception_int_not_str(self):
        self.assertRaises(Exception, validPassword, 3413)

    def test_exception_list_with_good_psw_not_str(self):
        self.assertRaises(Exception, validPassword, ["123Slowo_"])

    def test_exception_empty_list_not_str(self):
        self.assertRaises(Exception, validPassword, [])

    def test_exception_tuple_not_str(self):
        self.assertRaises(Exception, validPassword, ())

    def test_exception_dict_not_str(self):
        self.assertRaises(Exception, validPassword, {})

    def test_exception_negative_int_not_str(self):
        self.assertRaises(Exception, validPassword, -41)

    def test_exception_float_not_str(self):
        self.assertRaises(Exception, validPassword, 51.1341)

    def test_exception_negative_float_not_str(self):
        self.assertRaises(Exception, validPassword, -5.13)
    

if __name__ == "__main__":
    import doctest
    # doctest.testmod()
    doctest.testmod(extraglobs={'p': Password()})
