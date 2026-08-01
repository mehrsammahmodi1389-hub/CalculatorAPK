[app]

# App information
title = Calculator
package.name = calculator
package.domain = org.mehrsam

# Source
source.dir = .
source.include_exts = py,png,jpg,kv,wav

# Version
version = 1.0

# Requirements
requirements = python3,kivy

# Orientation
orientation = portrait

# Entry point
fullscreen = 0

# Android
android.api = 35
android.minapi = 23
android.build_tools_version = 35.0.0
android.archs = arm64-v8a, armeabi-v7a
android.permissions =
# Logging
log_level = 2

[buildozer]

warn_on_root = 1