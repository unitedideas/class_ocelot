import random

print('Welcome\n')

out_list = ['It is certain',
'It is decidedly so',
'Without a doubt',
'Yes definitely',
'You may rely on it',
'As I see it yes',
'Most likely',
'Outlook good',
'Yes',
'Signs point to yes',
'Reply hazy try again',
'Ask again later',
'Better not tell you now',
'Cannot predict now',
'Concentrate and ask again',
'Don\'t count on it',
'My reply is no',
'My sources say no',
'Outlook not so good',
'Very doubtful']

while True:

    input('...Ask any yes or no question...\n')

    print(random.choice(out_list))

    while True:
        play = input('Would you like to play again? yes or no\n')
        if play == 'yes' or play == 'no':
            break
    if play == 'no':
        break
