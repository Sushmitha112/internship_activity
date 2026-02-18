# import random

# trials = 1000
# count_sum_7 = 0

# for _ in range(trials):
#     dice1 = random.randint(1, 6)
#     dice2 = random.randint(1, 6)
    
#     if dice1 + dice2 == 7:
#         count_sum_7 += 1

# experimental_probability = count_sum_7 / trials

# print("Experimental Probability of Sum = 7:", experimental_probability)

# Independent Events

# Probability of Heads
# P_heads = 1/2

# Probability of rolling a 6
# P_six = 1/6

# Independent formula
# P_heads_and_six = P_heads * P_six

# print("Probability of Heads AND 6:", P_heads_and_six)

# Dependent Events

# First marble red
# P_first_red = 5/10

# After removing one red
# P_second_red = 4/9

# Dependent formula
# P_both_red = P_first_red * P_second_red

# print("Probability of both marbles being Red:", P_both_red)




# Given probabilities

P_spam = 0.1            # P(Spam)
P_ham = 0.9             # P(Ham)

P_free_given_spam = 0.9   # P(Free | Spam)
P_free_given_ham = 0.05   # P(Free | Ham)

# Step 1: Total probability of seeing "Free"
P_free = (P_free_given_spam * P_spam) + \
         (P_free_given_ham * P_ham)

# Step 2: Apply Bayes' Theorem
P_spam_given_free = (P_free_given_spam * P_spam) / P_free

print("P(Free) =", P_free)
print("P(Spam | Free) =", P_spam_given_free)



