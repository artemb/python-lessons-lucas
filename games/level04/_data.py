from random import randint

code1 = randint(1, 99)
code2 = randint(1, 99)
code3 = randint(1, 99)

conf = {
    "map": [
        "XXXXXXXXXXXXXXXXXXXXX",
        "X   X   X   X   X   X",
        "XP  F   F   F   L  VX",
        "X   X   X   X   X   X",
        "XXXXXXXXXXXXXXXXXXXXX"
    ],
    "allowKeyboard": False,
    "title": "Level 4. Sums",
    "welcomeMessage": [
        "Hello, adventurer! You've got a friend. Walk up to her.",
        "You can walk using functions right(), left(), up() and down()"
    ],
    "friends": [{
        "data": code1,
        "message": [
            f"The code to the lock is the sum of 3 numbers",
            f"I only know the first number. It's {code1}",
            f"Good luck! Bye! (the ask() function returns {code1})"
        ]
    }, {
        "data": code2,
        "message": [
            f"The second number is {code2}.",
            f"(ask() function returns {code2})"
        ]
    }, {
        "data": code3,
        "message": [
            f"The third number is {code3}",
            f"(ask() function returns {code3})"
        ]
    }
    ],
    "locks": [
        {
            "code": code1 + code2 + code3
        }
    ]
}
