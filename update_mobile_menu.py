import re
with open('index.html', 'r') as f:
    content = f.read()

# Current mobile menu
# <div id="mobile-menu" class="hidden md:hidden bg-gray-800 border-t border-gray-700">
# Let's change the classes to make it a fixed sidebar that transforms.
new_menu_classes = 'class="fixed inset-y-0 right-0 z-40 w-64 glass-menu shadow-2xl transform translate-x-full transition-transform duration-300 ease-in-out md:hidden flex flex-col pt-20 border-l border-gray-700"'

# In script.js it toggles 'hidden'. So currently if it has 'hidden' it will be completely hidden.
# If we want a slide out, we shouldn't toggle 'hidden', we should toggle 'translate-x-full' vs 'translate-x-0'.
# But since script.js toggles 'hidden', I'll just change the script.js logic too.

# Replace HTML classes
content = content.replace('<div id="mobile-menu" class="hidden md:hidden bg-gray-800 border-t border-gray-700">',
                          f'<div id="mobile-menu" {new_menu_classes}>')

with open('index.html', 'w') as f:
    f.write(content)
