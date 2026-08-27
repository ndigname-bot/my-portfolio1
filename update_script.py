with open('script.js', 'r') as f:
    content = f.read()

# Replace mobile menu toggle logic
old_toggle = """        mobileMenu.classList.toggle('hidden');"""
new_toggle = """        mobileMenu.classList.toggle('translate-x-full');
        mobileMenu.classList.toggle('translate-x-0');"""
content = content.replace(old_toggle, new_toggle)

old_close = """            mobileMenu.classList.add('hidden');"""
new_close = """            mobileMenu.classList.add('translate-x-full');
            mobileMenu.classList.remove('translate-x-0');"""
content = content.replace(old_close, new_close)

with open('script.js', 'w') as f:
    f.write(content)
