import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from tkinter.font import Font
import random
from datetime import datetime

class QuizSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("mariwhiskis /creado por riothedog/")
        self.root.geometry("1000x600")
        
        # Configuración de estilo
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Variables de datos
        self.categories = self.load_data('categories.json', [
            {'id': 'default', 'name': 'General', 'description': 'Preguntas generales'}
        ])
        self.questions = self.load_data('questions.json', {})
        self.current_category = 'default'
        
        # Variables de estado
        self.current_quiz_question = 0
        self.quiz_score = 0
        self.quiz_questions = []
        
        # Crear interfaz principal
        self.create_main_interface()
        
    def load_data(self, filename, default_data):
        try:
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return default_data
        except:
            return default_data
            
    def save_data(self):
        with open('categories.json', 'w', encoding='utf-8') as f:
            json.dump(self.categories, f, ensure_ascii=False, indent=2)
        with open('questions.json', 'w', encoding='utf-8') as f:
            json.dump(self.questions, f, ensure_ascii=False, indent=2)
    
    def create_main_interface(self):
        # Barra de navegación
        nav_frame = ttk.Frame(self.root)
        nav_frame.pack(fill='x', padx=10, pady=5)
        
        ttk.Button(nav_frame, text="Administrar", command=self.show_admin).pack(side='left', padx=5)
        ttk.Button(nav_frame, text="Iniciar Quiz", command=self.show_quiz_selection).pack(side='left', padx=5)
        
        # Frame principal
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        self.show_admin()
    
    def show_admin(self):
        self.clear_main_frame()
        
        
        category_frame = ttk.LabelFrame(self.main_frame, text="Categorías")
        category_frame.pack(fill='x', padx=5, pady=5)
        
        
        add_cat_frame = ttk.Frame(category_frame)
        add_cat_frame.pack(fill='x', padx=5, pady=5)
        
        ttk.Label(add_cat_frame, text="Nueva categoría:").pack(side='left', padx=5)
        cat_name = ttk.Entry(add_cat_frame)
        cat_name.pack(side='left', padx=5)
        
        def add_category():
            name = cat_name.get().strip()
            if name:
                cat_id = name.lower().replace(' ', '_')
                self.categories.append({
                    'id': cat_id,
                    'name': name,
                    'description': ''
                })
                self.questions[cat_id] = []
                self.save_data()
                self.update_category_list()
                cat_name.delete(0, 'end')
        
        ttk.Button(add_cat_frame, text="Añadir", command=add_category).pack(side='left', padx=5)
        
        
        self.cat_list_frame = ttk.Frame(category_frame)
        self.cat_list_frame.pack(fill='x', padx=5, pady=5)
        self.update_category_list()
        
        
        question_frame = ttk.LabelFrame(self.main_frame, text="Preguntas")
        question_frame.pack(fill='both', expand=True, padx=5, pady=5)
        
        
        add_q_frame = ttk.Frame(question_frame)
        add_q_frame.pack(fill='x', padx=5, pady=5)
        
        ttk.Label(add_q_frame, text="Pregunta:").grid(row=0, column=0, padx=5, pady=5)
        question_text = ttk.Entry(add_q_frame, width=50)
        question_text.grid(row=0, column=1, columnspan=3, padx=5, pady=5)
        
        answers = []
        for i in range(4):
            ttk.Label(add_q_frame, text=f"Respuesta {i+1}:").grid(row=i+1, column=0, padx=5, pady=2)
            answer = ttk.Entry(add_q_frame, width=40)
            answer.grid(row=i+1, column=1, padx=5, pady=2)
            answers.append(answer)
        
        correct_ans = tk.StringVar(value="0")
        for i in range(4):
            ttk.Radiobutton(add_q_frame, text="Correcta", variable=correct_ans, value=str(i)).grid(row=i+1, column=2, padx=5)
        
        def add_question():
            q_text = question_text.get().strip()
            if not q_text:
                messagebox.showwarning("Error", "La pregunta no puede estar vacía")
                return
                
            ans_list = []
            for i, ans in enumerate(answers):
                text = ans.get().strip()
                if not text:
                    messagebox.showwarning("Error", "Todas las respuestas deben estar completas")
                    return
                ans_list.append({
                    'text': text,
                    'isCorrect': str(i) == correct_ans.get()
                })
            
            if self.current_category not in self.questions:
                self.questions[self.current_category] = []
                
            self.questions[self.current_category].append({
                'question': q_text,
                'answers': ans_list
            })
            
            self.save_data()
            question_text.delete(0, 'end')
            for ans in answers:
                ans.delete(0, 'end')
            self.update_question_list()
            
        ttk.Button(add_q_frame, text="Añadir Pregunta", command=add_question).grid(row=5, column=1, pady=10)
        
        
        self.q_list_frame = ttk.Frame(question_frame)
        self.q_list_frame.pack(fill='both', expand=True, padx=5, pady=5)
        self.update_question_list()
    
    def update_category_list(self):
        for widget in self.cat_list_frame.winfo_children():
            widget.destroy()
            
        for cat in self.categories:
            frame = ttk.Frame(self.cat_list_frame)
            frame.pack(fill='x', pady=2)
            
            ttk.Label(frame, text=cat['name']).pack(side='left', padx=5)
            ttk.Label(frame, text=f"({len(self.questions.get(cat['id'], []))} preguntas)").pack(side='left', padx=5)
            
            if cat['id'] != 'default':
                ttk.Button(frame, text="Eliminar", command=lambda c=cat['id']: self.delete_category(c)).pack(side='right', padx=5)
            
            ttk.Button(frame, text="Seleccionar", command=lambda c=cat['id']: self.select_category(c)).pack(side='right', padx=5)
    
    def update_question_list(self):
        for widget in self.q_list_frame.winfo_children():
            widget.destroy()
            
        questions = self.questions.get(self.current_category, [])
        for i, q in enumerate(questions):
            frame = ttk.Frame(self.q_list_frame)
            frame.pack(fill='x', pady=2)
            
            ttk.Label(frame, text=f"{i+1}. {q['question']}").pack(side='left', padx=5)
            ttk.Button(frame, text="Eliminar", command=lambda idx=i: self.delete_question(idx)).pack(side='right', padx=5)
    
    def delete_category(self, category_id):
        if messagebox.askyesno("Confirmar", "¿Estás seguro de eliminar esta categoría?"):
            self.categories = [c for c in self.categories if c['id'] != category_id]
            self.questions.pop(category_id, None)
            self.save_data()
            self.current_category = 'default'
            self.update_category_list()
            self.update_question_list()
    
    def delete_question(self, index):
        if messagebox.askyesno("Confirmar", "¿Estás seguro de eliminar esta pregunta?"):
            self.questions[self.current_category].pop(index)
            self.save_data()
            self.update_question_list()
    
    def select_category(self, category_id):
        self.current_category = category_id
        self.update_question_list()
    
    def show_quiz_selection(self):
        self.clear_main_frame()
        
        ttk.Label(self.main_frame, text="Selecciona una categoría para iniciar el quiz", font=('Helvetica', 14)).pack(pady=20)
        
        for cat in self.categories:
            if cat['id'] in self.questions and self.questions[cat['id']]:
                frame = ttk.Frame(self.main_frame)
                frame.pack(fill='x', pady=5)
                
                ttk.Label(frame, text=cat['name']).pack(side='left', padx=5)
                ttk.Label(frame, text=f"({len(self.questions[cat['id']])} preguntas)").pack(side='left', padx=5)
                ttk.Button(frame, text="Iniciar Quiz", command=lambda c=cat['id']: self.start_quiz(c)).pack(side='right', padx=5)
    
    def start_quiz(self, category_id):
        self.quiz_questions = self.questions[category_id].copy()
        random.shuffle(self.quiz_questions)
        self.current_quiz_question = 0
        self.quiz_score = 0
        self.show_quiz_question()
    
    def show_quiz_question(self):
        self.clear_main_frame()
        
        if self.current_quiz_question >= len(self.quiz_questions):
            self.show_quiz_results()
            return
        
        question = self.quiz_questions[self.current_quiz_question]
        
        progress = ttk.Progressbar(self.main_frame, length=400, mode='determinate')
        progress['value'] = (self.current_quiz_question / len(self.quiz_questions)) * 100
        progress.pack(pady=20)
        
        ttk.Label(self.main_frame, text=f"Pregunta {self.current_quiz_question + 1} de {len(self.quiz_questions)}", 
                 font=('Helvetica', 12)).pack(pady=5)
        
        ttk.Label(self.main_frame, text=question['question'], 
                 font=('Helvetica', 14, 'bold')).pack(pady=20)
        
        answers = question['answers'].copy()
        random.shuffle(answers)
        
        for answer in answers:
            btn = ttk.Button(self.main_frame, text=answer['text'], 
                           command=lambda a=answer: self.check_answer(a))
            btn.pack(fill='x', padx=50, pady=5)
    
    def check_answer(self, answer):
        if answer['isCorrect']:
            self.quiz_score += 1
        
        self.current_quiz_question += 1
        self.show_quiz_question()
    
    def show_quiz_results(self):
        self.clear_main_frame()
        
        percentage = (self.quiz_score / len(self.quiz_questions)) * 100
        
        ttk.Label(self.main_frame, text="¡Quiz completado!", 
                 font=('Helvetica', 16, 'bold')).pack(pady=20)
        
        ttk.Label(self.main_frame, text=f"Puntuación: {self.quiz_score} de {len(self.quiz_questions)}", 
                 font=('Helvetica', 14)).pack(pady=10)
        
        ttk.Label(self.main_frame, text=f"Porcentaje: {percentage:.1f}%", 
                 font=('Helvetica', 14)).pack(pady=10)
        
        ttk.Button(self.main_frame, text="Volver al inicio", 
                  command=self.show_admin).pack(pady=20)
    
    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    app = QuizSystem(root)
    root.mainloop()