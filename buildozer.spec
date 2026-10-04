[app]

title = Risk Management Calculator
package.name = riskcalculator
package.domain = org.spades

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas

version = 1.0

requirements = python3,kivy

orientation = portrait

fullscreen = 0


[buildozer]

log_level = 2
warn_on_root = 1


[android]

android.api = 33
android.minapi = 24

android.archs = arm64-v8a

android.accept_sdk_license = True
