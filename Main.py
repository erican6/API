import tkinter as tk
import requests
import webbrowser
from os import path
import sys

#Authorisation
headers = {
   'Accept': 'application/json',
   'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjlkMGIxY2FkLWZiN2EtNGRiOS05ZTM2LWYzYzNlMjk4Yzk0MiIsImlhdCI6MTU2ODY5NTU5NCwic3ViIjoiZGV2ZWxvcGVyLzViOGM3ZDI3LTQwOTAtZmQ1Zi01ZWEwLTgwMDExZmU0NWNmMSIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjk5LjIyOC4yNTAuMjUyIl0sInR5cGUiOiJjbGllbnQifV19.P-nHOENT2iJAnqFJTapl7HLoTytNbAQMSs-MydKAuCOw6Tup8wOFvfpDW4zaez1iVXfZgJK1hik_sz4spUXv1g'
}

# headers = {
#     'Accept': 'application/json',
#     'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjhjZjE1N2E1LTZmNDgtNGYwZC1hY2EwLTk1OGNjM2M1YmM0MSIsImlhdCI6MTU2ODgzNDkzMiwic3ViIjoiZGV2ZWxvcGVyLzViOGM3ZDI3LTQwOTAtZmQ1Zi01ZWEwLTgwMDExZmU0NWNmMSIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjY5Ljc3LjE2MC4yIl0sInR5cGUiOiJjbGllbnQifV19.ORxMfBIGfJEhgbSm0LGNFR7PwZMVR5qgSyuyil1HH4uVg_eREyg6vMAnm-5B-RwppBltFn-rLh9iAE_fB8jPUg'
# }

#headers = {
#    'Accept': 'application/json',
#    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImFmNjAwZDI3LWEwNWItNDQzZS05YjU0LTY3NTM1NzMwYzI2ZSIsImlhdCI6MTU3MDk4NzgzOSwic3ViIjoiZGV2ZWxvcGVyLzViOGM3ZDI3LTQwOTAtZmQ1Zi01ZWEwLTgwMDExZmU0NWNmMSIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjEyOS4xMDAuMjA1LjIxMyJdLCJ0eXBlIjoiY2xpZW50In1dfQ.c8N0siduzy4M5MJloq-YP89UO6WUsbXD_mSES-NO3JuUB72krnooIVP4isGrE7LfP3SblONnAxQ80iqhDWZi4w'
#}


