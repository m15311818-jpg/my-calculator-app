[app]
title = My Calculator
package.name = mycalculator
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg
version = 0.1
requirements = python3,kivy

# 🛡️ إعدادات التوافق مع إصدارات أندرويد لعام 2026
android.api = 34
android.minapi = 21
android.ndk = 25b
android.private_storage = True

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
