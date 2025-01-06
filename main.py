def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        text_length(file_contents)
        print("")
        character_frequency(file_contents)

def text_length(string):
    word_list = string.split()
    print("Word Count: " + str(len(word_list)))

def character_frequency(string):
    lower_string = string.lower()
    word_list = lower_string.split()
    character_dict = {}
    for word in word_list:
        for character in word:
            if character in character_dict:
                character_dict[character] = character_dict[character] + 1
            else:
                character_dict[character] = 1
    character_dict = dict(sorted(character_dict.items()))
    # print("Character List: " + str(character_dict))
    output = character_export(character_dict)
    for line in output:
        print(line)

def character_export(index):
    output_list = []
    for char in index:
        if char.isalpha() == True:
            output_list.append(f"The {char} character was found {index[char]} times.")
    #output_list = output_list.sort(reverse = True)
    return output_list

            

main()