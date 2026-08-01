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

android.ndk = 27.2.12479018
android.archs = arm64-v8a


android.accept_sdk_license = True


log_level = 2



[buildozer]

warn_on_root = 1