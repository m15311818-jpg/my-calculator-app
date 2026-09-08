[app]
title = My Calculator
package.name = mycalculator
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg
version = 0.1
requirements = python3,kivy==2.3.0

# 🛡️ الإعدادات الذهبية للتوافقية والاستقرار
android.api = 33
android.minapi = 21
android.ndk = 25b
android.private_storage = True

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
