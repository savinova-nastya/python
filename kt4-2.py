import tkinter as tk
import re
import bs4
import requests

URL = r"https://teron.online/index.php?showforum=89"

try:
    def bsParse():
        response = requests.get(URL)
        htmlCode = response.text
        soup = bs4.BeautifulSoup(response.text, features="lxml")
        #tags = soup.find_all("a", class_="topic_title")
        #tagss = soup.find_all("a", class_="_hovertrigger")
        tags = soup.find_all("tr", class_="row2")
        result =""
        for tr in tags:
            text = tr.find("a", class_="topic_title").text
            author = tr.find("a", class_="_hovertrigger").text
            result += f"{text}\t{author}\n"
            #print(result)
        return result.strip()

    def reParse():
        response = requests.get(URL)
        htmlCode = response.text
        tags = re.split("row2", htmlCode)
        result = ""
        for tr in tags:
            match = re.search("class='topic_title'>(.+?)</a>.*?class=\"_hovertrigger\"[^>]*?>(.+?)</a>", tr,flags=re.DOTALL)
            if match:
                text, author = match.groups()
                result += f"{text}\t{author}\n"
        return result.strip()


    def buttonClick(ctrl, method: object):
        """Универсальный обработчик нажатия кнопки"""
        ctrl.delete("1.0", tk.END)
        ctrl.insert(tk.END, bsParse() if method == "bs" else reParse())


    form = tk.Tk()
    form.title("КТ 4, вариант 6")
    editText = tk.Text(height=30, width=70, wrap=tk.WORD)
    editText.pack()
    bsButton = tk.Button(text="Спарсить библиотекой", command=lambda: buttonClick(editText, method="bs"))
    bsButton.pack()
    reButton = tk.Button(text="Спарсить регулярками", command=lambda: buttonClick(editText, method="re"))
    reButton.pack()

    form.mainloop()


except Exception as e:
    print(e)