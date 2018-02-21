import re

def hey(phrase):
    is_question = False
    is_yelling = False
    is_addressing_without_saying = False
    answer = ''
    phrase = re.sub(r'[\n\r\t]','',phrase.strip())

    if phrase.isupper():
        is_yelling = True
    if len(phrase) is 0:
        is_addressing_without_saying = True
    elif phrase[len(phrase)-1] is '?':
        is_question = True

    if is_question and is_yelling:
        answer = 'Calm down, I know what I\'m doing!'
    elif is_question:
        answer = 'Sure.'
    elif is_yelling:
        answer = 'Whoa, chill out!'
    elif is_addressing_without_saying:
        answer = 'Fine. Be that way!'
    else:
        answer = 'Whatever.'
    return answer
