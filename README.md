## 🛡️ **Pouncer**

A small Windows utility that fakes a Blue Screen of Death at startup as a privacy buffer.
Originally built out of pure desperation during a family conflict, now shared in case someone finds it genuinely useful (responsibly, of course).

### ✨ What it does

Pouncer launches automatically at system startup and displays a **fake BSOD screen** to prevent immediate access to the desktop.

* Looks like a real Windows blue screen
* Press **Alt + F4** to dismiss it and load normally
* If Alt + F4 *isn’t* pressed within the configured timeout, it triggers a **real system crash / forced BSOD**
* Designed as a lightweight “digital door lock” when you’re unable to use a real login password

### 🧠 Why it exists

My stepmom forced me to remove my Windows password so she could randomly inspect my computer.
I didn’t want to fight about it, so together with my dad we threw together a fake-BSOD startup blocker so I could keep some basic privacy.

It solved the problem surprisingly well, so I’m releasing it here in case someone finds themselves in a similar situation.

### 🚀 How to run

#### Recommended (easy)

Download the compiled `Bouncer.exe` from `dist/` and add it to:

```
shell:startup
```

This runs it automatically at login.

#### Developers

```bash
python Bouncer.py
```

Requires pillow / pyinstaller if you want to rebuild.

### ⚠️ Disclaimer

This tool was created for **personal privacy and peaceful conflict avoidance** — not malicious use.

Please don’t use it to:

* Hide illegal activity
* Lock people out of devices they rightfully control
* Bypass organizational or school security policies

Use responsibly, ethically, and with consent.

---

## 📜 License

Probably MIT, but also: **don’t be a jerk with it.**

## 🤝 Contributions

Bug fixes and improvements welcome. PRs, docs, and creative suggestions appreciated.

---
