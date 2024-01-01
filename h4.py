import requests
import json
#import numpy as np
#import time
from datetime import datetime
import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from polygon import WebSocketClient, STOCKS_CLUSTER
import numpy as np
import pandas as pd




      
      
#AMKR","ADI","AMAT","AAOI","ATOM","AXTI","AVGO","CCMP","CSIQ","CEVA","IMOS","CRUS","CREE","CY","DIOD","DSPG","EMKR","ENPH","MRAM","FNSR","FSLR","FORM","GSIT"]
#listT=["INTC","ON","ADI","NVDA","STM","TXN","NXPI","MCHP","XLNX","MU","TSM","LSCC","AMD"]
listT=["INTC","ON","ADI","NVDA","STM","TXN","NXPI","MCHP","XLNX","MU","TSM","LSCC","AMD","AVGO","SWKS","QRVO","MCHP","MRVL","MXIM","QRVO","ADI","HPE","DELL","EMR"]
#listT=["GE", "PYPL"," SHOP", "SPY", "SQ", "STM", "TSM"]
counbid=[]
counbid1=[]
sstemp=""
Fr=.5
Fg=.7
CRED=0
CRED10=0
price=0.001
priceBuy=0.001
pricesale=0.001





totalRedSym=Fr*len(listT)
totalGreenSym=Fg*len(listT)
print(totalGreenSym)
print(totalRedSym)
lidf=[]


for i in listT:
    lidf.append( pd.DataFrame({
    'Price': [1.1, 2.1, 3.1, 4.1, 5.1, 6.1, 7.1, 8.1, 9.1, 10.1],
    'speed': [1.1, 2.1, 3.1, 4.1, 5.1, 6.1, 7.1, 8.1, 9.1, 10.1],
    'Acc': [1.1, 2.1, 3.1, 4.1, 5.1, 6.1, 7.1, 8.1, 9.1, 10.1],
    'time': [1.1, 2.1, 3.1, 4.1, 5.1, 6.1, 7.1, 8.1, 9.1, 10.1],
    'sym': ["1", "2", "3", "4", "5", "6"," 7"," 8"," 9", "10"],
    'Group': ["1", "2", "3", "4", "5", "6"," 7"," 8"," 9", "10"],
      }))

temp=0

for listtemp in listT:
    sstemp+= "T."+str(listtemp)+" , " 
    counbid.append(0)
    counbid1.append(0)
    for yy in range(9):
        lidf[temp]['sym'][yy]=listtemp
    temp+=1





root = Tk()
root.geometry("1280x2000")  
fontStyle = tkFont.Font(family="Lucida Grande", size=18)
fontStyle1 = tkFont.Font(family="Lucida Grande", size=12)
 



z0 = Label(root, text="SYMB", fg="white",bg="BLACK" , font=fontStyle )
z1 = Label(root, text="PRICE", fg="white",bg="BLACK" , font=fontStyle )
z2 = Label(root, text="Speed ", fg="white",bg="BLACK" , font=fontStyle )
z3 = Label(root, text="Sp10", fg="white",bg="BLACK" , font=fontStyle )
z4 = Label(root, text="SpAv", fg="white",bg="BLACK" , font=fontStyle )
z5 = Label(root, text="Acc", fg="white",bg="BLACK" , font=fontStyle )
z6 = Label(root, text="AccAV", fg="white",bg="BLACK" , font=fontStyle )
z7 = Label(root, text="TIME", fg="white",bg="BLACK" , font=fontStyle )
z8 = Label(root, text="Wlist", fg="white",bg="BLUE" , font=fontStyle )
z9 = Label(root, text="00.00", fg="white",bg="BLUE" , font=fontStyle )


z0.grid (column=0 ,row=0)
z1.grid (column=1 ,row=0)
z2.grid (column=2 ,row=0)
z3.grid (column=3 ,row=0)
z4.grid (column=4 ,row=0)
z5.grid (column=5 ,row=0)
z6.grid (column=6 ,row=0)
z7.grid (column=7 ,row=0)
z8.grid (column=8 ,row=0)
z9.grid (column=9 ,row=0)