def compare():
    #Import helper module written already
    import get_user as get

    def change():
        #Setting Parameters
        ynum = 210
        num1=0

        def retrieve():

            def success():

                def openbrowser():
                    #Close file (helper module), open file into web, exit code
                    get.close_file()
                    webbrowser.open('file://'+ path.realpath('comparisonCOC.html'))
                    sys.exit()

                #SUCCESS, Open browser button to open the file into web (goes into def openbrowser)
                tk.Label(window, text="Success",font=('times new roman', 16, 'bold'),fg='orangered').place(x=225,y=ynum+30)
                tk.Button(window,text="Open in Browser",command=openbrowser).place(x=195,y=ynum+60)

            #For every answer found in the list, set player_tag, get response from API, run the response through the helper module
            for answer in player_answer_list:
                player_tag = answer.get()
                response = requests.get("https://api.clashofclans.com/v1/players/%23"+player_tag, headers=headers)

                #Error checking.. if the response code is different, results in default input
                if response.status_code != 200:
                    response = requests.get("https://api.clashofclans.com/v1/players/%23YVOYV82J", headers=headers)

                get.get_user(response)

            #Calling on def success
            success()

        #Now asking for inputs of Payer Tags
        tk.Label(window,text="Running for {} users...".format(var.get()),font=('times new roman', 13, 'italic'),fg='black').place(x=170, y=150)
        tk.Label(window,text="Input Player Tags!",font=('times new roman', 16, 'bold'),fg='orangered').place(x=160,y=185)

        #Using the previously set variable to get how many accounts are being compared and thus how many entry boxes must be made
        num=int(var.get())

        #List creation to store the data from the for loop
        player_answer_list = []

        #Entry, variable assignment. First for loop adds each entry answer into list. Second for loop is adding the entry boxes
        player_answer = tk.Entry(window, width=20)
        for i in range (0, num, 1):
            player_answer_list.append(player_answer)

        for i in range(0, num, 1):
            tk.Label(window,text="Player Tag (No #)",font=('times new roman', 15, 'underline'),fg='black').place(x=60, y=ynum)
            player_answer_list[i] = tk.Entry(window,width=20)
            player_answer_list[i].place(x=180,y=ynum)
            ynum=ynum+30
            num1=num1+1

        #Once all inputed, click button to retrieve (goes into def retrieve)
        tk.Button(window, text="Retrieve", command=retrieve).place(x=225, y=ynum)
    #Creating list to set options for upcoming menu
    limitNum = ['2', '3', '4', '5', '6']

    #Setting variable
    var = tk.StringVar(window)
    var.set(limitNum[0])

    #Creating the start of the file (helper module)
    get.start_file()

    #Introduction, makes users choose how many accounts they would like to compare (goes into def change)
    tk.Label(window,text="Welcome To Player Comparisons",font=('times new roman', 16, 'bold'),fg='orangered').place(x=120,y=60)
    tk.Label(window,text="Input Player Tags And Receive Basic Info To Compare With!",font=('times new roman', 16, 'bold'),fg='orangered').place(x=35,y=90)
    tk.Label(window, text="Number of accounts (Max 6): ").place(x=90,y=120)
    tk.OptionMenu(window,var,*limitNum).place(x=290,y=120)
    tk.Button(window,text="Submit",command=change).place(x=335,y=123)
def depth():
    #import helper module already written
    import get_details as details

    def run():

        def success():

            def openbrowser():
                # Close file (helper module), open file into web, exit code
                details.close_file()
                webbrowser.open('file://' + path.realpath('detailsCOC.html'))
                sys.exit()

            #SUCCESS, Open browser button to open the file into web (goes into def openbrowser)
            tk.Label(window, text="Success", font=('times new roman', 16, 'bold'), fg='orangered').place(x=225,y=180)
            tk.Button(window, text="Open in Browser", command=openbrowser).place(x=195, y=210)

        #Set player tag to the answer received from the entry box, get response from API, run the response through the helper module

        player_tag = answer.get()
        response = requests.get("https://api.clashofclans.com/v1/players/%23" + player_tag, headers=headers)

        if response.status_code != 200:
            response = requests.get("https://api.clashofclans.com/v1/players/%23YVOYV82J", headers=headers)

        details.get_details(response)

        # Calling on def success
        success()

    #Creating the start of the file (helper module)
    details.start_file()

    #Introduction, makes users input player tag, button to run the command (goes into def run)
    tk.Label(window,text="Welcome To Player Analysis",font=('times new roman', 16, 'bold'),fg='orangered').place(x=135,y=60)
    tk.Label(window,text="Input Player Tag And Receive Basic In Depth Info!",font=('times new roman', 16, 'bold'),fg='orangered').place(x=50,y=90)
    tk.Label(window, text="Player Tag (No #)").place(x=90,y=120)
    answer = tk.Entry(window,width=20)
    answer.place(x=220,y=120)
    tk.Button(window,text="Retrieve",command=run).place(x=220,y=150)
#Create Window
window = tk.Tk()
window.title('Clash of Clans API')
window.geometry('500x750')
window.resizable(0,0)

#Place button to receive input from user on what type of data they would like to receive (Goesi nto def compare or def depth)
tk.Label(window, text='Please Select Which Data You Would Like To Retrieve', font=('times new roman', 16, 'bold'), fg='orangered').pack()
tk.Button(window, text='Compare Users', command=compare).place(x=110,y=30)
tk.Button(window, text='In Depth Analysis', command=depth).place(x=250,y=30)


window.mainloop()
