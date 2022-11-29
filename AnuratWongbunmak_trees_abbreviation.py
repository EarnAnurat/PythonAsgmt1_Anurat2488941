# AC50002 Programming languages for Data Engineering ( SEM 1 22/23 )
# Python Assignment
# Anurat Wongbunmak 2488941
# 2488941@dundee.ac.uk

# After get the file name from input() in main(), This readfile() will read all of the lines into a list.
# Storing the data into a linelist, each item representing a line of the file. 
# So, now we can loop through each line of the file and process it.
# https://eldoyle.github.io/PythonIntro/08-ReadingandWritingTextFiles/
def readfile(fname):
    """Reading a file from input line by line and store it into a list
    fname : filename(Strings)"""
    if(fname[-4:] != ".txt"):
        fname += ".txt";                # open the file
    infile = open(fname);               # infile is the opened file object that we will read from
    linelist = infile.readlines();      # read all of the lines into a list, where each line of the file is an item in the list
    infile.close();                     # close opened file
    return linelist;                    # Now, we get the data call "linelist" which is a list of all the lines

# Use words(name) to generate a list of words that are appropriate for abbreviations
def words(name):
    """Ignore the space and any special characters when spliting the names into a separate uppercase words. 
    Ex. "@Anurat-Wongbunmak Dundee" has three words "ANURAT", "WONGBUNMAK", and "DUNDEE" 
    name : the names we read from file(Strings)"""
    while name.find("-") != -1:                                       # while loop will execute the statement through name
        if name.find("-") != -1:
            name = name[:name.find("-")]+" "+name[name.find("-")+1:]; # If a name contain "-", replace it with a space " ".

    # .strip() Remove spaces at the beginning and at the end of the name
    # .upper() Change to upper case
    # .split() Separate words using a space into a list
    fmtname = name.strip().upper().split(); 

    # Delete special charector which is not 'A' - 'Z' by ASCII code 65-90
    n = 0                                                     # start with fisrt x
    for x in fmtname:                                         # x(n)
        m = 0;                                                # start with first charector
        for i in x:                                           # i(m)
            if ord(i) not in range(65,91):                    # The ord() function returns an integer representing the Unicode character.
                fmtname[n] = fmtname[n][:m]+fmtname[n][m+1:]; # skip the special charector
                m -= 1;                                       # if i is a special character, go back for 1 character to execute for loop again
            m += 1;                                           # after end loop of i, move to next i
        n += 1;                                               # after end loop of n, move to next n
    return fmtname; 

# Create a set of all the possible abbreviation 
def allabbr(wl):
    """Create a set of all the possible abbreviation 
    Ex. ["ANURAT", "WONGBUNMAK", "DUNDEE"] >>> {"ANU","ANR","AWD","ADD",...}
    wl : words list that we get from words(name)"""

    # Create a string by appending a words from words list, then getting len()
    lgth = 0; 
    str = ""; 

    for x in wl:
        str += x;                               # "ANURATWONGBUNMAKDUNDEE"

    lgth = len(str); 

    # Create a set of all the possible abbreviation
    setabbr = {str[:3]}                         # start with a set of first 3 letters Ex."ANU"
    for x in range(1):                          # first letter of the name
        for y in range(x+1,lgth-1):             # secode letter which is not first and last character in str
            for z in range(y+1,lgth):           # third letter which come from the rest of character that come after y
                setabbr.add(str[x]+str[y]+str[z]); 
    return setabbr; 

# calculate a score of abbreviation which indicates how good it is. The lower is the better.
def cal(wl,abbr):
    """Given a score to the abbreviation which which indicates how good it is, and return the lowest score
    wl : words list that we get from words(name)
    abbr : abbreviation 'xyz'"""

    # Create a string from words and a list of position of each letter
    lgth = 0; 
    str = "";  
    pos = [];                       # List of positions of characters in each word
    for x in wl:
        str += x;                   # "ANURATWONGBUNMAKDUNDEE"
        pos += list(range(len(x))); # [0,1,2,3,4,0,1,2,3,0,1,2,3,4,5]
    lgth = len(str);

    if lgth < 3:                    # no score for word that already contain 3 letters
        return 0;
    
    # create a list of the positions of potential first, second, and third abbreviations from all the string. 
    fst = [];                       # potential first abbreviations
    snd = [];                       # potential second abbreviations
    trd = [];                       # potential third abbreviations
    n = 0; 
    for i in str:
        if i == abbr[0]:
            fst.append(n); # append i from str to list of fst if == abbr[0] 
        if i == abbr[1]:
            snd.append(n); # append i from str to list of snd if == abbr[1]
        if i == abbr[2]:
            trd.append(n); # append i from str to list of trd if == abbr[2]
        n += 1
    
    # Create a set[tuple] of positions of potential abbreviation with only the right order
    settp = {(x,y,z) for x in fst for y in snd for z in trd if x<y and y<z}; # {(0, 2, 3), (0, 2, 6)}

    # value based on how common/uncommon this letter is in English
    values = {'A' : 25,'B' : 8,'C' : 8,'D' : 9,'E' : 35,'F' : 7,'G' : 9,'H' : 7,'I' : 25,'J' : 3,'K' : 6,'L' : 15,'M' : 8,'N' : 15,'O' : 20,'P' : 8,'Q' : 1,'R' : 15,'S' : 15,'T' : 15,'U' : 20,'V' : 7,'W' : 7,'X' : 3,'Y' : 7,'Z' : 1}

    # The lower is the better
    lowscore = 100; 
    for t in settp:                             
        score = 0; 
        n = 0; 
        for c in t:                           # c is position/char of abbr in string ex.(0,3,7)
            if pos[c] == 0:                   # pos is the list of positions of characters in each word
                score += 0;                   # ex.[0,1,2,3,0,1,2] z[4] = 0 
                n += 1;                       # the first letter is always the first letter ofthe name, so it does not get a score
                continue;                     # continue statement rejects all the remaining statements in the current iteration of the loop and moves the control back to the top of the loop.
            if c == len(pos)-1 and abbr[n] == 'E':
                score += 20;                  # last letter of word and the letter is "E", the score is 20
                n += 1; 
                continue; 
            if c == len(pos)-1:              
                score += 5;                   # if a letter is the last letter of a word in the name then it has score 5
                n += 1; 
                continue; 
            if pos[c] == 1:                    # second letter + a values
                score += 1 + values[abbr[n]]; 
                n += 1; 
                continue; 
            if pos[c] == 2:                    # third letter + a values
                score += 2 + values[abbr[n]]; 
                n += 1; 
                continue; 
            score += 3 + values[abbr[n]];     # any other position + a value
            n += 1; 
        lowscore = min(lowscore,score);       # Return the lowest score
    return lowscore; 

