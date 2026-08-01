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

android.ndk = 28c

android.archs = arm64-v8a, armeabi-v7a

android.permissions =


log_level = 2


[buildozer]

warn_on_root = 1