z0.config(height=1, width=5) 
z1.config(height=1, width=10) 
z2.config(height=1, width=6) 
z3.config(height=1, width=6) 
z4.config(height=1, width=10) 
z5.config(height=1, width=5) 
z6.config(height=1, width=5) 
z7.config(height=1, width=9)
z8.config(height=1, width=9)
z9.config(height=1, width=9)
pSym= tk.StringVar()
pSale= tk.StringVar()
pqunt= tk.StringVar()

def buybut():
    global price,priceBuy

    priceBuy=float(price)
    lbuy.configure(text="Buy:"+str(price))
    lsale.configure(text="G:")

def SellNow():
    ssale=str(round((price-priceBuy)*int(pqunt.get())-20,4))
    #print(ssale)
    lsale.configure(text="G:"+ssale)




ButtBuy= Button(root, text="Buy Button", fg="white",bg="BLUE"  ,font=fontStyle1, command = buybut)
ButtSell= Button(root, text="Sell Button", fg="white",bg="MAGENTA"  ,font=fontStyle1, command = SellNow)
ALL_SP10 = Label(root, text="All Sp10:", fg="white",bg="BLUE",font=fontStyle1 )
All_SPAv = Label(root, text="All SpAv:", fg="white",bg="BLUE",font=fontStyle1 )
colorSP10 = Label(root, text="Sp10", fg="white",bg="BLUE",font=fontStyle1 )
colorSPAv = Label(root, text="SpAv:", fg="white",bg="BLUE",font=fontStyle1 )



txt1= Entry(root, width = 15 , fg="white",bg="BROWN"  ,font=fontStyle1,textvariable = pSym )
txt2= Entry(root, width = 15 , fg="white",bg="BROWN" ,font=fontStyle1, textvariable = pqunt )
lbuy = Label(root, text="buy:", fg="white",bg="BLUE" ,font=fontStyle1 )
lsale = Label(root, text="Gain:", fg="white",bg="GREEN",font=fontStyle1  )
lsale1 = Label(root, text="GainOnLine:", fg="white",bg="BLUE" ,font=fontStyle1 )
pSym.set("AMD")
pqunt.set(500)

ButtBuy.grid (column=9 ,row=1)
ButtSell.grid (column=9 ,row=2)
ALL_SP10.grid (column=9 ,row=3)
All_SPAv.grid (column=9 ,row=4)
colorSP10.grid (column=9 ,row=5)
colorSPAv.grid (column=9 ,row=6)
lbuy.grid (column=9 ,row=7)
lsale.grid (column=9 ,row=8)
lsale1.grid (column=9 ,row=9)
txt1.grid (column=9 ,row=12)
txt2.grid (column=9 ,row=13)
ButtBuy.config(height=1, width=15) 
ButtSell.config(height=1, width=15)
ALL_SP10.config(height=1, width=10) 
All_SPAv.config(height=1, width=10)
colorSP10.config(height=1, width=10) 
colorSPAv.config(height=1, width=10)



lsale.config(height=1, width=10) 
lsale1.config(height=1, width=10) 
lbuy.config(height=1, width=10) 


labSym=[]
labPrice=[]
labtime=[]
labvalue = []
labspeed = []
labspeedAv = []
labacc = []
labaccAv=[]
labBUY=[]
REDBOOL=[]
REDBOOL10=[]
sp10=[]
spAv=[]

for counter in range(13):
      labBUY.append(Label(root, text ="" , fg="white",bg="BLUE" ,relief=SUNKEN ,anchor=W, justify=LEFT, font=fontStyle ))
      labBUY[counter].grid (column=8 ,row=counter+1)
      labBUY[counter].config(height=1, width=10) 


labTotal=[labSym,labPrice,labvalue,labspeed,labspeedAv,labacc,labaccAv,labtime]


