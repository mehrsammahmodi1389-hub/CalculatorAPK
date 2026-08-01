[app]

title = Calculator

package.name = calculator
package.domain = org.mehrsam

source.dir = .

source.include_exts = py,png,jpg,kv,wav

icon.filename = %(source.dir)s/icon.png

version = 1.0

requirements = python3==3.11,kivy

orientation = portrait

fullscreen = 0


# Android

android.api = 35
android.minapi = 23

android.archs = arm64-v8a, armeabi-v7a

android.ndk = 28.0.13004108

android.accept_sdk_license = True


[buildozer]

log_level = 2

warn_on_root = 1