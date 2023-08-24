programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
  "Loop": "The action of doing something over and over again.",
}

# Accessing a dictionary
print(programming_dictionary["Function"])

# Adding new items to dictionary.
programming_dictionary["Touch Grass"] = "The futile act of trying to retreive some sanity."

print(programming_dictionary)

# Iterating through dictionary goes through the keys:
for key in programming_dictionary:
  print(key)
  
# Nesting:
