from pyscript import display, document

members = ["Gavin Taguiga", "Natan Ladyon", "Carwo Barrel", "Ariana Grenade", "Jarvis More Alcohol"]

def check_member(e):
    FirstName = document.getElementById("nameInput1").value
    LastName = document.getElementById("nameInput2").value
    FullName = FirstName + " " + LastName

    messages = {
        True: f"Congratulations {FullName}! You are now part of the ICT club.",
        False: f"Sorry {FullName}, your name is not on the list."
    }

    message = messages[FullName in members]

    result = document.getElementById("result")

    result.innerHTML = message
    display(message, target="output1")