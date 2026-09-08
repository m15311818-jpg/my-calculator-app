import math
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class ProScientificCalculatorApp(App):

    def build(self):
        self.operators = ['/', '*', '+', '-']

        # التنسيق الرئيسي (رأسي)
        main_layout = BoxLayout(
            orientation='vertical', padding=10, spacing=10
        )

        # شاشة عرض العمليات والنتائج
        self.solution = TextInput(
            multiline=False, readonly=True, halign='right', font_size=45
        )
        main_layout.add_widget(self.solution)

        # الأزرار العلمية والمتقدمة المرتبة
        buttons = [
            ['π', 'e', 'log', '^'],
            ['sin', 'cos', 'tan', 'sqrt'],
            ['(', ')', 'C', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['.', '0', 'DEL', '='],
        ]

        # بناء واجهة الأزرار وتلوينها
        for row in buttons:
            h_layout = BoxLayout(spacing=5)
            for label in row:
                if label in [
                    'sin',
                    'cos',
                    'tan',
                    'sqrt',
                    'log',
                    '^',
                    'π',
                    'e',
                    '(',
                    ')',
                ]:
                    btn_color = (0.25, 0.25, 0.3, 1)  # أزرار علمية
                elif label in self.operators or label in ['C', 'DEL']:
                    btn_color = (0.85, 0.45, 0.1, 1)  # أزرار مسح وتحكم
                elif label == '=':
                    btn_color = (0.15, 0.65, 0.25, 1)  # يساوي
                else:
                    btn_color = (0.2, 0.2, 0.2, 1)  # الأرقام

                button = Button(
                    text=label, font_size=24, background_color=btn_color
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == 'C':
            self.solution.text = ''
        elif button_text == 'DEL':
            self.solution.text = current[:-1]
        elif button_text in ['sin', 'cos', 'tan', 'sqrt', 'log']:
            self.solution.text = current + button_text + '('
        elif button_text == '=':
            self.on_solution()
        else:
            self.solution.text = current + button_text

    def on_solution(self):
        text = self.solution.text
        if text:
            try:
                # تحويل الحروف النصية إلى دوال يفهمها نظام بايثون الرياضي المدمج
                expr = text.replace('^', '**')
                expr = expr.replace('π', 'math.pi')
                expr = expr.replace('e', 'math.e')
                expr = expr.replace('sin', 'math.sin')
                expr = expr.replace('cos', 'math.cos')
                expr = expr.replace('tan', 'math.tan')
                expr = expr.replace('sqrt', 'math.sqrt')
                expr = expr.replace('log', 'math.log10')

                # حساب المعادلة بأمان باستخدام مكتبة math
                result = eval(expr, {'math': math})
                self.solution.text = str(round(result, 6))
            except Exception:
                self.solution.text = 'Error'


if __name__ == '__main__':
    ProScientificCalculatorApp().run()
