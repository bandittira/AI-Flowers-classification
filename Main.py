from myclass import *
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import numpy as np

#Image flowers classification
#ภาคภูมิ ผลไพบูลย 1620706174
#อธิคุณ รัตนพฤกษาชาติ 1620706158
#บัณทิต ถิระเสถียร 1620707743

labels_name = ['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']

def classify(file_path):
    img = Image.open(file_path)
    path=os.path.join(file_path)
    print(path)
    new_array = cv2.imread(path)
    img_rgb = cv2.cvtColor(new_array, cv2.COLOR_BGR2RGB)
    im2 = cv2.resize(img_rgb, (64, 64))
    im3 = np.expand_dims(im2, axis=0)
    im3 = np.array(im3)
    pred = model.predict_classes([(im3)])
    sign = labels_name[pred[0]]
    print("Class: ",sign)
    actual = path.split('/')
    print(actual)
    label.configure(foreground='#011638', text=('Predicted: '+ labels_name[(pred[0])]))

    test = label2.configure(foreground='#011638', text=('ถ้าคำตอบของเราถูกต้อง ข้อมูลดอกไม้ที่คุณต้องการ มีดังนี้ครับ'))
    
    if labels_name[(pred[0])] == "daisy":
        labeltext = "daisy มีความหมายถึง ความสวยงาม ความบริสุทธิ์ไร้เดียงสา ความอดทน ความหวัง สื่อถึงความรักที่ซื่อสัตย์ และยังเป็นตัวแทนมอบเป็นสัญลักษณ์แทนความรัก"
    elif labels_name[(pred[0])] == "dandelion":
        labeltext = "dandelion สื่อความหมายถึง ความร่าเริง ความสุข และมีความหวัง"
    elif labels_name[(pred[0])] == "rose":
        labeltext = "rose สื่อความหมายถึง ความรักอันลึกซึ้ง ความรักอันบริสุทธิ์ใจไม่ต้องการสิ่งตอบแทน ความรักแบบโรแมนติกและความเสน่หาต่อกัน"
    elif labels_name[(pred[0])] == "sunflower":
        labeltext = "sunflower ความหมาย คือ ดอกทานตะวันนั้นเองดอกทานตะวันเป็นสัญลักษณ์ของความเชื่อมั่น ความมั่นคง รักเดียว ใจเดียว และมีนัยถึงศิลปะที่งดงาม"
    elif labels_name[(pred[0])] == "tulip":
        labeltext = "tulipคือสัญลักษณ์ของความรักและความโรแมกติก และมีความหมายถึง ความรักที่สมบูรณ์แบบ ความอุดมสมบูรณ์ ความหลงใหล ความซื่อสัตย์ การขอโทษ การเริ่มต้นสิ่งใหม่"
    else:
        labeltext = ""
    
    meaning_label.configure(foreground='#011638', text=(labeltext))

def show_classify_button(file_path):
    classify_b=Button(root,text="Classify Image",command=lambda: classify(file_path),padx=10,pady=5)
    classify_b.configure(background='#364156', foreground='white',font=('arial',10,'bold'))
    classify_b.place(relx=0.79,rely=0.46)

def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        print(file_path)
        uploaded.thumbnail(((root.winfo_width()/2.25),(root.winfo_height()/2.25)))
        image=ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=image)
        sign_image.image=image
        sign_image.pack(pady = 50)
        label.configure(text='')
        show_classify_button(file_path)
        labeltext = ""
        label.configure(foreground='#011638', text=(labeltext))
        meaning_label.configure(foreground='#011638', text=(labeltext))
        label2.configure(foreground='#011638', text=(labeltext))
    except:
        pass

def center_screen():
	""" gets the coordinates of the center of the screen """
	global screen_height, screen_width, x_cordinate, y_cordinate

	screen_width = root.winfo_screenwidth()
	screen_height = root.winfo_screenheight()
	x_cordinate = int((screen_width/2) - (window_width/2))
	y_cordinate = int((screen_height/2) - (window_height/2))
	root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

if __name__ == '__main__':
    root = tk.Tk()
    root.attributes("-topmost", True)
    window_width = 1200
    window_height = 800
    center_screen()
    root.title('Flower Image Classification')
    root.configure(background='#CDCDCD')
    label=Label(root,background='#CDCDCD', font=('arial',15,'bold'))
    label2=Label(root,background='#CDCDCD', font=('arial',13,'bold'))
    meaning_label = Label(root,background='#CDCDCD', font=('arial',13))
    heading = Label(root, text="Flower Image Prediction",pady=20, font=('arial',20,'bold'))
    heading.configure(background='#CDCDCD',foreground='#364156')
    heading.pack()
    sign_image = Label(root)

    upload=Button(root,text="Upload an image",command=upload_image,padx=10,pady=5)
    upload.configure(background='#364156', foreground='white',font=('arial',10,'bold'))
    upload.pack(side=BOTTOM,pady=50)
    meaning_label.pack(side=BOTTOM,expand=True)
    label2.pack(side=BOTTOM,expand=True)
    label.pack(side=BOTTOM,expand=True)

    root.mainloop()