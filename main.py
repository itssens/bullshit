import modules.sense
import time
import os

def clearcmd():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def rechner():
  sense = modules.sense.gamesense(6)
  val = sense.getVal()

  print(val)
  
def main():
  print("Module:")
  print("[1] Automatischer Rechner")
  print("Weiteres kommt bald...")
  eingabe = input("Welches Modul willst du starten?")
  if eingabe == "1":
    rechner()
  elif eingabe == "2":
    print("bald....")
    time.sleep(2.00)
    clearcmd()
    main()
  else:
    ungültig = input("Ungültige Eingabe! Drücke enter um es erneut zu probieren....")
    clearcmd()
    main()
main()
