import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image  # pip install pillow
import os  # dostęp do katalogu
import random

class LoginForn:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.state('zoomed')
        self.window.resizable(0, 0)

        # Inicjalizacja listy użytych obrazów
        self.used_images = []

        # TŁO
        self.bg_frame = Image.open('tlo.png')
        self.bg_frame = self.bg_frame.resize((self.window.winfo_screenwidth(), self.window.winfo_screenheight()))  # skaluje rozmiar do wielkosci aplikacji
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.place(x=0, y=0, relwidth=1, relheight=1)  # umieszczenie panelu na calej przestrzeni okna

        # LOGIN RAMKA
        self.login_frame = Frame(self.window, bg='#040405', width='950', height=600)
        self.login_frame.place(x=200, y=70)

        self.txt = 'TEST NA DALTONIZM'
        self.heading = Label(self.login_frame, text=self.txt, font=('yu gothic ui', 25, 'bold'), bg='#040405', fg='white')
        self.heading.place(x=80, y=30, width=500, height=30)

        # LEWA STRONA ZDJĘCIE
        self.side_left = Image.open('logowanie.jpg')
        photo = ImageTk.PhotoImage(self.side_left)
        self.side_left_label = Label(self.login_frame, image=photo, bg='#040405')  # to bg to jest zeby sie zrobilo na obrazku czarne tlo
        self.side_left_label.image = photo
        self.side_left_label.place(x=150, y=100)

        # OBRAZ LOGOWANIA
        self.sign_image = Image.open('mail2.jpg')
        self.sign_image = self.sign_image.resize((120, 120))
        photo = ImageTk.PhotoImage(self.sign_image)
        self.sign_image_label = Label(self.login_frame, image=photo, bg='#040405')  # to bg to jest zeby sie zrobilo na obrazku czarne tlo
        self.sign_image_label.image = photo
        self.sign_image_label.place(x=625, y=130)

        self.sign_label = Label(self.login_frame, text='Podaj maila', bg='#040405', fg='white', font=('yu gothic ui', 13, 'bold'))
        self.sign_label.place(x=640, y=240)

        # LOGOWANIE
        self.username_label = Label(self.login_frame, text='Mail', bg='#040405', font=('yu gothic ui', 13, 'bold'), fg='#4f4e4d')
        self.username_label.place(x=550, y=300)

        self.username_entry = Entry(self.login_frame, highlightthickness=0, relief=FLAT, bg='#040405', fg='#6b6a69', font=('yu gothic ui', 12, 'bold'))
        self.username_entry.place(x=580, y=335, width=270)

        self.username_line = Canvas(self.login_frame, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.username_line.place(x=550, y=359)

        # IKONA PRZY LOGOWANIU
        self.username_icon = Image.open('mail.jpg')
        self.username_icon = self.username_icon.resize((30, 30))
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.login_frame, image=photo, bg='#040405')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=325)

        self.next_button = Button(self.login_frame, text='Dalej', bg='#6b6a69', fg='#bdb9b1', font=('yu gothic ui', 12, 'bold'), relief=FLAT, command=self.rules_page)
        self.next_button.place(x=620, y=400, width=140, height=40)

    def rules_page(self):
        self.login_frame.destroy()
        self.next_frame = Frame(self.window, bg='#bdb9b1', width='950', height=600)
        self.next_frame.place(x=200, y=70)
        label_rules = Label(self.next_frame, text='Przeczytaj zasady:', font=('yu gothic ui', 13, 'bold'), bg='#bdb9b1', fg='black')
        label_rules.place(x=400, y=20)

        rules_text = """

        1. Wyświetlone zostaną zdjęcia, pod którymi wpisz liczbę widoczną na zdjęciu i naciśnij przycisk dalej.

        2. W przypadku problemu z rozpoznaniem liczb, naciśnij przycisk dalej.

        3. Wynik zostanie wyświetlony po zakończonym teście.

        4. Po zakończeniu można zapisać swój wynik do bazy.

        5. Kliknij start aby rozpocząć test.
        """

        rules_label = Label(self.next_frame, text=rules_text, font=('yu gothic ui', 12), bg='#bdb9b1', fg='black', justify=LEFT)
        rules_label.place(x=20, y=50)

        self.start_button = Button(self.next_frame, text='Start', bg='#6b6a69', fg='#bdb9b1', font=('yu gothic ui', 12, 'bold'), relief=FLAT, command=self.start_test)
        self.start_button.place(x=410, y=450, width=140, height=40)

    def start_test(self):
        self.next_frame.destroy()
        self.used_images = []  # Resetowanie listy użytych obrazów
        self.used_images_count = 0
        self.correct_answers = 0  # Zmienna do przechowywania liczby poprawnych odpowiedzi
        self.test_frame = Frame(self.window, bg='#bdb9b1', width='950', height=600)
        self.test_frame.place(x=200, y=70)
        self.show_next_image()

    def show_next_image(self):
        if self.used_images_count == 15:  # Jeśli wyświetlono już 15 obrazów
            self.show_result()
            return

        while True:
            image_files = [file for file in os.listdir('dane') if file not in self.used_images]
            if not image_files:
                return

            random_image = random.choice(image_files)
            random_image_path = os.path.join('dane', random_image)

            if random_image not in self.used_images:
                break

        self.used_images.append(random_image)
        self.used_images_count += 1

        image = Image.open(random_image_path)
        image = image.resize((320, 300))
        self.photo = ImageTk.PhotoImage(image)

        self.image_label = Label(self.test_frame, image=self.photo, bg='black')
        self.image_label.image = self.photo
        self.image_label.place(x=325, y=50)

        # Tworzenie pola tekstowego na wpisanie odpowiedzi
        self.result_entry = Entry(self.test_frame, highlightthickness=0, relief=FLAT, bg='#040405', fg='white', font=('yu gothic ui', 12, 'bold'), justify='center')
        self.result_entry.place(x=325, y=380, width=323)

        self.next_button = Button(self.test_frame, text='Dalej', bg='#6b6a69', fg='#bdb9b1', font=('yu gothic ui', 12, 'bold'), relief=FLAT, command=self.evaluate_answer)
        self.next_button.place(x=410, y=450, width=140, height=40)

    def evaluate_answer(self):
        # Sprawdzanie czy odpowiedź jest poprawna
        user_answer = self.result_entry.get()
        current_image = self.used_images[self.used_images_count - 1]  # Aktualne zdjęcie
        if user_answer == current_image.split('.')[0]:
            self.correct_answers += 1

        # Czyszczenie pola tekstowego
        self.result_entry.delete(0, END)

        # Wyświetlanie kolejnego obrazka
        self.show_next_image()

    def show_result(self):
        self.test_frame.destroy()
        self.result_frame = Frame(self.window, bg='#bdb9b1', width='950', height='600')
        self.result_frame.place(x=200, y=70)
        result_label = Label(self.result_frame, text=f'Twój wynik: {self.correct_answers}/15', font=('yu gothic ui', 25, 'bold'), bg='#bdb9b1', fg='black')
        result_label.place(relx=0.5, rely=0.5, anchor='center')

def page():
    window = tk.Tk()
    LoginForn(window)
    window.mainloop()

if __name__ == '__main__':
    page()
