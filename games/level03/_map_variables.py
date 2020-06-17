from random import randint

code = randint(1, 99)

conf = {
  "map": [
    "XXXXXXXXXXXXX",
    "X   X   X   X",
    "XP  F   L  VX",
    "X   X   X   X",
    "XXXXXXXXXXXXX"
  ],
  "allowKeyboard": False,
  "title": "Level 3. Variables",
  "welcomeMessage": [
    "Hello, adventurer! You've got a friend. Walk up to her.",
    "You can walk using functions right(), left(), up() and down()"
  ],
  "friends": [
    {
      "data": code,
      "message": [
        f"The code to the lock is {code}. Good luck. Bye!",
        f"(the ask() function returned {code})"
      ]
    }
  ],
  "locks": [
    {
      "code": code
    }
  ]
}