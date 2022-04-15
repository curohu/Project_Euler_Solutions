# 04/15/2022

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600,851,475,143 ?

# I guess that I was factoring every number and not a specific one... I am dumb

# def largest_prime_factor(number)
#   i = 2
#   while number > 1
#     if number % i == 0
#       number /= i;
#     else
#       i += 1
#     end
#   end
#   return i
# end

# largest_prime_factor(600851475143)
# # => 6857

target = 600851475143
i = 3
while target > 1:
    if target % i == 0:
        print(i)
        target = target/i
        print('-',target)
    else:
        i += 2
print(i)
