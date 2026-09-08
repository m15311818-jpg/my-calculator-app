import numpy as np
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class ScientificCalculatorApp(App):

    def build(self):
        self.operators = ['/', '*', '+', '-']
        self.last_was_operator = None
        self.last_button = None

        # التنسيق الرئيسي
        main_layout = BoxLayout(
            orientation='vertical', padding=10, spacing=10
        )

        # شاشة العرض
        self.solution = TextInput(
            multiline=False, readonly=True, halign='right', font_size=45
        )
        main_layout.add_widget(self.solution)

        # زر الكاميرا الذكي (تمهيداً للمرحلة الثانية)
        camera_btn = Button(
            text='تصوير المسألة والحل بالذكاء الاصطناعي 📸',
            font_size=20,
            background_color=(0.1, 0.6, 0.9, 1),
            size_hint_y=0.15,
        )
        camera_btn.bind(on_press=self.open_camera_ai)
        main_layout.add_widget(camera_btn)

        # أزرار الآلة الحاسبة العلمية
        buttons = [
            ['sin', 'cos', 'tan', '^'],
            ['sqrt', 'log', '(', ')'],
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '0', 'C', '+'],
        ]

        # بناء واجهة الأزرار
        for row in buttons:
            h_layout = BoxLayout(spacing=5, size_hint_y=0.12)
            for label in row:
                # تلوين الأزرار العلمية بلون مختلف
                if label in [
                    'sin',
                    'cos',
                    'tan',
                    '^',
                    'sqrt',
                    'log',
                    '(',
                    ')',
                ]:
                    btn_color = (0.3, 0.3, 0.3, 1)
                elif label in self.operators or label == 'C':
                    btn_color = (0.8, 0.4, 0.1, 1)
                else:
                    btn_color = (0.2, 0.2, 0.2, 1)

                button = Button(
                    text=label, font_size=24, background_color=btn_color
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        # زر اليساوي
        equals_button = Button(
            text='=',
            font_size=28,
            background_color=(0.2, 0.6, 0.2, 1),
            size_hint_y=0.12,
        )
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)

        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == 'C':
            self.solution.text = ''
        elif button_text in ['sin', 'cos', 'tan', 'sqrt', 'log']:
            self.solution.text = current + button_text + '('
        else:
            self.solution.text = current + button_text

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            try:
                # تحويل الرموز النصية إلى دوال يفهمها نظام numpy الرياضي الرهيب
                expr = text.replace('^', '**')
                expr = expr.replace('sin', 'np.sin')
                expr = expr.replace('cos', 'np.cos')
                expr = expr.replace('tan', 'np.tan')
                expr = expr.replace('sqrt', 'np.sqrt')
                expr = expr.replace('log', 'np.log10')

                # حساب الناتج
                result = eval(expr, {'np': np})
                self.solution.text = str(round(result, 6))
            except Exception:
                self.solution.text = 'Error'

    # دالة زر الكاميرا (تمهيد ميزة تصوير المسائل)
    def open_camera_ai(self, instance):
        self.solution.text = 'جاري فتح الكاميرا للمحاكاة...'
        # هنا هنحط كود استدعاء كاميرا الأندرويد والربط بسيرفر الذكاء الاصطناعي


if __name__ == '__main__':
    ScientificCalculatorApp().run()
