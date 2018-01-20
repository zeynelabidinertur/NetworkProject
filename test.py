import Tkinter as tk
import anydbm
import pickle as pk
from tkFileDialog import askopenfilename
import re
from ScrolledText import ScrolledText


class FetchData(object):
    def __init__(self):
        print "Hej more!"


class newWords(FetchData):
    def __init__(self, new_master):
        super(newWords, self).__init__()
        new_master.title("New Words")
        self.new_master = new_master

        # define our frames

        upperCanvas = tk.Canvas(new_master, width=800, height=50)
        upperCanvas.create_text(350, 15, text="new Words",
                                font=("Calibri", 14, "bold"), anchor="w")

        upperCanvas.create_text(135, 40, text="Books" + " " * 70 + "Known Words" + " " * 24 + "Unknown Words",
                                font=("Calibri", 12), anchor="w", )
        upperFrame = tk.Frame(new_master, relief="groove", borderwidth=3)
        lowerCanvas = tk.Canvas(new_master, width=800, height=50)
        lowerCanvas.create_text(245, 40, text="All Words" + " " * 18 + "Outside Words",
                                font=("Calibri", 12), anchor="w", )
        lowerFrame = tk.Frame(new_master, relief="groove", borderwidth=3)

        upperCanvas.pack(side=tk.TOP, fill=tk.BOTH)
        upperFrame.pack(side=tk.TOP, fill=tk.BOTH)
        lowerCanvas.pack(side=tk.TOP, fill=tk.BOTH)
        lowerFrame.pack(side=tk.TOP, fill=tk.BOTH)

        # upper Frame

        shto = tk.Button(upperFrame, text="Add a\nbook!", command=self.shtoNjeLiber)
        libratScrollbar = tk.Scrollbar(upperFrame)
        self.librat = tk.Listbox(upperFrame, yscrollcommand=libratScrollbar.set,
                                 width=40)
        for book in generalDict["All"]:
            self.librat.insert(tk.END, book)

        self.librat.bind('<<ListboxSelect>>', self.libratSelection)
        libratScrollbar.config(command=self.librat.yview)
        hape = tk.Button(upperFrame, text="Open", command=self.hapeLibrin)
        largo = tk.Button(upperFrame, text="Delete the\nbook!", command=self.largoLibrin)
        fn1Scrollbar = tk.Scrollbar(upperFrame)
        self.fn1 = tk.Listbox(upperFrame, yscrollcommand=fn1Scrollbar.set, selectmode="multiple", )
        self.fn1.bind('<<ListboxSelect>>', self.fn1Selection)
        fn1Scrollbar.config(command=self.fn1.yview)

        ntmajt = tk.Button(upperFrame, text="<=", command=self.passButton)
        ntdjatht = tk.Button(upperFrame, text="=>", command=self.passButton2)
        fp1Scrollbar = tk.Scrollbar(upperFrame)
        self.fp1 = tk.Listbox(upperFrame, yscrollcommand=fp1Scrollbar.set, selectmode="multiple")
        self.fp1.bind('<<ListboxSelect>>', self.fp1Selection)
        fp1Scrollbar.config(command=self.fp1.yview)

        shto.grid(row=0, column=0, rowspan=2, padx=(10, 10))
        self.librat.grid(row=0, column=1, rowspan=2, padx=(10, 0))
        libratScrollbar.grid(row=0, column=2, rowspan=2, sticky=tk.N + tk.S, padx=(0, 10))
        hape.grid(row=0, column=3, padx=(10, 10), pady=(30, 10))
        largo.grid(row=1, column=3, rowspan=1, padx=(10, 10), pady=(10, 30))
        self.fn1.grid(row=0, column=4, rowspan=2, padx=(20, 0))
        fn1Scrollbar.grid(row=0, column=5, rowspan=2, sticky=tk.N + tk.S, padx=(0, 10))
        ntmajt.grid(row=0, column=6, rowspan=1, padx=(10, 10), pady=(30, 0))
        ntdjatht.grid(row=1, column=6, padx=(10, 10), pady=(0, 30))
        self.fp1.grid(row=0, column=7, rowspan=2, padx=(10, 0))
        fp1Scrollbar.grid(row=0, column=8, rowspan=2, sticky=tk.N + tk.S,
                          padx=(0, 10))

        # lower Frame

        fnScrollbar = tk.Scrollbar(lowerFrame)
        self.fn = tk.Listbox(lowerFrame, yscrollcommand=fnScrollbar.set)
        self.fn.bind('<<ListboxSelect>>', self.fnSelection)
        fnScrollbar.config(command=self.fn.yview)
        for i in range(19):
            self.fn.insert(i)

        fpScrollbar = tk.Scrollbar(lowerFrame)
        self.fp = tk.Listbox(lowerFrame, yscrollcommand=fpScrollbar.set, height=10)
        self.fp.bind('<<ListboxSelect>>', self.fpSelection)
        fpScrollbar.config(command=self.fp.yview)

        self.fn.grid(row=0, column=0, padx=(230, 0))
        fnScrollbar.grid(row=0, column=1, padx=(0, 30), sticky=tk.N + tk.S)

        self.fp.grid(row=0, column=2, padx=(10, 0))
        fpScrollbar.grid(row=0, column=3, sticky=tk.N + tk.S)

        self.emptyspaces = []
        for i in range(20):
            self.emptyspaces.append("" * i)
        self.libratValue = "[]"

    def shtoNjeLiber(self):
        global libratList
        filename = askopenfilename(filetypes=[("Word Files", ('.docx', '.txt'))])
        if filename == "":
            return
        fileTitle = re.split("/", filename)[-1].split(".")[0]
        fileTitle_ = ""

        for word in fileTitle.split():
            fileTitle_ += re.sub("\W", "", word)
            fileTitle_ += " "

        fileTitle = fileTitle_
        while fileTitle in libratList:
            fileTitle += "_"
        libratList.append(fileTitle)

        self.librat.insert(tk.END, fileTitle)
        self.extractWords(fileTitle, filename)

    def extractWords(self, fileTitle, filename):
        global generalDict
        fileTitle = str(fileTitle)
        words_list = []
        words_number = {}
        file1 = open(filename)
        bookText = ""

        for line in file1:
            bookText += line
            line = line.lower()

            for word in re.split("[^A-Za-z]", line):
                word = word.strip()
                if word == "":
                    continue
                else:
                    if word in words_number:
                        words_number[word] += 1
                    else:
                        words_number[word] = 1
        generalDict["Text"][fileTitle] = bookText

        for word in words_number:
            words_list.append((words_number[word], word))

        words_list.sort()
        words_list.reverse()
        generalDict["Known"][fileTitle] = {}
        generalDict["Unknown"][fileTitle] = {}
        generalDict["Outside"][fileTitle] = {}
        generalDict["All"][fileTitle] = words_list




    def libratSelection(self, event):

        global fp1List
        global libratIndex
        fp1List = []
        self.fp1.delete(0, tk.END)
        self.fn1.delete(0, tk.END)
        self.fp.delete(0, tk.END)
        self.fn.delete(0, tk.END)
        listbox = event.widget
        if listbox.get(0) == "":
            return
        libratIndex = listbox.curselection()[0]
        self.libratValue = listbox.get(libratIndex)
        self.fp1.insert(tk.END, self.libratValue)
        self.fp1.insert(tk.END, "")
        listedWords = []
        for word in generalDict["Unknown"][self.libratValue]:
            listedWords.append(word)
        listedWords.sort()
        for word in listedWords:
            self.fp1.insert(tk.END, word)
        self.fn1.insert(tk.END, self.libratValue)
        self.fn1.insert(tk.END, "")
        listedWords = []
        for word in generalDict["Known"][self.libratValue]:
            listedWords.append(word)
        listedWords.sort()
        for word in listedWords:
            self.fn1.insert(tk.END, word)
        self.fp.insert(tk.END, self.libratValue)
        self.fp.insert(tk.END, "")
        listedWords = []
        for word in generalDict["Outside"][self.libratValue]:
            listedWords.append(word)
        listedWords.sort()
        for word in listedWords:
            self.fp.insert(tk.END, word)

        for count1, word in generalDict["All"][self.libratValue]:
            self.fn.insert(tk.END, str(count1) + "  " + word)

    def largoLibrin(self):
        global generalDict
        global fp1List
        global libratList
        if libratIndex == None:
            return
        self.librat.delete(libratIndex)
        generalDict["Unknown"].pop(self.libratValue)
        generalDict["Known"].pop(self.libratValue)
        generalDict["Outside"].pop(self.libratValue)
        generalDict["All"].pop(self.libratValue)
        libratList.remove(self.libratValue)
        self.fp1.delete(0, tk.END)
        self.fn1.delete(0, tk.END)
        self.fp.delete(0, tk.END)
        self.fn.delete(0, tk.END)
        fp1List = []

    def hapeLibrin(self):
        pass

    def passButton(self):
        pass

    def passButton2(self):
        pass

    def fn1Selection(self, event):
        global fn1List
        global libratIndex
        libratIndex = None
        fn1List = []
        listBox = event.widget
        listindexS = listBox.curselection()

        for index in listindexS:
            value = listBox.get(index)
            fn1List.append((index, value))
        fn1List.reverse()

    def fp1Selection(self, event):
        global libratIndex
        global fp1List
        libratIndex = None
        fp1List = []
        listBox = event.widget
        listindexS = listBox.curselection()

        for index in listindexS:
            value = listBox.get(index)
            fp1List.append((index, value))
        fp1List.reverse()

    def fnSelection(self, event):
        global libratIndex
        global fp1List
        libratIndex = None
        fp1List = []

    def fpSelection(self, event):
        global libratIndex
        global fp1List
        libratIndex = None
        fp1List = []


if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(1, 1)
    root.geometry("800x450+300+100")
    newWords(root)
    root.mainloop()
