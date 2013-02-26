import unittest
import ipdb
import myregexp
from myregexp import * 

class RegexpAutotester(unittest.TestCase):

    def setUp(self):
        pass

    @classmethod
    def add_success_test(cls,method,example_list):
        #success_test = cls.create_success_test(method, example_list)
        def success_test(self):
            for test_string in example_list:
                match = method(test_string)
                self.assertTrue(match,msg = "%s should succeed on %s" % (method.__name__,  test_string))
        setattr(cls, 'test_%s_success' % method.__name__, success_test)

    @classmethod
    def add_failure_test(cls,method,example_list):
        def failure_test(self):
            for test_string in example_list:
                match = method(test_string)
                msg = "%s should fail on %s" % (method.__name__, test_string)
                self.assertFalse(match,msg = msg)
        setattr(cls, 'test_%s_failure' % method.__name__, failure_test)

    @classmethod
    def add_tests(cls,method,success_list,failure_list):
        cls.add_success_test(method,success_list)
        cls.add_failure_test(method,failure_list)

    def test_profile_pictures_success(self):
        profile_id, picture_id = profile_pictures('/profile/3/picture/10')   
        self.assertEqual('3', profile_id)
        self.assertEqual('10',picture_id)

    def test_profile_pictures_failure(self):
        groups = profile_pictures('/profile/f/picture/10')   
        self.assertFalse(groups)

RegexpAutotester.add_success_test(starts_with_apple, ['apple','apple bottom jeans','apple mac'])
RegexpAutotester.add_failure_test(starts_with_apple,['aapple','bottom apple jeans','mac apple'])

RegexpAutotester.add_success_test(ends_with_apple,['apple','bottom jeans apple','mac apple'])
RegexpAutotester.add_failure_test(ends_with_apple,['apple hey','bottom apple jeans','apple top'])

RegexpAutotester.add_success_test(contains_apple,['apple','apple bottom jeans','apple mac'])
RegexpAutotester.add_failure_test(contains_apple,['hey ','bottom  jeans','mac '])

#Character Classes
RegexpAutotester.add_tests(leet_n00b,['n0ob','no0b','noob','n00b'],['n0b','nob','nob'])
RegexpAutotester.add_tests(leet_password,['p@s$w0rd'],['passwor'])

#Named Character Classes
RegexpAutotester.add_tests(valid_telephone,['285-8133'],['26-8133','2458133'])
RegexpAutotester.add_tests(valid_license_plate,['AB1234-12'],['aB1234-19'])

#Repetition
RegexpAutotester.add_tests(mexico_goal,['goal','gooaaaal','goaal'],['gol ','gal'])

#General Practice
RegexpAutotester.add_tests(twitter_page,['/profile/123','/profile/1'],['/hey/profile/1','/profile/123/asdfasdfas'])
RegexpAutotester.add_tests(valid_email,['haynorb@gmail.com','h@g.edu'],['ben@yahoo','ben@yahoo@yahoo.com'])

#Grouping
RegexpAutotester.add_tests(regex_awesome,['regular expressions are really awesome!', 'regular expressions are really really really awesome!'],
        ['regular expressions are awesome!','regular expressions should burn for eternity'])

if __name__=='__main__':
    loader = unittest.TestLoader()
    matches = [re.search('test_(\w+)_success',method) for method in dir(RegexpAutotester)]
    non_zero_matches = filter(lambda x: bool(x), matches)
    filtered_methods = [match.group(1) for match in non_zero_matches]
    print 'Enter a method from the following list, or "all" to test everything'
    print "\n".join(filtered_methods)
    method_name = raw_input()
    if method_name == 'all':
        method_name = ''
    loader.testMethodPrefix = 'test_%s' % method_name
    suite = loader.loadTestsFromTestCase(RegexpAutotester)
    unittest.TextTestRunner(verbosity=2).run(suite)

