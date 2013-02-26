import re

'''
Lab inspired by NYU lecture @ http://www.cs.nyu.edu/~mohri/unix08/lect4.pdf
For more info go to: http://docs.python.org/2/library/re.html
''' 

#Anchors
'''i
Anchors are used to match at the beginning or
end of a line (or both).
^ means beginning of the line
$ means end of the line
'''

def contains_apple(test_string):
    '''Returns a match iff a string contains apple
    '''
    return re.search(r'apple',test_string)

def starts_with_apple(test_string):
    '''Should match all strings starting with apple. Hint, use ^
    '''
    return None

def ends_with_apple(test_string):
    '''Returns a match iff a string ends with apple. Hint, use $

    '''
    return None

#Character Class
'''
Character classes [] can be used to match
any specific set of characters
b[eor]at matches beat, brat, boat

Negated character classes:
[^eor] will match any characer except e,o, or r.

which of the following match b[^eo]at?
I beat a brat on a boat.  Include the answer below.
'''
def leet_n00b(test_string):
    '''Should match noob, where the o may be replaced by a 0
    '''
    return None

def leet_password(test_string):
    '''Write a regexp to match password, where the a
    may be replaced by @, the s with $, the o with 0.
    '''
    return None

#Named character classes, character ranges
'''
Because it is so common to match a digit or an alphanumeric character,
most regexp engines have special character classes 
The digits 0-9 can be matched as [0123456789],\d, [0-9]

For all lower case, upper case letters use [a-z], or [A-Z]

All letters: [a-zA-Z]
'''

def valid_telephone(test_string):
    '''Matches phone numbers of the form digit digit digit - digit digit digit digit
    e.g. 285-8133
    '''
    return None

def valid_license_plate(test_string):
    '''Matches license plates of the form capital letter capital letter number number number number - number number
    e.g.
    AB1234-12
    AC1451-12

    Does not match
    aB1234-12
    AB123412
    '''
    return None


#Repetiion
''' Often you want to match 0 or more, one or more, or some specific
range of characters.  a* represents 0 or more occurences of a.
a+ represents 1 or more occurences of a
a? matches 0 or 1 occurence of a
a{1,3} matches 1 to 3 occurence of a
a{3} matches exactly 3 occurences of a
a{3,} matches three or more occurrences of a
a{,3} matches up to three occurences of a
'''
def mexico_goal(test_string):
    ''' g, followed by one or more o's, one or more a's, one or more l's.
    Should match goooal goaaaal gooooaaaalll
    '''
    return None

#Now that you know more about character ranges, redo valid_telephone, valid_license_plate 
#With a cleaner regular expression

#General practice
def twitter_page(test_string):
    '''Matches twitter userpages of the form '/profile/1' profile/1
    Note. It should not match pages of the form 'hey/profile/1', or profile/1/more_stuff'
    Hint: use the anchor characters ^, $
    '''
    return None

def valid_email(test_string):
    '''The full details of allowed e-mail addresses is reasonably complicated.  
    See the official regular expression for matching e-mail below:
    at http://www.regular-expressions.info/email.html
    
    For here, I think of a valid e-mail as some letters,numbers,underscores , followed by
    an @ followed by some letters, a ., and some more letters.

    Matches: 
    'haynorb@gmail.com'
    'ben@meltwator.org'
    'ben_123@gmail.com'
    Failures
    'ben@yahoo'
    'ben@yahoo@yahoo.com'
    '''
    return None


#Grouping
'''Often you'll want to repeat an entire expression.
Suppose you want to match regex of the form
regex are really really really really awesome!.  Possibly more.
This can be acheived by grouping 'really ' with parenthesis
'''

#Example
def regex_awesome(test_string):
    return None


#Capture Groups.
'''Often we want to do something with captured groups. 
Imagine the following url for viewing the user with id 3's 
5th picture.
/profile/3/picture/5.
You want to fetch the 3, 5, an do something with them.  The code
below does just that

'''
def profile_pictures(test_string):
    match = re.search('^/profile/(\d+)/picture/(\d+)$',test_string)
    if match:
        groups = match.groups()
        return groups
    else:
        return None

'''
Try it out by opening a terminal and entering the following
ipython

From the ipython shell enter the following

import myregexp
myregexp.profile_pictures('/profiles/3/pictures/5')
'''

#CHALLENGE PROBLEM
def get_cookie_info(test_string):
    ''' 
    Used for scraping information from 
    "Set-Cookie" headers in HTTP responses.
    
    Given a string of the form:
    Set-Cookie: name=value
    returns a tuple: (name,value).  Can be found as match.groups
    Example: On the string: "Set-Cookie: LSID=DQAAAK;", returns
    ("LSID", "DQAAAK")

    On the string: ""Cookie: LSID=DQAAAK;", returns none
    (only mtaches Set-Cookie.
    '''
    #return None
    match = re.search('',test_string)
    if match:
        return match.groups()
    else:
        return None


#CHALLENGE PROBLEM
'''
Write a function that takes a csv file and converts it to a list of lists
first,last,email
ben,haynor,haynorb@gmail.com
ben,sholes,rowdy@meltwater.org
p,squard,chop@mymoney.com

should become
[['first','last','email'],
['ben','haynor','haynorb@gmail.com'],
['ben','sholes','rowdy@meltwater.org'],
['p','square','chop@mymoney.com']]
'''

#CHALLENGE PROBLEM
'''Try using search and replace with regular expressions to perform the
above challenge proplem in your favorite text editor.
'''
