


def minion_game(string):
    # your code goes here
    # To find the number of sub strings that can be formed with A char and the followed       chars, we can subtract the Length with Index. Hence to find the substrings with the      constants and vowels we can subtract the length with its index
    string = string.upper()
    vowels = ['A','E','I','O','U']
    vow,con = 0,0
    len_str = len(string)
    for i in range(len_str):
        if string[i] in vowels:
            vow += len_str - i 
        else:
            con += len_str - i
    
    if vow > con:
        print(f"Kevin {vow}")
    elif con > vow:
        print(f"Stuart {con}")
    else:
        print("Draw")


#it will iterate through all the characters of the string.. if the string is banana, you can create 6 words starting from the first 'B', you can create 5 words starting from the first 'A' and similarly for every character you can create (string_len-i) words. so if the word starts with vowel, add it to Kevin, else add it to Stuart. Finally compare their results and print the winner.