for counter in range(len(listT)):
      
     
      labSym.append(Label(root, text ="" , fg="white",bg="RED" , font=fontStyle ))
      labSym[counter].grid (column=0 ,row=counter+1)
      labSym[counter].config(height=1, width=5) 
      
      labPrice.append(Label(root, text ="" , fg="white",bg="GREEN" ,relief=SUNKEN ,anchor=W, justify=LEFT,font=fontStyle ))
      labPrice[counter].grid (column=1 ,row=counter+1)
      labPrice[counter].config(height=1, width=10) 
      
      labvalue.append(Label(root, text ="" , fg="white",bg="GREY",relief=SUNKEN ,anchor=W, justify=LEFT, font=fontStyle ))
      labvalue[counter].grid (column=3 ,row=counter+1)
      labvalue[counter].config(height=1, width=6) 

      labspeed.append(Label(root, text ="" , fg="white",bg="GREEN",relief=SUNKEN ,anchor=W, justify=LEFT, font=fontStyle ))
      labspeed[counter].grid (column=2 ,row=counter+1)
      labspeed[counter].config(height=1, width=6) 

      labacc.append(Label(root, text ="" , fg="white",bg="GREY" ,relief=SUNKEN ,anchor=W, justify=LEFT, font=fontStyle ))
      labacc[counter].grid (column=5 ,row=counter+1)
      labacc[counter].config(height=1, width=5) 

      labspeedAv.append(Label(root, text ="" , fg="white",bg="GREEN" ,relief=SUNKEN ,anchor=W, justify=LEFT, font=fontStyle ))
      labspeedAv[counter].grid (column=4 ,row=counter+1)
      labspeedAv[counter].config(height=1, width=10) 

      labaccAv.append(Label(root, text ="" , fg="white",bg="GREY" ,relief=SUNKEN ,anchor=W, justify=LEFT, font=fontStyle ))
      labaccAv[counter].grid (column=6,row=counter+1)
      labaccAv[counter].config(height=1, width=5) 

      labtime.append(Label(root, text ="" , fg="white",bg="GREEN" ,relief=SUNKEN ,anchor=W, justify=LEFT, font=fontStyle ))
      labtime[counter].grid (column=7 ,row=counter+1)
      labtime[counter].config(height=1, width=9) 

      


      REDBOOL.append(False)
      REDBOOL10.append(False)
      sp10.append(.1)
      spAv.append(.1)     
labBUY[4].configure(text="sp 10 sec")
labBUY[1].configure(text="speed Av")
labBUY[7].configure(text="FG:"+str(Fg))
labBUY[8].configure(text="FR:"+str(Fr))
labBUY[9].configure(text="Over G:>"+str(int(totalGreenSym)+1))
labBUY[10].configure(text="Over R:>"+str(int(totalRedSym)+1))
labBUY[11].configure(text="SYMBOL:->")
labBUY[12].configure(text="Quntity:->")

def lab7(message):
    
    global sp10
    x1=json.loads(message)
    i=len(listT)
    j=-1
    CRED10=REDBOOL10.count(True)
    labBUY[5].configure(text=str(CRED10))
    
    
    
    if totalGreenSym < len(listT)- CRED10:
        labBUY[5].configure(bg="GREEN")
        z3.configure(bg="GREEN")
        ALL_SP10.configure(bg="GREEN")
    if totalRedSym < CRED10:
        labBUY[5].configure(bg="RED")
        z3.configure(bg="RED")
        ALL_SP10.configure(bg="RED")
    if not(totalGreenSym < len(listT)- CRED10) and  not(totalRedSym < CRED10):
        labBUY[5].configure(bg="YELLOW")
        z3.configure(bg="YELLOW")
        ALL_SP10.configure(bg="YELLOW")
    

    while j<i:
        j+=1
        if str(listT[j]) == str(x1[0]['sym']) :
             
            try:
                if counbid1[j]>9:
                    counbid1[j]=1
                    sp10[j]=lidf[j]['speed'].sum()/10

                labvalue[j].configure(text=str(round(sp10[j],4)))
                if sp10[j] >0:
                    labvalue[j].configure(bg="GREEN")
                    REDBOOL10[j]=False
                if sp10[j] ==0:
                    labvalue[j].configure(bg="YELLOW")
                if sp10[j] <0:
                    labvalue[j].configure(bg="RED")
                    REDBOOL10[j]=True

                counbid1[j]+=1
                if pSym.get() == str(x1[0]['sym']) :
                    z9.configure(text=str(x1[0]['p'])) 
                    if sp10[j] <0:
                        colorSP10.configure(bg="RED") 
                    if sp10[j] ==0:
                        colorSP10.configure(bg="YELLOW") 
                    if sp10[j] >0: 
                        colorSP10.configure(bg="GREEN") 
                       
                 
            except:
                print("erroe********************")
                dtime10=1
   
  
    
           
    



