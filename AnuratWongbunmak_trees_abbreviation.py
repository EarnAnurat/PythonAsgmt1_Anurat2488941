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
    linelist = infile.readlines(fname); # read all of the lines into a list, where each line of the file is an item in the list
    infile.close(fname);                # close opened file
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
    pos = [];                       
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