[app]

title = Calculator
package.name = calculator
package.domain = org.mehrsam

source.dir = .
source.include_exts = py,png,jpg,kv,wav

icon.filename = %(source.dir)s/icon.png

version = 1.0

requirements = python3,kivy

orientation = portrait

fullscreen = 0


android.api = 35
android.minapi = 23
android.build_tools_version = 35.0.0
android.ndk = 27.3.13750724
android.ndk = 28c
android.archs = arm64-v8a

log_level = 2


[buildozer]

warn_on_root = 1