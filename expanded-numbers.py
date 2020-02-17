'''
You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'

NOTE: All numbers will be whole numbers greater than 0.
'''

def expanded_form(num):
    numList = [int(number) for number in str(num)] #this can be list(str(num))
    expanded = [str(x * 10**(len(numList) - y - 1)) for x, y in zip(numList, range(len(numList))) if x != 0] #there is enumerate(num) as an option
    return ' + '.join(expanded)

    #copied cleaner solution
    #def expanded_form(num):
    #    num = list(str(num))
    #    return ' + '.join(x + '0' * (len(num) - y - 1) for y,x in enumerate(num) if x != '0')