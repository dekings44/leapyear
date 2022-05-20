print('Welcome to  my love calculator')

name1 = input('What is your name?\n')
name2 = input('What is your spouse name name?\n')

both_names = name1 + name2

both_names_lowercase = both_names.lower()

t = both_names_lowercase.count('t')
r = both_names_lowercase.count('r')
u = both_names_lowercase.count('u')
e = both_names_lowercase.count('e')

total_true = t + r + u + e

l = both_names_lowercase.count('l')
o = both_names_lowercase.count('o')
v = both_names_lowercase.count('v')
e = both_names_lowercase.count('e')

total_love = l + o + v + e

love_score = int(str(total_true) + str(total_love))

if (love_score < 10) or (love_score > 90):
    print(f'Your score is {love_score}. You go together like bread and ewa goin')
elif love_score >= 40 and love_score <= 50:
    print(f'Your score is {love_score}. You are alright together')
else:
    print(f'Your score is {love_score}. Enjoy your partner')
