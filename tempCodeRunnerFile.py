
        if self.sidebar_visible:
            self.sidebar_frame.pack_forget()
            self.courses_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=20)
        else:
            self.sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)
            self.courses_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        self.sidebar_visible = not self.sidebar_visible
    
    def create_course_cards(self, parent, courses):
        self.course_cards = []
        
        for i, course in enumerate(courses):
            card = tk.Frame(parent, bg='goldenrod2', bd=2, relief=tk.RAISED, width=400)
            card.grid(row=i//2, column=i%2, padx=10, pady=10, sticky="nsew")
            
            title_label = tk.Label(card, text=course[1], bg='goldenrod2', font=('Arial', 14, 'bold'))
            title_label.pack(pady=5)
            
            teacher_label = tk.Label(card, text=f"Teacher: {course[2]}", bg='goldenrod2', font=('Arial', 10))
            teacher_label.pack(pady=5)
            
            open_btn = tk.Button(card, text="Get Started", font=('Arial', 12), bg='blue', fg='white', padx=10, pady=5, command=lambda c=course: self.open_course(c))
            open_btn.pack(pady=5)
            
            self.course_cards.append(card)
        
        for i in range(len(courses)//2 + len(courses)%2):
            self.courses_frame.grid_rowconfigure(i, weight=1)
        for i in range(2):  # Assume a max of 2 columns for simplicity
            self.courses_frame.grid_columnconfigure(i, weight=1)
    
    def on_resize(self, event):
        width = self.courses_frame.winfo_width()
        if width < 200:
            columns = 1
        elif width < 800:
            columns = 2
        else:
            columns = 3
        
        for index, card in enumerate(self.course_cards):
            card.grid_forget()
            card.grid(row=index//columns, column=index%columns, padx=10, pady=10, sticky="nsew")
        
        for i in range(len(self.course_cards)//columns + len(self.course_cards)%columns):
            self.courses_frame.grid_rowconfigure(i, weight=1)
        for i in range(columns):
            self.courses_frame.grid_columnconfigure(i, weight=1)