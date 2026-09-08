[app]
title = AI Scientific Calculator
package.name = aicalculator
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg
version = 1.0

# 🛡️ المكتبات المطلوبة: أضفنا numpy للعمليات الرهيبة، ومكتبات الكاميرا والـ requests للذكاء الاصطناعي
requirements = python3,kivy,numpy,requests

# 📸 إضافة الأذونات الرسمية لفتح الكاميرا وقراءة الملفات على أندرويد
android.permissions = CAMERA, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, INTERNET

# 🛡️ إعدادات التوافق القياسية لتعمل على كل الأجهزة (32-bit & 64-bit)
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.private_storage = True

orientation = portrait
fullscreen = 0
android.allow_backup = True
