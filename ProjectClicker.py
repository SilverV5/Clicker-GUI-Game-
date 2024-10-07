import tkinter as tk


points = 0
click_power = 1
per_second = 0
per_second_switch = False
window = tk.Tk()
window.geometry("860x420")
window.title("Project Clicker")

def click():
    global points, click_power
    points += click_power
    clicking_point.config(text=f"Points: {points}")
    pass
    
    

def upgrade1():
    global points
    if points >= 15:
        points -= 15
        clicking_point.config(text=f"Points: {points}")
        # use thise for next upgrade per sec type thing window.after(0, upgrade1_update)
        upgrade1_update()
        
    else:
        brokie.config(text='Not Enough Points!')
        brokie.pack()
        brokie.after(5000, brokie.forget)

def upgrade1_update():
    global click_power
    click_power += 1
    power_display.config(text=f"Clicking Power: {click_power}")
    
    
def upgrade2():
    global points , per_second , per_second_switch, persec_display
    if points >= 20:
        points -=20
        clicking_point.config(text=f"Points: {points}")
        per_second += 1
        persec_display.config(text=f"Per Second Power: {per_second}")
        if not per_second_switch:
            per_second_switch = True
            upgrade2_persec()
    else:
        brokie.config(text='Not Enough Points!')
        brokie.pack()
        brokie.after(5000, brokie.forget)
              

def upgrade2_persec():
    global per_second , points
    points += per_second 
    clicking_point.config(text=f"Points: {points}")
    window.after(1000, upgrade2_persec)



clicking_point = tk.Label(text="Points: 0")

gain_button = tk.Button(
    text="+ 1",
    width=5,
    height=1,
    command=click   
)


upgrade_button1 = tk.Button(
    text="(+1 Clicking Power) Cost: 15", #potential hover effect in future to show effects
    command=upgrade1
)

upgrade_button2 = tk.Button(
    text="(+1/S) Cost: 20", 
    command=upgrade2
)



brokie = tk.Label()
power_display = tk.Label(text=f"Clicking Power: {click_power}")
power_display.place(x=10,y=10)

persec_display = tk.Label(text=f"Per Second Power: {per_second}")
persec_display.place(x=10,y=40)




cost1 = tk.Label(text="Cost: 15")

clicking_point.pack()
gain_button.pack()
upgrade_button1.pack()
upgrade_button2.pack()


window.mainloop()