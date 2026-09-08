[app]
title = My Calculator
package.name = mycalculator
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg
version = 0.1

# 💡 تم تعديل المتطلبات لنسخة مجربة ومستقرة بدون تضارب
requirements = python3,kivy

# 🛡️ إعدادات التوافق القياسية
android.api = 33
android.minapi = 21
android.ndk_path = 
android.sdk_path = 
android.private_storage = True

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a
android.allow_backup = True
