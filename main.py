from ultralytics import YOLO
import cv2
from tkinter import Tk, Button, Label, filedialog, Frame
from PIL import Image, ImageTk

class YOLOGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ĐỒ ÁN CUỐI KÌ - COMPUTER VISION")
        self.root.geometry("950x550")  # rộng hơn để đủ chỗ 2 ảnh bên cạnh
        self.root.configure(bg="#1a1a2e")

        self.model = YOLO("D:\\TAI_LIEU_DH\\TONGHOPKIENTHUC\\CV\\best.pt")

        title_text = "ĐỒ ÁN CUỐI KÌ\nCOMPUTER VISION"
        info_text = "GV: Võ Quang Hoàng Khang\nNguyễn Thị Hồng Thắm\nNguyễn Chiêu Văn"
        self.lbl_title = Label(root, text=title_text, font=("Arial", 24, "bold"), fg="white", bg="#1a1a2e")
        self.lbl_title.pack(pady=(8,2))
        self.lbl_info = Label(root, text=info_text, font=("Arial", 16), fg="white", bg="#1a1a2e", justify="center")
        self.lbl_info.pack(pady=(0,12))

        self.frame_buttons = Frame(root, bg="#1a1a2e")
        self.frame_buttons.pack(pady=8)

        self.btn_select = Button(self.frame_buttons, text="Chọn ảnh", bg="green", fg="white", width=14, height=2, font=("Arial", 16), command=self.select_image)
        self.btn_select.pack(side="left", padx=10)

        self.btn_detect = Button(self.frame_buttons, text="Nhận diện", bg="red", fg="white", width=14, height=2, font=("Arial", 16), command=self.detect_image)
        self.btn_detect.pack(side="left", padx=10)

        # Frame chứa 2 cột: Input và Output
        self.frame_images = Frame(root, bg="#1a1a2e")
        self.frame_images.pack(padx=15, pady=15)

        # Cột Input
        self.frame_input = Frame(self.frame_images, bg="#1a1a2e")
        self.frame_input.pack(side="left", padx=15)
        self.lbl_input_text = Label(self.frame_input, text="Input", font=("Arial", 20), fg="white", bg="#1a1a2e", anchor="center")
        self.lbl_input_text.pack(pady=(0,5))
        self.lbl_original = Label(self.frame_input, bg="black", width=440, height=440)
        self.lbl_original.pack()

        # Cột Output
        self.frame_output = Frame(self.frame_images, bg="#1a1a2e")
        self.frame_output.pack(side="left", padx=15)
        self.lbl_output_text = Label(self.frame_output, text="Output", font=("Arial", 20), fg="white", bg="#1a1a2e", anchor="center")
        self.lbl_output_text.pack(pady=(0,5))
        self.lbl_result = Label(self.frame_output, bg="black", width=440, height=440)
        self.lbl_result.pack()

        self.img_path = None
        self.img_original = None

    def select_image(self):
        file_path = filedialog.askopenfilename(
            title="Chọn ảnh để nhận dạng",
            filetypes=[("Image Files", "*.jpg;*.png;*.jpeg")]
        )
        if not file_path:
            return

        self.img_path = file_path
        self.img_original = Image.open(file_path)
        self.img_original = self.img_original.resize((440, 440))
        img_tk = ImageTk.PhotoImage(self.img_original)

        self.lbl_original.config(image=img_tk)
        self.lbl_original.image = img_tk

        self.lbl_result.config(image='', text='')

    def detect_image(self):
        if not self.img_path:
            self.lbl_result.config(text="Vui lòng chọn ảnh trước", fg="red", font=("Arial", 16))
            return

        results = self.model(self.img_path)

        for result in results:
            img_with_boxes = result.plot()
            img_rgb = cv2.cvtColor(img_with_boxes, cv2.COLOR_BGR2RGB)
            img_pil = Image.fromarray(img_rgb)
            img_pil = img_pil.resize((440, 440))
            img_tk_result = ImageTk.PhotoImage(img_pil)

            self.lbl_result.config(image=img_tk_result)
            self.lbl_result.image = img_tk_result
            self.lbl_result.text = ""

if __name__ == "__main__":
    root = Tk()
    app = YOLOGUI(root)
    root.mainloop()
