import pytextnow
import calculations
import keys
import time


client = pytextnow.Client(
    keys.user,
    sid_cookie=keys.sid,
    csrf_cookie=keys.csrf
)


def getgreeting():
    #determines the greeting of the message
    currentTime = int(time.strftime('%H'))   

    if currentTime < 12 :
        return('Good morning')
    if currentTime > 12 :
        return('Good afternoon')
    if currentTime > 6 :
        return('Good evening')



def sendmsg():
    users = keys.peoples()

    times = calculations.calc()

    for i in range(len(users)):
        user = users[i][0]
        number = users[i][1]

        fullmess = getgreeting() + ' ' + user + ',' + r"\n"

        fullmess = fullmess + r"\n" + f'You have {times[0]}  left to eat this morning.' + r"\n"

        fullmess = fullmess + r"\n" + f'Breakfast ends at {times[3]}!' + r"\n"

        fullmess = fullmess + r"\n" + f'You have {times[1]} left until dinner.' + r"\n"

        fullmess = fullmess + r"\n" + f'You can eat at dinner at {times[2]}!'


        client.send_sms(user ,fullmess)
        
            



sendmsg()