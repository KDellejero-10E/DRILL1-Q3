
from pyscript import display, document

def check_gwa(e):
    
    document.getElementById('output').innerHTML = ''

    gwa_input = document.getElementById('gwa').value  

    if not gwa_input:
        display("Please enter your GWA.", target="output")
        return

    try:
        gwa = float(gwa_input)
    except ValueError:
        display("Invalid input. Enter a number.", target="output")
        return


    if gwa > 74:
        result = "PASSED"
    else:
        result = "FAILED"

    display(f"Your result is: {result}", target="output")
