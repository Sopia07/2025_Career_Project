import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import time

# 실험 단계 데이터 정의 (각 단계는 제목, 설명, 이미지 파일 경로, 지연시간, 그리고 주의사항을 포함)
steps = [
    {
        "title": "Step 1: 입안 헹굼",
        "description": "적당량의 증류수로 입안을 강하게 헹궈 입안 상피세포 추출액을 만듭니다.",
        "image": "images/rinse_mouth.jpg",
        "delay": 1,  # 시뮬레이션 상의 딜레이 (실제 시간보다 짧게 설정)
        "note": "입안 상피세포를 모을 때 되도록 강하고 오래 헹구세요."
    },
    {
        "title": "Step 2: 첫 번째 원심분리",
        "description": "입안 상피세포 추출액 1.5mL를 마이크로 튜브에 옮긴 후, 13000rpm으로 1분간 원심분리합니다.\n(원심분리 중 …)",
        "image": "images/centrifugation1.jpg",
        "delay": 2,
        "note": ""
    },
    {
        "title": "Step 3: 상층액 제거 및 재충전 원심분리",
        "description": "원심분리 후 상층액을 버리고, 마이크로 튜브에 입안 상피세포 추출액을 꽉 채워 다시 원심분리합니다.",
        "image": "images/centrifugation2.jpg",
        "delay": 1,
        "note": ""
    },
    {
        "title": "Step 4: 세포 추출",
        "description": "두 번째 원심분리 후 상층액을 제거하여 세포를 얻습니다.",
        "image": "images/cell_extraction.jpg",
        "delay": 1,
        "note": ""
    },
    {
        "title": "Step 5: 소금-세제액 준비 및 혼합",
        "description": "소금 2g, 주방용 세제 7mL, 증류수 150mL를 섞어 소금-세제액을 만든 후, 입안 상피세포가 들어있는 튜브에 0.5mL를 넣고 잘 섞습니다.",
        "image": "images/salt_detergent_mix.jpg",
        "delay": 1,
        "note": ""
    },
    {
        "title": "Step 6: 세 번째 원심분리",
        "description": "12500rpm으로 10분 동안 원심분리합니다.",
        "image": "images/centrifugation3.jpg",
        "delay": 2,
        "note": ""
    },
    {
        "title": "Step 7: 에탄올 추가",
        "description": "마이크로 튜브의 상층액에 차가운 95% 에탄올 0.5mL를 벽을 따라 천천히 흘려 에탄올 층을 만듭니다.",
        "image": "images/ethanol_layer.jpg",
        "delay": 1,
        "note": "에탄올은 실험 하루 전 냉장 보관하고, 벽을 따라 천천히 흘려 넣어야 합니다."
    },
    {
        "title": "Step 8: DNA 관찰",
        "description": "세포 추출액과 에탄올 층의 경계에서 실 모양의 DNA가 나타나 덩어리로 뭉치는 현상을 관찰합니다.",
        "image": "images/dna_thread.jpg",
        "delay": 1,
        "note": ""
    }
]

# Tkinter를 활용하여 시뮬레이션 GUI 클래스 생성
class DNASimulation:
    def __init__(self, master):
        self.master = master
        self.master.title("DNA 추출 실험 시뮬레이션")
        self.master.geometry("800x600")
        
        # 현재 단계 인덱스 초기화
        self.current_step = 0
        
        # 이미지 레이블과 텍스트 출력 레이블 생성
        self.title_label = tk.Label(master, text="", font=("Helvetica", 18, "bold"))
        self.title_label.pack(pady=10)
        
        self.desc_label = tk.Label(master, text="", font=("Helvetica", 14), wraplength=750, justify="left")
        self.desc_label.pack(pady=10)
        
        self.image_label = tk.Label(master)
        self.image_label.pack(pady=10)
        
        # 버튼 프레임 생성
        btn_frame = tk.Frame(master)
        btn_frame.pack(side="bottom", pady=20)
        
        self.prev_button = tk.Button(btn_frame, text="이전", command=self.prev_step, width=10)
        self.prev_button.grid(row=0, column=0, padx=10)
        
        self.info_button = tk.Button(btn_frame, text="정보 보기", command=self.show_info, width=10)
        self.info_button.grid(row=0, column=1, padx=10)
        
        self.next_button = tk.Button(btn_frame, text="다음", command=self.next_step, width=10)
        self.next_button.grid(row=0, column=2, padx=10)
        
        self.restart_button = tk.Button(btn_frame, text="재시작", command=self.restart, width=10)
        self.restart_button.grid(row=0, column=3, padx=10)
        
        # 첫 번째 단계 로드
        self.load_step()

    # 현재 단계를 화면에 표시하는 함수
    def load_step(self):
        step = steps[self.current_step]
        self.title_label.config(text=step["title"])
        self.desc_label.config(text=step["description"])
        
        # 이미지 로딩 (이미지 파일이 없으면 기본 텍스트 출력)
        try:
            img = Image.open(step["image"])
            img = img.resize((400, 300), Image.ANTIALIAS)  # 이미지 크기 조정
            self.photo = ImageTk.PhotoImage(img)
            self.image_label.config(image=self.photo, text="")
        except Exception as e:
            self.image_label.config(text="이미지를 불러올 수 없습니다.", image="")
        
        # 시뮬레이션 딜레이 (단계에 따라 지연 후 다음 동작을 실행)
        self.master.update()
        time.sleep(step["delay"])
    
    # 다음 단계로 이동하는 함수
    def next_step(self):
        if self.current_step < len(steps) - 1:
            self.current_step += 1
            self.load_step()
        else:
            messagebox.showinfo("완료", "실험 시뮬레이션이 완료되었습니다.")
    
    # 이전 단계로 이동하는 함수
    def prev_step(self):
        if self.current_step > 0:
            self.current_step -= 1
            self.load_step()
        else:
            messagebox.showwarning("주의", "첫 번째 단계입니다.")
    
    # 추가 정보(주의사항) 표시 함수
    def show_info(self):
        step = steps[self.current_step]
        note = step.get("note", "")
        if note:
            messagebox.showinfo("주의사항", note)
        else:
            messagebox.showinfo("주의사항", "추가 주의사항이 없습니다.")
    
    # 프로그램을 처음부터 재시작하는 함수
    def restart(self):
        self.current_step = 0
        self.load_step()

# 메인 프로그램 실행
if __name__ == "__main__":
    root = tk.Tk()
    app = DNASimulation(root)
    root.mainloop()
