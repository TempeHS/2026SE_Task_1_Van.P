def logged():
    geek = int(input("1.Change password " "2.Log out "))
    if geek == 1:
        input("what you finna change it to? ")
    if geek == 2:
        print("Logged out")
        menu = int(input("1.Login " "2.Register " "3.Quit "))


menu = int(input("1.Login " "2.Register " "3.Quit "))

if menu == 1:
    LogUs = input("Username? ")
    if LogUs == ("sithLord" or "d_Vader" or "GENERALleia" or "grogu" or "there_is_no_try" or "MyRey" or "Luke"):
        LogPa = input("Password? ")
        if LogPa == ("Ancient enimes r us" "I'm Your Father" "May the Force be with you" "patu" "Yoda" "I Am All The Jedi" "May the Force be with you"):
            print("Logged in!")
            logged()
    else:
        menu = int(input("1.Login " "2.Register " "3.Quit "))

elif menu == 2:
    RegUs = input("Username? ")
    if RegUs == ("sithLord" or "d_Vader" or "GENERALleia" or "grogu" or "there_is_no_try" or "MyRey" or "Luke"):
        print("Taken")
    elif input("Password? "):
        print("Okay!")
        logged()




elif menu == 3:
    print("Terminated")

    