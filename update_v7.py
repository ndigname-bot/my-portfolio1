import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Update Footer to Brittany Chiang style with SVG icons
footer_old_pattern = re.compile(r'<footer.*?</footer>', re.DOTALL)

footer_new = """
    <!-- Brittany Chiang Style Fixed Socials (Desktop) -->
    <div class="hidden md:flex flex-col fixed left-10 bottom-0 z-50 space-y-6 items-center social-bar-animate">
        <a href="https://github.com/ndigname-bot" target="_blank" class="text-gray-400 hover:text-blue-400 hover:-translate-y-2 transition-all duration-300">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
        </a>
        <a href="https://gh.linkedin.com/in/emmanuel-ndignam-4b17113b1" target="_blank" class="text-gray-400 hover:text-blue-400 hover:-translate-y-2 transition-all duration-300">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>
        </a>
        <a href="https://x.com/ndiganam" target="_blank" class="text-gray-400 hover:text-blue-400 hover:-translate-y-2 transition-all duration-300">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4l11.733 16h4.267l-11.733 -16z"/><path d="M4 20l6.768 -6.768m2.46 -2.46l6.772 -6.772"/></svg>
        </a>
        <div class="w-px h-24 bg-gray-400"></div>
    </div>

    <!-- Fixed Right Side Email (Brittany Style) -->
    <div class="hidden md:flex flex-col fixed right-10 bottom-0 z-50 items-center space-y-6 social-bar-animate">
        <a href="mailto:ndigname@gmail.com" class="text-gray-400 hover:text-blue-400 tracking-widest font-mono text-sm" style="writing-mode: vertical-rl; transform: translateY(-10px);">
            ndigname@gmail.com
        </a>
        <div class="w-px h-24 bg-gray-400"></div>
    </div>

    <!-- Mobile Footer -->
    <footer class="bg-gray-800 text-gray-400 py-8 text-center font-mono text-sm border-t border-gray-700">
        <div class="flex md:hidden justify-center space-x-8 mb-6">
            <a href="https://github.com/ndigname-bot" target="_blank" class="hover:text-blue-400 transition-colors"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg></a>
            <a href="https://gh.linkedin.com/in/emmanuel-ndignam-4b17113b1" target="_blank" class="hover:text-blue-400 transition-colors"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg></a>
            <a href="https://x.com/ndiganam" target="_blank" class="hover:text-blue-400 transition-colors"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4l11.733 16h4.267l-11.733 -16z"/><path d="M4 20l6.768 -6.768m2.46 -2.46l6.772 -6.772"/></svg></a>
        </div>
        <a href="https://github.com/ndigname-bot/my-portfolio1" target="_blank" class="hover:text-blue-400 transition-colors duration-300">
            <p>Designed & Built by Emmanuel Ndignam</p>
        </a>
    </footer>
"""
content = footer_old_pattern.sub(footer_new, content)

with open('index.html', 'w') as f:
    f.write(content)