def lab6(message):
    global price
    x1=json.loads(message)
    i=len(listT)
    j=0
    CRED=REDBOOL.count(True)
    
    labBUY[2].configure(text=str(CRED))
    if totalGreenSym < len(listT)- CRED:
        labBUY[2].configure(bg="GREEN")
        z4.configure(bg="GREEN")
        All_SPAv.configure(bg="GREEN")
    if totalRedSym < CRED:
        labBUY[2].configure(bg="RED")
        z4.configure(bg="RED")
        All_SPAv.configure(bg="RED")
    if not(totalGreenSym < len(listT)- CRED) and  not(totalRedSym < CRED):
        labBUY[2].configure(bg="YELLOW")
        z4.configure(bg="YELLOW")
        All_SPAv.configure(bg="YELLOW")
      
    
    while j<i:
        if str(listT[j]) == str(x1[0]['sym']) :
            #dtime10= lidf[10]['time'][counbid[j]] -  lidf[j]['time'][counbid[2]]
           
            counbid[j]+=1
            if counbid[j]>9 :
                 counbid[j]=0
            lidf[j]['Price'][counbid[j]]=x1[0]['p']
            lidf[j]['time'][counbid[j]]=x1[0]['t'] 
            deti= lidf[j]['time'][counbid[j]] -  lidf[j]['time'][counbid[j-1]]
            dpri= lidf[j]['Price'][counbid[j]]-lidf[j]['Price'][counbid[j-1]]
            if deti >0 :
                speed = dpri*100/deti
                #print(speed)
                av= speed /deti
                if speed >0:
                    labspeed[j].configure(bg="GREEN")
                else:
                   labspeed[j].configure(bg="RED")   

                lidf[j]['speed'][counbid[j]] = float(speed)
                lidf[j]['Acc'][counbid[j]] =float(av)
                speedAv = lidf[j]['speed'].sum()/9
                accAv = lidf[j]['Acc'].sum()/9
                try:
                    if speedAv <0:
                        labspeedAv[j].configure(bg="RED")
                        REDBOOL[j]=True
                    if speedAv ==0:
                        labspeedAv[j].configure(bg="YELLOW")
                    if speedAv >0:
                        labspeedAv[j].configure(bg="GREEN")
                        REDBOOL[j]=False
                except:
                    print("ERRoR")
             
            labSym[j].configure(text=str(x1[0]['sym']))
            labPrice[j].configure(text=str(x1[0]['p']))
            
           # lidf[j]['AccColor'][counbid[j]])
            speedstr=str(round(speed,4))
            if speed < 0.001:
                speedstr="0000"
            labspeed[j].configure(text=speedstr)
            #labspeed[j].configure(bg=lidf[j]['spColor'][counbid[j]])
            labacc[j].configure(text=str(round(av,4)))

            labspeedAv[j].configure(text=str(round(speedAv,4)))
            labaccAv[j].configure(text=str(round(accAv,4)))
            
            

            timestamp=x1[0]['t']
            timestamp=str(timestamp)[0:10]
            dt_object = datetime.fromtimestamp(int(timestamp))
            labtime[j].configure(text=str(dt_object)[11:19])

            if pSym.get() == str(x1[0]['sym']) :
            
                price=float(lidf[j]['Price'][counbid[j]])
                ssale=str(round((price-priceBuy)*int(pqunt.get())-20,4))
                lsale1.configure(text="Gain:"+ssale)
                #print(speedAv)
                
                if float(speedAv) < 0:
                    #print("RED")
                    colorSPAv.configure(bg="RED")  
                if float(speedAv) == 0:
                    colorSPAv.configure(bg="YELLOW")
                    #print("y")
                      
                if float(speedAv) > 0:
                    colorSPAv.configure(bg="GREEN")
                    #print("GREEN")
                      
               

                

        #print(pSym.get())
        #lidf[j].to_excel("o"+str(j)+".xls")      
        j+=1
        


 #------------------------------------------------- 



def my_customer_process_message(message):
    lab6(message)
    lab7(message)
    root.update()
   
    
    


def main():
    key = ''
    my_client = WebSocketClient(STOCKS_CLUSTER, key, my_customer_process_message)
    my_client.run_async()


    #my_client.subscribe("T.GE", "T.PYPL","T.SHOP" ,"T.SPY" , "T.SQ", "T.STM","T.TSM" )
    my_client.subscribe(sstemp)
    
    #time.sleep(.5)

    #my_client.close_connection()
    
    root.update()
    root.mainloop()


if __name__ == "__main__":
    main()

 
    


