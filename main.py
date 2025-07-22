import subprocess
import tkinter as tk

def Ping():
    ip = IPInput.get()
    fps = int(FPsEntry.get()) + 1
    fp = int(FPEntry.get())

    splitip = ip.split('.')
    loctet = int(splitip[3])

    techip = (loctet - fp) + fps
    techip = str(f"{splitip[0]}.{splitip[1]}.{splitip[2]}.{techip}")
    print(techip)

    out = subprocess.run(['ping', '-c', '4', ip], capture_output=True)
    out = out.stdout.decode()




#IP = 'google.com'

# out = subprocess.run(['ping', '-c', '4', IP], capture_output=True)
# out = out.stdout.decode()


# recieve = out.find("received")

# print(out[recieve - 2])

root = tk.Tk()
root.title('Dispenser Ping')
root.geometry('500x500')

root.columnconfigure(0, weight=1)

frame = tk.Frame(root)
frame.grid(row=0, column=0)

IPLabel = tk.Label(frame, text="What is the IP address of the\ndispenser you are trying to ping")
IPLabel.grid(row=0, column=0, pady=5)

IPInput = tk.Entry(frame, width=20)
IPInput.grid(row=0, column=1, pady=5)

FPsLabel = tk.Label(frame, text="How many fueling points are at this site")
FPsLabel.grid(row=1, column=0, pady=5)

FPsEntry = tk.Entry(frame, width=20)
FPsEntry.grid(row=1, column=1, pady=5)

FPLabel = tk.Label(frame, text="What Fueling Point are you trying to ping")
FPLabel.grid(row=2, column=0, pady=5)

FPEntry = tk.Entry(frame, width=20)
FPEntry.grid(row=2, column=1, pady=5)

HelpButton = tk.Button(frame, text="Help")
HelpButton.grid(row=3, column=0, pady=5)

PingButton = tk.Button(frame, text="Ping", command=Ping)
PingButton.grid(row=3, column=1, pady=5)

root.mainloop()


#loss = out.stdout.decode().find("packet loss")

#print(out.stdout.decode()[loss:loss+5])

#print (out.stdout.decode().find("packet loss"))