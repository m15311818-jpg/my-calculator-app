from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None
        
        # التنسيق الرئيسي للتطبيق (رأسي)
        main_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        
        # شاشة عرض الأرقام والنتائج
        self.solution = TextInput(
            multiline=False, readonly=True, halign="right", font_size=55
        )
        main_layout.add_widget(self.solution)
        
        # ترتيب الأزرار على شكل آلة حاسبة
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"]
        ]
        
        # بناء الأزرار وإضافتها للواجهة
        for row in buttons:
            h_layout = BoxLayout(spacing=5)
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                    font_size=30
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
        
        # زر اليساوي (يأخذ مساحة أفقية كاملة في الأسفل)
        equals_button = Button(
            text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}, font_size=30
        )
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)
        
        return main_layout

    # دالة التعامل مع ضغطات الأزرار
    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text
        
        if button_text == "C":
            # مسح الشاشة
            self.solution.text = ""
        else:
            if current and (self.last_was_operator and button_text in self.operators):
                # منع كتابة علامتين ورا بعض (مثلا ++ أو //)
                return
            elif current == "" and button_text in self.operators:
                # منع البدء بعلامة رياضية
                return
            else:
                self.solution.text = current + button_text
        
        self.last_button = instance
        self.last_was_operator = button_text in self.operators

    # دالة حساب النتيجة عند الضغط على =
    def on_solution(self, instance):
        text = self.solution.text
        if text:
            try:
                # دالة eval تحسب المعادلة المكتوبة في النص تلقائياً
                self.solution.text = str(eval(text))
            except Exception:
                self.solution.text = "Error"

if __name__ == "__main__":
    CalculatorApp().run()
