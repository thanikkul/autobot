from tkinter import *

root = Tk()
root.title('First aid - App')

app_Width = 396
app_Height = 702

scnWidth = root.winfo_screenwidth()
scnHeight = root.winfo_screenheight()

xPos = int(scnWidth / 2 - app_Width / 2)
yPos = int(scnHeight / 2 - app_Height / 2)
root.geometry('{}x{}+{}+{}'.format(app_Width, app_Height, xPos, yPos))


class StartPage():
    def __init__(self, root):
        self.frame = Label(root, text='Start Typing...',
                           font=('Helvetica', 20), fg='grey').pack()
        self.my_entry = Entry(root, font=('Helvetica', 14))
        self.my_entry.pack()
        self.my_listbox = Listbox(root, width=50)
        self.my_listbox.pack(pady=25)
        self.data = []

    def check(self):
        self.typed = self.my_entry.get()

        if self.typed == '':
            data = self.data_list()[0]
        else:
            self.data = []
            for item in self.data_list()[0]:
                if self.typed.lower() in item.lower():
                    self.data.append(item)
            self.update(self.data)

    def go(self):
        self.cs = self.my_listbox.curselection()
        # Setting Background Colour
        for list in self.cs:
            # if list == 0:
            #     my_list.configure(background='red')
            try:
                if self.data_list()[1][self.my_listbox.get(self.cs)] == 'palevioletred':
                    self.my_listbox.configure(background=self.data_list()[
                                              1][self.my_listbox.get(self.cs)])
                elif self.data_list()[1][self.my_listbox.get(self.cs)] == 'slateblue':
                    self.my_listbox.configure(background=self.data_list()[
                                              1][self.my_listbox.get(self.cs)])
            except:
                if list == 0:
                    self.my_listbox.configure(background='lightcoral')
                elif list == 1:
                    self.my_listbox.configure(background='hotpink')
                elif list == 2:
                    self.my_listbox.configure(background='white')
                elif list == 3:
                    self.my_listbox.configure(background='gold')
                elif list == 4:
                    self.my_listbox.configure(background='darkkhaki')
                elif list == 5:
                    self.my_listbox.configure(background='lavender')
                elif list == 6:
                    self.my_listbox.configure(background='aquamarine')
                elif list == 7:
                    self.my_listbox.configure(background='lawngreen')
                elif list == 8:
                    self.my_listbox.configure(background='blueviolet')
                elif list == 9:
                    self.my_listbox.configure(background='dodgerblue')
                elif list == 10:
                    self.my_listbox.configure(background='gainsboro')

    def data_list(self):
        self.toppings = ['การช่วยฟื้นคืนชีพ (CPR)', 'ไฟไหม้หรือน้ำร้อนลวก', 'เลือดกำเดาไหล', 'แผลที่เกิดจากของมีคมบาด',
                         'บาดแผลกระดูกหัก', 'แมลงกัดต่อย', 'บาดแผลถลอก', 'บาดแผลฟกช้ำ', 'ความดันต่ำ/หน้ามืด/เวียนศีรษะ',
                         'หมดสติ', 'การห้ามเลือด']
        self.data_topic = {'เลือดกำเดาไหล': 'palevioletred',
                           'ไฟไหม้หรือน้ำร้อนลวก': 'slateblue'}
        return self.toppings, self.data_topic

    def update(self, data):
        # clear the listbox
        self.my_listbox.delete(0, END)

        # add toppings to listbox
        for item in data:
            self.my_listbox.insert(END, item)

    def fillout(self):
        # delete whatever is in the entrry box
        self.my_entry.delete(0, END)

        # add clicked list item to entry box
        self.my_entry.insert(0, self.my_listbox.get(ACTIVE))

    def event(self):
        self.my_listbox.bind('<<ListboxSelect>>', self.fillout())

        self.my_entry.bind('<KeyRelease>', self.check())

        self.my_listbox.bind('<Double-1>', self.go())
        self.my_listbox.pack()

        self.update(self.data_list()[0])

    def run(self):
        self.event()


app = StartPage(root)
app.run()

root.mainloop()
