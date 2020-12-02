import tkinter
import tkinter.ttk
import random
import winsound
import threading
import time
import numpy as np
import re

hiragana1 = {'아': 'あ', '이': 'い', '우': 'う', '에': 'え', '오': 'ぉ', '카': 'か', '키': 'き', '쿠': 'く', '케': 'け', '코': 'こ',
             '사': 'さ', '시': 'し', '스': 'す', '세': 'せ', '소': 'そ', '타': 'た', '치': 'ち', '츠': 'つ', '테': 'て', '토': 'と',
             '나': 'な', '니': 'に', '누': 'ぬ', '네': 'ね', '노': 'の', '하': 'は', '히': 'ひ', '후': 'ふ', '헤': 'へ', '호': 'ほ',
             '마': 'ま', '미': 'み', '무': 'む', '메': 'め', '모': 'も', '야': 'や', '유': 'ゆ', '요': 'よ',
             '라': 'ら', '리': 'り', '루': 'る', '레': 'れ', '로': 'ろ', '와': 'わ', '목오': 'を', '응': 'ん'}
hiragana = ['あ', 'い', 'う', 'え', 'ぉ', 'か', 'き', 'く', 'け', 'こ',
            'さ', 'し', 'す', 'せ', 'そ', 'た', 'ち', 'つ', 'て', 'と',
            'な', 'に', 'ぬ', 'ね', 'の', 'は', 'ひ', 'ふ', 'へ', 'ほ',
            'ま', 'み', 'む', 'め', 'も', 'や', 'ゆ', 'よ',
            'ら', 'り', 'る', 'れ', 'ろ', 'わ', 'を', 'ん']
koriana = ['아', '이', '우', '에', '오', '카', '키', '쿠', '케', '코',
           '사', '시', '스', '세', '소', '타', '치', '츠', '테', '토',
           '나', '니', '누', '네', '노', '하', '히', '후', '헤', '호',
           '마', '미', '무', '메', '모', '야', '유', '요',
           '라', '리', '루', '레', '로', '와', '목오', '응']

gatakana1 = {'아': 'ア', '이': 'イ', '우': 'ウ', '에': 'エ', '오': 'オ', '카': 'カ', '키': 'キ', '쿠': 'ク', '케': 'ケ', '코': 'コ',
             '사': 'サ', '시': 'シ', '스': 'ス', '세': 'セ', '소': 'ソ', '타': 'タ', '치': 'チ', '츠': 'ツ', '테': 'テ', '토': 'ト',
             '나': 'ナ', '니': 'ニ', '누': 'ヌ', '네': 'ネ', '노': 'ノ', '하': 'ハ', '히': 'ヒ', '후': 'フ', '헤': 'ヘ', '호': 'ホ',
             '마': 'マ', '미': 'ミ', '무': 'ム', '메': 'メ', '모': 'モ', '야': 'ヤ', '유': 'ユ', '요': 'ヨ',
             '라': 'ラ', '리': 'リ', '루': 'ル', '레': 'レ', '로': 'ロ', '와': 'ワ', '목오': 'ヲ', '응': 'ン'}
gatakana = ['ア', 'イ', 'ウ', 'エ', 'オ', 'カ', 'キ', 'ク', 'ケ', 'コ',
            'サ', 'シ', 'ス', 'セ', 'ソ', 'タ', 'チ', 'ツ', 'テ', 'ト',
            'ナ', 'ニ', 'ヌ', 'ネ', 'ノ', 'ハ', 'ヒ', 'フ', 'ヘ', 'ホ',
            'マ', 'ミ', 'ム', 'メ', 'モ', 'ヤ', 'ユ', 'ヨ',
            'ラ', 'リ', 'ル', 'レ', 'ロ', 'ワ', 'ヲ', 'ン']
kotakana = ['아', '이', '우', '에', '오', '카', '키', '쿠', '케', '코',
            '사', '시', '스', '세', '소', '타', '치', '츠', '테', '토',
            '나', '니', '누', '네', '노', '하', '히', '후', '헤', '호',
            '마', '미', '무', '메', '모', '야', '유', '요',
            '라', '리', '루', '레', '로', '와', '목오', '응']

