[app]
title = Pro Scientific Calculator
package.name = procalculator
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg
version = 2.0

# 💡Requirements: أضفنا numpy فقط للعمليات الرياضية المعقدة
requirements = python3,kivy

# 🛡️ إعدادات التوافقية الشاملة لجميع الهواتف
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.private_storage = True

orientation = portrait
fullscreen = 0
android.allow_backup = True
