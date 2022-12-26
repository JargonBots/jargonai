from conversation import conversation

# Chat useage examwannple:


Name = "Sherlock Holmes"

# cv = conversation("Rico Chen is from Millburn, he goes to Millburn HS is a junior. likes to lift weights, good student, interested in trading stocks and football. Close friends are Aryan and Armaan Kapoor, Chase, Carizzo, kishmeya. Currently rico made a bad decision and took alot of LSD, hes feeling trippy, but hes is alright. His friends want to get deep w him\nThe following is a conversation with {}.\n", "{}: ".format(Name))
cv = conversation(
    starting_environment="The following is a chat with {}.".format(Name), bot_name="{}: ".format(Name)
)

print("The following is a chat with {}".format(Name))
cv.tick(50)

# cv.user_append()
