# my first madlibs project
# first step
# assign variables to the madlibs game 

proper_noun = input("Proper Noun(Ex: Person's Name): ")
noun = input("Noun: ")
adj1 = input("Adjective(Feeling): ")
verb = input("Verb: ")
adj2 = input("Adjective(Feeling): ")
animal = input("Animal: ")
verb1 = input("Verb: ")
color = input("Color: ")
verb2 = input("Verb (ending in 'ing': ")
adverb = input("Adverb ending in 'ly': ")
number1 = input("Number: ")
time = input("Measure of Time: ")
color1 = input("Color: ")
animal1 = input("Animal: ")
number2 = input("Number: ")
silly_word = input("Silly Word: ")
noun1 = input("Noun: ")

# madlibs game:  this story was copied from : https://www.thepaintedturtle.org/sites/main/files/file-attachments/mad_libs.pdf

madlib =f"This weekend I am going camping with {proper_noun}. I packed my lantern, sleeping bag, and {noun}.\
    I am so {adj1}  to {verb} in a tent. I am {adj2} we might see a {animal}, they are kind of dangerous. We are going to hike, fish, and {verb1}.\
    I have heard that the {color} lake is great for {verb2}. Then we will {adverb} hike through the forest for {number1} {time}.\
    If I see a {color1} {animal1} while hiking, I am going to bring it home as a pet! At night we will tell {number2} {silly_word} stories and roast {noun1} around the campfire!!"

print(madlib)


