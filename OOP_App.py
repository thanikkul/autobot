from tkinter import *

# root = Tk()
# root.title('First aid - App')

# app_Width = 396
# app_Height = 702

# scnWidth = root.winfo_screenwidth()
# scnHeight = root.winfo_screenheight()

# xPos = int(scnWidth / 2 - app_Width / 2)
# yPos = int(scnHeight / 2 - app_Height / 2)
# root.geometry('{}x{}+{}+{}'.format(app_Width, app_Height, xPos, yPos))


class StartPage():
    def __init__(self, root):
        self.frame = Label(root, text='Start Typing...',
                           font=('Helvetica', 20), fg='grey').pack()
        self.my_entry = Entry(root, font=('Helvetica', 14))
        self.my_entry.pack()
        self.my_listbox = Listbox(root, width=50)
        self.my_listbox.pack(pady=25)
        #self.data = []

    def check(self,e):
        typed = self.my_entry.get()

        if typed == '':
            data = self.data_list()[0]
        else:
            data = []
            for item in self.data_list()[0]:
                if typed.lower() in item.lower():
                    data.append(item)
            self.update(data)

    def go(self,e):
        cs = self.my_listbox.curselection()
        # Setting Background Colour
        for i in cs:
            # if list == 0:
            #     my_list.configure(background='red')
            try:
                if self.data_list()[1][self.my_listbox.get(cs)] == 'palevioletred':
                    self.my_listbox.configure(background=self.data_list()[
                                              1][self.my_listbox.get(cs)])
                elif self.data_list()[1][self.my_listbox.get(cs)] == 'slateblue':
                    self.my_listbox.configure(background=self.data_list()[
                                              1][self.my_listbox.get(cs)])
            except:
                if i == 0:
                    self.my_listbox.configure(background='lightcoral')
                elif i == 1:
                    self.my_listbox.configure(background='hotpink')
                elif i == 2:
                    self.my_listbox.configure(background='white')
                elif i == 3:
                    self.my_listbox.configure(background='gold')
                elif i == 4:
                    self.my_listbox.configure(background='darkkhaki')
                elif i == 5:
                    self.my_listbox.configure(background='lavender')
                elif i == 6:
                    self.my_listbox.configure(background='aquamarine')
                elif i == 7:
                    self.my_listbox.configure(background='lawngreen')
                elif i == 8:
                    self.my_listbox.configure(background='blueviolet')
                elif i == 9:
                    self.my_listbox.configure(background='dodgerblue')
                elif i == 10:
                    self.my_listbox.configure(background='gainsboro')

    def data_list(self):
        toppings = ['การช่วยฟื้นคืนชีพ (CPR)', 'ไฟไหม้หรือน้ำร้อนลวก', 'เลือดกำเดาไหล', 'แผลที่เกิดจากของมีคมบาด',
                         'บาดแผลกระดูกหัก', 'แมลงกัดต่อย', 'บาดแผลถลอก', 'บาดแผลฟกช้ำ', 'ความดันต่ำ/หน้ามืด/เวียนศีรษะ',
                         'หมดสติ', 'การห้ามเลือด']
        data_topic = {'เลือดกำเดาไหล': 'palevioletred',
                           'ไฟไหม้หรือน้ำร้อนลวก': 'slateblue'}
        return toppings, data_topic

    def update(self, data):
        # clear the listbox
        self.my_listbox.delete(0, END)

        # add toppings to listbox
        for item in data:
            self.my_listbox.insert(END, item)

    def fillout(self,e):
        # delete whatever is in the entrry box
        self.my_entry.delete(0, END)

        # add clicked list item to entry box
        self.my_entry.insert(0, self.my_listbox.get(ACTIVE))

    @property
    def event(self):
        self.my_listbox.bind('<<ListboxSelect>>', self.fillout)

        self.my_entry.bind('<KeyRelease>', self.check)

        self.my_listbox.bind('<Double-1>', self.go)
        self.my_listbox.pack()

        self.update(self.data_list()[0])

    # def run(self):
    #     self.event()


root = Tk()
root.title('First aid - App')

app_Width = 396
app_Height = 702

scnWidth = root.winfo_screenwidth()
scnHeight = root.winfo_screenheight()

xPos = int(scnWidth / 2 - app_Width / 2)
yPos = int(scnHeight / 2 - app_Height / 2)
root.geometry('{}x{}+{}+{}'.format(app_Width, app_Height, xPos, yPos))
app = StartPage(root)
app.event
root.mainloop()
