from random import choice

words = ['flag', 'brass', 'hook', 'tooth', 'stew', 'coat', 'swim', 'parent']

code1 = choice(words)
code2 = choice(words)
code3 = choice(words)

conf = {
    "map": [
        "XXXXXXXXXXXXXXXXXXXXX",
        "X   X   X   X   X   X",
        "XP  F   F   F   L  VX",
        "X   X   X   X   X   X",
        "XXXXXXXXXXXXXXXXXXXXX"
    ],
    "allowKeyboard": False,
    "title": "Level 5. Text",
    "welcomeMessage": [
        "Hello, adventurer! You've got a friend. Walk up to her.",
        "You can walk using functions right(), left(), up() and down()"
    ],
    "friends": [{
        "data": code1,
        "message": [
            f"The code to the lock consists of 3 words.",
            f"I only know the first word. It's {code1}",
            f"Good luck! Bye! (the ask() function returns '{code1}')"
        ]
    }, {
        "data": code2,
        "message": [
            f"The second word is {code2}",
            f"(the ask() function returns '{code2}')"
        ]
    }, {
        "data": code3,
        "message": [
            f"The third word is {code3}",
            f"(the ask() function returns '{code3}')"
        ]
    }
    ],
    "locks": [
        {
            "code": code1 + " " + code2 + " " + code3
        }
    ]
}