hi_rand_list = []; temp_hi_list = []
ga_rand_list = []; temp_ga_list = []

que_list = []; temp_que_list = []
my_answer_list = []; temp_my_answer_list = []

worng = []; temp_worng = []
worng_idx = []; temp_worng_idx = []

class Japanese:
    def __init__(self):
        self.sc = 0; self.cnt = 0; self.trans = 0; self.menu = 0; self.click = 0; self.total = 0; self.hi_rand = 0; self.ga_rand = 0
        self.stopped = False; self.on_time = True
        self.main()

    def main(self):
        self.window = tkinter.Tk()
        self.window.title("Japanese")
        self.window.geometry("600x550+650+150")
        self.window.resizable(False, False)
        self.window.iconbitmap('asd.ico')
        # self.window.configure(bg='lavender blush')

        self.backg = tkinter.PhotoImage(file="C:\\Users\\W45176\\Desktop\\asd\\aa.png")  # 다른 컴퓨터에서는 파일 주소 바꿔주기
        self.back_label = tkinter.Label(image=self.backg)
        self.back_label.pack()

        self.label1 = tkinter.Label(self.window, text="Japanese", width=8, height=1, bg='lavender blush')
        self.label1.config(font=("Courier", 40))
        self.label1.place(relx=0.3, rely=0.35)

        self.label2 = tkinter.Label(self.window, text=f"{self.sc}/{20}", width=5, height=1, bg='lavender blush')
        self.label2.config(font=("Courier", 20))
        self.label2.place(relx=0.8, rely=0.07)

        self.label3 = tkinter.Label(self.window, text=f"{self.cnt}", width=7, height=1, bg='lavender blush')
        self.label3.place(relx=0.33, rely=0.515)

        self.label4 = tkinter.Label(self.window, width=7, height=1, bg='lavender blush')
        self.label4.config(font=("Courier", 15))
        self.label4.place(relx=0.8, rely=0.15)

        self.button1 = tkinter.Button(self.window, width=10, text="Start", command=self.button_event, bg='lavender blush')
        self.button1.config(width=10, height=2)
        self.button1.place(relx=0.8, rely=0.8)

        self.button2 = tkinter.Button(self.window, width=10, text="히라가나", command=self.switch_to_hiragana, bg='linen')
        self.button2.config(width=7, height=1)
        self.button2.place(relx=0.04, rely=0.04)

        self.button3 = tkinter.Button(self.window, width=10, text="가타카나", command=self.switch_to_gatakana, bg='linen')
        self.button3.config(width=7, height=1)
        self.button3.place(relx=0.137, rely=0.04)

        self.button4 = tkinter.Button(self.window, width=10, command=self.new_window, bg='lavender blush', relief='flat', state='disabled')
        self.button4.config(width=11, height=2)
        self.button4.place(relx=0.8, rely=0.23)

        self.entry = tkinter.Entry(self.window, justify="center", width=37, bg='lavender blush', disabledbackground='lavender blush', readonlybackground='lavender blush')
        self.entry.bind("<Return>", self.entry_event)
        self.entry.place(relx=0.3, rely=0.6, height=35)
        self.entry.config(state='disabled')

        s = tkinter.ttk.Style()
        s.theme_use('clam')
        s.configure("red.Horizontal.TProgressbar", foreground='red', background='salmon')

        self.progressbar = tkinter.ttk.Progressbar(self.window, style="red.Horizontal.TProgressbar", length=100, mode="determinate")
        self.progressbar.place(x=265, y=285)

        self.thread = threading.Thread(target=self.pgbar)
        self.thread.daemon = True

        self.window.mainloop()

    def next_btn(self):
        num = re.findall("\d+", self.combo.get())
        idx = int(num[0]) - 1
        try:
            if(self.count<len(worng[self.total-1])):
                if(self.menu==0):
                    self.count+=1
                    self.new_label3.config(text=f"{hiragana1[worng[idx][self.count]]}", fg="red")
                    self.new_label4.config(text=f"{worng[idx][self.count]}", fg="red")
                    self.new_label6.config(text=f"{idx+1}-{worng_idx[idx][self.count]+1}", fg="red")
                    print(self.count)
                    #print(hiragana1[worng[idx][self.count]])
                    #print(worng[idx][self.count])
                else:
                    self.count += 1
                    self.new_label3.config(text=f"{gatakana1[worng[idx][self.count]]}", fg="red")
                    self.new_label4.config(text=f"{worng[idx][self.count]}", fg="red")
                    self.new_label6.config(text=f"{idx + 1}-{worng_idx[idx][self.count]+1}", fg="red")
                    print(self.count)
        except:
            pass
    def pre_btn(self):
        num = re.findall("\d+", self.combo.get())
        idx = int(num[0]) - 1
        if(self.count>0):
            if (self.menu == 0):
                self.count -= 1
                self.new_label3.config(text=f"{hiragana1[worng[idx][self.count]]}", fg="red")
                self.new_label4.config(text=f"{worng[idx][self.count]}", fg="red")
                self.new_label6.config(text=f"{idx+1}-{worng_idx[idx][self.count]+1}", fg="red")
                print(self.count)
            else:
                self.count -= 1
                self.new_label3.config(text=f"{gatakana1[worng[idx][self.count]]}", fg="red")
                self.new_label4.config(text=f"{worng[idx][self.count]}", fg="red")
                self.new_label6.config(text=f"{idx + 1}-{worng_idx[idx][self.count]+1}", fg="red")
                print(self.count)

    def new_window(self):
        self.new_window = tkinter.Toplevel(self.window)
        self.new_window.title("Result")
        self.new_window.geometry("650x350+625+150")
        self.new_window.resizable(False, False)

        self.new_label1 = tkinter.Label(self.new_window, width=120, height=25, bg='lavender blush')
        self.new_label1.pack()

        aa = que_list
        bb = my_answer_list
        idx = 0
        self.new_label2 = tkinter.Label(self.new_window, width=28, height=13, anchor='nw', bg='lavender blush')
        self.new_label2.config(font=("Courier", 17))
        #self.new_label2.config(text="아:あ 이:い 우:う 에:え 오:ぉ\n\n\n카:か 키:き 쿠:く 케:け 코:こ\n\n\n사:さ 시:し 스:す 세:せ 소:そ\n\n\n타:た 치:ち 츠:つ 테:て 토:と")
        self.new_label2.config(text=f"{aa[idx][0]}:{bb[idx][0]} {aa[idx][1]}:{bb[idx][1]} {aa[idx][2]}:{bb[idx][2]} {aa[idx][3]}:{bb[idx][3]} {aa[idx][4]}:{bb[idx][4]}\n\n\n{aa[idx][5]}:{bb[idx][5]} {aa[idx][6]}:{bb[idx][6]} {aa[idx][7]}:{bb[idx][7]} {aa[idx][8]}:{bb[idx][8]} {aa[idx][9]}:{bb[idx][9]}\n\n\n{aa[idx][10]}:{bb[idx][10]} {aa[idx][11]}:{bb[idx][11]} {aa[idx][12]}:{bb[idx][12]} {aa[idx][13]}:{bb[idx][13]} {aa[idx][14]}:{bb[idx][14]}\n\n\n{aa[idx][15]}:{bb[idx][15]} {aa[idx][16]}:{bb[idx][16]} {aa[idx][17]}:{bb[idx][17]} {aa[idx][18]}:{bb[idx][18]} {aa[idx][19]}:{bb[idx][19]}")
        self.new_label2.place(relx=0.06, rely=0.1)

        self.new_label5 = tkinter.Label(self.new_window, width=22, height=11, bg='lavender blush', relief="solid")
        self.new_label5.place(relx=0.7, rely=0.36)

        self.count = 0

        self.new_label3 = tkinter.Label(self.new_window, width=3, height=1, bg='lavender blush')
        self.new_label3.config(font=("Courier", 40))
        self.new_label3.place(relx=0.748, rely=0.43)
        self.new_label3.config(text=f"{hiragana1[worng[idx][self.count]]}",fg="red")

        self.new_label4 = tkinter.Label(self.new_window, width=4, height=1, bg='lavender blush')
        self.new_label4.config(font=("Courier", 15))
        self.new_label4.place(relx=0.784, rely=0.62)
        self.new_label4.config(text=f"{worng[idx][self.count]}",fg="red")

        self.new_label6 = tkinter.Label(self.new_window, width=4, height=1, bg='lavender blush')
        self.new_label6.config(font=("Courier", 9))
        self.new_label6.place(relx=0.72, rely=0.38)
        self.new_label6.config(text=f"{idx+1}-{worng_idx[idx][self.count]+1}", fg="red")


        self.new_button1 = tkinter.Button(self.new_window, text="▶",bg='lavender blush',command=self.next_btn)
        self.new_button1.config(width=3, height=1)
        self.new_button1.place(relx=0.88, rely=0.74)

        self.new_button2 = tkinter.Button(self.new_window, text="◀", bg='lavender blush',command=self.pre_btn)
        self.new_button2.config(width=3, height=1)
        self.new_button2.place(relx=0.72, rely=0.74)


        tot = []
        self.str = 0
        inning = np.arange(1, self.total + 1).tolist()
        for i in range(self.total):
            tot.append(f"{inning[i]}회차")

        self.combo = tkinter.ttk.Combobox(self.new_window, value=tot, state="readonly")
        self.combo.current(0)
        self.combo.bind("<<ComboboxSelected>>", self.show_result)
        self.combo.place(relx=0.7, rely=0.1, height=35)


    def show_result(self,none):
        num = re.findall("\d+",self.combo.get())
        idx = int(num[0])-1
        aa = que_list
        bb = my_answer_list
        self.count = 0

        self.new_label2 = tkinter.Label(self.new_window, width=28, height=13, anchor='nw', bg='lavender blush')
        self.new_label2.config(font=("Courier", 17))
        #self.new_label2.config(text="아:あ 이:い 우:う 에:え 오:ぉ\n\n\n카:か 키:き 쿠:く 케:け 코:こ\n\n\n사:さ 시:し 스:す 세:せ 소:そ\n\n\n타:た 치:ち 츠:つ 테:て 토:と")
        self.new_label2.config(text=f"{aa[idx][0]}:{bb[idx][0]} {aa[idx][1]}:{bb[idx][1]} {aa[idx][2]}:{bb[idx][2]} {aa[idx][3]}:{bb[idx][3]} {aa[idx][4]}:{bb[idx][4]}\n\n\n{aa[idx][5]}:{bb[idx][5]} {aa[idx][6]}:{bb[idx][6]} {aa[idx][7]}:{bb[idx][7]} {aa[idx][8]}:{bb[idx][8]} {aa[idx][9]}:{bb[idx][9]}\n\n\n{aa[idx][10]}:{bb[idx][10]} {aa[idx][11]}:{bb[idx][11]} {aa[idx][12]}:{bb[idx][12]} {aa[idx][13]}:{bb[idx][13]} {aa[idx][14]}:{bb[idx][14]}\n\n\n{aa[idx][15]}:{bb[idx][15]} {aa[idx][16]}:{bb[idx][16]} {aa[idx][17]}:{bb[idx][17]} {aa[idx][18]}:{bb[idx][18]} {aa[idx][19]}:{bb[idx][19]}")
        self.new_label2.place(relx=0.06, rely=0.1)

        print(worng_idx)

        if(self.menu == 0):
            self.new_label3.config(text=f"{hiragana1[worng[idx][self.count]]}", fg="red")
            self.new_label4.config(text=f"{worng[idx][self.count]}", fg="red")
            self.new_label6.config(text=f"{idx + 1}-{worng_idx[idx][self.count]+1}", fg="red")
            print(self.count)

        else:
            self.new_label3.config(text=f"{gatakana1[worng[idx][self.count]]}", fg="red")
            self.new_label4.config(text=f"{worng[idx][self.count]}", fg="red")
            self.new_label6.config(text=f"{idx + 1}-{worng_idx[idx][self.count]+1}", fg="red")
            print(self.count)



    def pgbar(self):
        max = 20
        x = 0
        while (True):
            if (x <= max):
                if (self.stopped == True):
                    x = 0
                    self.progressbar["value"] = 0
                    self.stopped = False
                if (self.cnt == 20):
                    x = 0
                    self.progressbar["value"] = 0
                time.sleep(0.1)
                self.progressbar["value"] += 5
                x += 1
                # self.window.update_idletasks()
            else:
                winsound.Beep(120, 150)
                if (self.cnt > 20):
                    x = 0
                    self.progressbar["value"] = 0
                    break
                x = 0
                self.progressbar["value"] = 0
                self.on_time = False
                temp_my_answer_list.append("Ⅹ")

                if (self.menu == 0):
                    self.hiragana_check()
                else:
                    self.gatakana_check()

    def button_event(self):
        if (self.click == 0):
            self.thread.start()
            self.click += 1
        rand = random.randint(0, 45)
        self.cnt = 0
        self.sc = 0

        self.label2.config(text=f'{self.sc}/{20}')

        if (self.menu == 0):
            temp_hi_list.append(rand)
            temp_que_list.append(hiragana[rand])
            self.label1.config(text=f'{hiragana[rand]}')

        else:
            temp_ga_list.append(rand)
            temp_que_list.append(gatakana[rand])
            self.label1.config(text=f'{gatakana[rand]}')

        self.label3.config(text=f"{self.cnt+1}")
        self.button4.config(text='', state='disabled',relief="flat")
        self.label4.config(text=f"")
        self.entry.config(state='normal')
        self.button1.config(state='disabled')

    def entry_event(self, event):
        print("cnt = ", self.cnt)
        if (self.cnt < 20):
            if (self.menu == 0):
                try:
                    self.word = tkinter.Entry.get(self.entry)
                    temp_my_answer_list.append(self.word)
                    self.hiragana_check()
                    self.stopped = True
                    if (self.cnt < 20):
                        self.label3.config(text=f'{self.cnt + 1}')

                except:
                    pass

            else:
                try:
                    self.word = tkinter.Entry.get(self.entry)
                    temp_my_answer_list.append(self.word)
                    self.gatakana_check()
                    self.label3.config(text=f'{self.cnt+1}')
                    self.stopped = True
                    if (self.cnt < 20):
                        self.label3.config(text=f'{self.cnt+1}')

                except:
                    pass
        #print(temp_que_list,len(temp_que_list))
        #print(temp_my_answer_list, len(temp_my_answer_list))
        #print(temp_hi_list, len(temp_hi_list))
        #print(temp_worng)
        #print(worng)

        self.entry.delete(0, "end")

    def hiragana_check(self):
        self.hi_rand = random.randint(0, 45)
        if (self.on_time == True):
            if self.word in hiragana1:
                if (hiragana1[self.word] == hiragana[temp_hi_list[-1]]):  # 입력한 한글과 일본어가 맞는지 판단하는 코드
                    self.cnt += 1
                    self.sc += 1
                    self.label2.config(text=f"{self.sc}/{20}")
                    winsound.Beep(100, 70)

                else:
                    self.cnt += 1
                    temp_worng.append(koriana[temp_hi_list[-1]])
                    winsound.Beep(120, 150)
            else:
                temp_worng.append(koriana[temp_hi_list[-1]])
                self.cnt += 1
                winsound.Beep(120, 150)

            if (self.trans == 1):
                del temp_hi_list[-1]
                self.trans = 0
        else:
            if(self.cnt < 20):
                temp_worng.append(koriana[temp_hi_list[-1]])
            self.cnt += 1
            self.label3.config(text=f'{self.cnt+1}')

        while self.hi_rand in temp_hi_list:  # 같은 글자가 안나오게 해주는 코드
            self.hi_rand = random.randint(0, 45)

        if (self.cnt < 20):
            temp_hi_list.append(self.hi_rand)
            self.label1.config(text=f'{hiragana[temp_hi_list[-1]]}')
            temp_que_list.append(hiragana[self.hi_rand])
            self.on_time = True
        else:
            self.entry.delete(0, "end")
            self.label1.config(text=f'Finish')
            self.label4.config(text=f"Acc:{self.sc * 5}%")
            self.button1.config(state='normal')
            self.entry.config(state='disabled')
            self.button4.config(text='Result', state='normal', relief='solid')
            self.total += 1

            for i in temp_worng:
                temp_worng_idx.append(temp_que_list.index(hiragana1[i]))
            worng_idx.append(temp_worng_idx[:])
            temp_worng_idx.clear()


            if (self.cnt == 20):
                hi_rand_list.append(temp_hi_list[:])
                que_list.append(temp_que_list[:])
                my_answer_list.append(temp_my_answer_list[:])
                worng.append(temp_worng[:])
                temp_hi_list.clear()
                temp_que_list.clear()
                temp_my_answer_list.clear()
                temp_worng.clear()

                #print(hi_rand_list)
                #print(que_list)
                #print(my_answer_list)
                #print(self.total)ㅁ



    def gatakana_check(self):
        self.ga_rand = random.randint(0, 45)
        if (self.on_time == True):
            if self.word in gatakana1:
                if (gatakana1[self.word] == gatakana[temp_ga_list[-1]]):
                    self.cnt += 1
                    self.sc += 1
                    self.label2.config(text=f"{self.sc}/{20}")
                    winsound.Beep(100, 50)

                else:
                    self.cnt += 1
                    temp_worng.append(kotakana[temp_ga_list[-1]])
                    winsound.Beep(120, 150)
            else:
                temp_worng.append(kotakana[temp_ga_list[-1]])
                self.cnt += 1
                winsound.Beep(120, 150)

            if (self.trans == 2):
                del temp_ga_list[-1]
                self.trans = 0

        else:
            if (self.cnt<20):
                temp_worng.append(kotakana[temp_ga_list[-1]])
            self.cnt += 1
            self.label3.config(text=f'{self.cnt+1}')

        while self.ga_rand in temp_ga_list:
            self.ga_rand = random.randint(0, 45)

        if (self.cnt < 20):
            temp_ga_list.append(self.ga_rand)
            self.label1.config(text=f'{gatakana[temp_ga_list[-1]]}')
            temp_que_list.append(gatakana[self.ga_rand])
            self.on_time = True
        else:
            self.entry.delete(0, "end")
            self.label1.config(text=f'Finish')
            self.label4.config(text=f"Acc:{self.sc * 5}%")
            self.button1.config(state='normal')
            self.entry.config(state='disabled')
            self.button4.config(text='Result', state='normal', relief='solid')
            self.total += 1

            for i in temp_worng:
                temp_worng_idx.append(temp_que_list.index(gatakana1[i]))
            worng_idx.append(temp_worng_idx[:])
            temp_worng_idx.clear()

            if (self.cnt == 20):
                ga_rand_list.append(temp_ga_list[:])
                que_list.append(temp_que_list[:])
                my_answer_list.append(temp_my_answer_list[:])
                worng.append(temp_worng[:])
                temp_ga_list.clear()
                temp_que_list.clear()
                temp_my_answer_list.clear()
                temp_worng.clear()

    def switch_to_hiragana(self):
        self.menu = 0
        try:
            if self.hi_rand not in temp_hi_list:
                temp_hi_list.append(temp_ga_list[-1])
                self.trans = 1
        except:
            pass

    def switch_to_gatakana(self):
        self.menu = 1
        try:
            if self.ga_rand not in temp_ga_list:
                temp_ga_list.append(temp_hi_list[-1])
                self.trans = 2
        except:
            pass


jap = Japanese()