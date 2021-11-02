import tkinter as tk
import re
import bs4
import requests

URL = r"http://lib.ru/PROZA/"

def bsParse():
    response = requests.get(URL)
    htmlCode = response.text
    soup = bs4.BeautifulSoup(htmlCode, features="lxml")
    lis = soup.find_all("li")
    result =""
    for li in lis:
        author = li.find_all("b")[1].text
        num = li.find_all("small")[0].text
        result += f"{num}\t{author}\n"
    return result.strip()

def reParse():
    response = requests.get(URL)
    htmlCode = response.text
    soup = bs4.BeautifulSoup(htmlCode, features="lxml")
    text = soup.get_text()
    text1 =re.sub("[(|)|\[|\]|dir|www]", "", text)
    return text1.strip()

def buttonClick(ctrl, method):
    """Универсальный обработчик нажатия кнопки"""
    ctrl.delete("1.0", tk.END)
    ctrl.insert(tk.END, bsParse() if method == "bs" else reParse())


form = tk.Tk()
form.title("КТ 4")
editText = tk.Text(height=30, width=70, wrap=tk.WORD)
editText.pack()
bsButton = tk.Button(text="Спарсить библиотекой", command=lambda: buttonClick(editText, method="bs"))
bsButton.pack()
reButton = tk.Button(text="Спарсить регулярками", command=lambda: buttonClick(editText, method="re"))
reButton.pack()

form.mainloop()
