print("harshit")
print("Hello" )
name = "harshit"
print(name)
"harshit"
name = 15
print(name)
#15
print("5 + 2 =", 5+2)
print("5 - 2 =", 5-2)
print("5 * 2 =", 5*2)
print("5 / 2 =", 5/2)
"This costs " + str(6) +  " Dollars"
'This costs 6 Dollars'
"this costs " + str(4+5) +  " dollars"
'this costs 9 dollars'

"Now using split function to create an array"
"Harshit:Hello".split(":")
#['Harshit', 'Hello']
"we can split it many times"
"now performing complex problems"
print("My name is "+ "harshit:whats up:hey".split(":") [0])
'My name is harshit'
X= "blue red green"
X.split(" , ")
#['blue red green']
"\n   - for new line"
"to cancel the special meaning in string just use r before your input command"
'eg- print(r" c : \docs \ navin")'
"now using lists operators"
print ("I like playing " + ["football", "cricket", "vollyball"] [1])
"I like playing cricket"
"dictonaries concept"
print( {"name":"harshit" , "age":"21" , "hobby": "cricket"} ["hobby"])
"cricket"
"variables concept"
greeting = "hello world"
print(greeting)
"hello world"
greeting = greeting.split(" ")[0]
print(greeting)
"hello"


def my_function():
    print("My hobby is to play cricket")
    print("i love haldwani")


my_function()


def my_function(name="harshit", age=21):
    print("my name is ", name, "and my age is", age)


my_function()
"my name is harshit and my age is 21"

def do_math(num1,num2):
    return num1 + num2

math1 = do_math(40,30)
math2 = do_math(40,89)
print("first sum is",math1,"and the second sum is",math2 )
"first sum is 70 and the second sum is 129"

"else if statement"

check = "haldwani"
if check == "haldwani":
    print("it is true")
elif check == "delhi":
    print("it is false")
else:
    print("it is actually nothing")
"it is true"

'''run= True
current=1

while run:
    if current==100:
        run=False
    else:
        print(current)
        current+=1
        1
        2
        3
        4
        5
        6
        7
        8
        9
        10
        11
        12
        13
        14
        15
        16
        17
        18
        19
        20
        21
        22
        23
        24
        25
        26
        27
        28
        29
        30
        31
        32
        33
        34
        35
        36
        37
        38
        39
        40
        41
        42
        43
        44
        45
        46
        47
        48
        49
        50
        51
        52
        53
        54
        55
        56
        57
        58
        59
        60
        61
        62
        63
        64
        65
        66
        67
        68
        69
        70
        71
        72
        73
        74
        75
        76
        77
        78
        79
        80
        81
        82
        83
        84
        85
        86
        87
        88
        89
        90
        91
        92
        93
        94
        95
        96
        97
        98
        99'''
import re
string ="I AM NOT YELLING',she said.Though we knew it to not be true."
print(string)
"I AM NOT YELLING',she said.Though we knew it to not be true."
new = re.sub('[A-z]', '' , string)
print(new)
"   ', .       . "
new = re.sub('[.,\']' , '' , string)
print(new)
"I AM NOT YELLINGshe saidThough we knew it to not be true"
new = re.sub('[.,\'a-z]' , '' , string)
print(new)
"I AM NOT YELLING T"
new = re.sub('[.,\'A-Z+" "]' , '' , string)
print(new)
#shesaidhoughweknewittonotbetrue
string = string + "6 298 - 345"
print(string)
"I AM NOT YELLING',she said.Though we knew it to not be true.6 298 - 345"
new = re.sub('[^0-9]' , '' , string)
print(new)
6298345

