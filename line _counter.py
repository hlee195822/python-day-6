line_counter = 0
empty_line_counter = 0
section_label-counter = 0

with open("lyrics. txt", "r") as file:
    for every_line in file:
        if every_line == "\n":
        
        empty_line_counter = empty_line_counter + 1 


        elif _every_line.startswith("["):
            section_lable_counter =empty_line-counter + 1

        elif every_line.startswith("["):
            section_lable_counter = section_label_counter + 1


        elif:
             line_counter = line_counter + 1

             print("The total lines in the song: ", line_counter)
             print("The total EMPTY line:", empty_line_counter)
             print("The total section labels: ", section_label_counter)