# This main() acts as a starting point for code that performs the primary purpose of the script.
def main():
    """main() will start execute other functions"""
    fname = input("Please enter a file name: "); 

    # First, get the data name linelist which is a list where each line in .txt file is an item
    # Also, check the file name is valid; if not, "Please enter a file name: " again
    while True:
        try:                              # The try block lets you test a block of code for errors
            linelist = readfile(fname);   # read the file with readinput(fname)
            if(len(linelist) >0):         # If there is a data, break
                break; 
        except:                           # If there is no data, call input() again
            pass; 
        fname = input('File is not found. Please enter a valid file name:'); 
    
    # Create a list of the best abbreviations to be a final result
    n = 0; 
    aabbr = [];                           # List of sets of all abbreviations
    unqabbr = [];                         # List of sets of unique abbreviations that do not repeat in other names
    for x in linelist:
        aabbr.append(allabbr(words(x))); 
    
    for x in aabbr:
        othabbr = set([]);                      # Set of all abbreviations from other names
        for y in range(len(aabbr)):             # 0,1
            if y != n:                          # Collect all abbreviations from other names ex. (y != n) ==> n=0{'ERN', 'EAN', 'EAR'} , y=1{'EIN', 'EIG', 'ENG'}
                othabbr = othabbr|aabbr[y];     # use OR | operation to create a set of othabbr: {'EIG', 'EAR', 'EIN', 'EAN', 'ENG', 'ERN'}
        unqabbr.append(x - othabbr);            # Create list of sets of unique abbreviations
        n += 1                                  # Now, unqabr is the remain of abbr of x that not repeat in other, unique  or occur just once
    
    # create a list of set of final abbreviation
    n = 0
    finabbr = []
    for x in unqabbr:           # [{'ERR'}, set(), {'ENG', 'EIG', 'EIN'}]
        if(len(x) == 0):        # If a name has no abbreviation left in the set of possible abbreviations(pabb),
            finabbr.append([]); # [] will be set to be its abbreviation.
            n += 1;
            continue; 
        
        ##### Find the minimum score
        minscore = 100;
        for y in x:                                             # y1{'ERR'}, y2set(), y345{'ENG', 'EIG', 'EIN'}
            minscore = min(minscore,cal(words(linelist[n]),y)); # use words(linelist[n]) in here to prepare data for cal
            
        ##### Create a list of lists of final abbreviations
        finabbr.append([y for y in x if cal(words(linelist[n]),y) == minscore])
        n += 1;

    ##### Write the output file #####
    if(fname[-4:] == '.txt'):
        fname = fname[:len(fname)-4];
    outfile = open("AnuratWongbunmak_"+fname+'_abbrevs.txt','w');
    for n in range(len(finabbr)):
        print(linelist[n].strip(),' : ',finabbr[n]);   ###Print output on the screen

        if(n == len(finabbr)-1):
            outfile.write(str(linelist[n].strip()));        ###Write original names
            outfile.write('\n');                            ###Last name put the end of line

        else:
            outfile.write(str(linelist[n]));            ###Write original names
            
        if(len(finabbr[n]) == 0):
            outfile.write('\n');                    ###If no possible abbreviation, skip the line
        else:
            for i in finabbr[n]:
                outfile.write(i+' ');
            outfile.write('\n');
    outfile.close()

# Running a module 
if __name__ == "__main__": # The first line is to ensure that when the module is simply imported, the function is not called
    main();                # Then the module can be run from an ordinary Windows command prompt