import re

with open('index.html', 'r') as f:
    content = f.read()

contact_pattern = re.compile(r'<section id="contact".*?</section>', re.DOTALL)
new_contact = """
<section id="contact" class="py-24 bg-gray-900 relative z-20">
    <div class="container mx-auto px-4 max-w-2xl" data-aos="fade-up">
        <div class="text-center mb-12">
            <h2 class="text-4xl md:text-5xl font-bold text-gray-100 mb-4 glow-text-subtle">Get In <span class="text-blue-400">Touch</span></h2>
            <p class="text-gray-400 text-lg">Whether you have a question or just want to say hi, my inbox is always open. Let's build something secure together.</p>
        </div>
        
        <div class="bg-gray-800/60 backdrop-blur-md p-8 md:p-10 rounded-2xl shadow-2xl border border-gray-700 relative overflow-hidden group">
            <!-- Decorative Cyber Line -->
            <div class="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-blue-500 via-purple-500 to-blue-500 opacity-75 group-hover:opacity-100 transition-opacity duration-500"></div>
            
            <form action="https://formspree.io/f/mdalbrll" method="POST" class="space-y-6 relative z-10">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div>
                        <label class="block text-sm font-medium text-gray-400 mb-2 font-mono tracking-wide">YOUR NAME</label>
                        <input type="text" name="name" class="w-full bg-gray-900/80 border border-gray-700 rounded-lg px-4 py-3 text-gray-200 focus:outline-none focus:border-blue-500 focus:ring-1 focus:ring-blue-500 transition-colors" required>
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-400 mb-2 font-mono tracking-wide">YOUR EMAIL</label>
                        <input type="email" name="email" class="w-full bg-gray-900/80 border border-gray-700 rounded-lg px-4 py-3 text-gray-200 focus:outline-none focus:border-blue-500 focus:ring-1 focus:ring-blue-500 transition-colors" required>
                    </div>
                </div>
                
                <div>
                    <label class="block text-sm font-medium text-gray-400 mb-2 font-mono tracking-wide">MESSAGE</label>
                    <textarea name="message" rows="5" class="w-full bg-gray-900/80 border border-gray-700 rounded-lg px-4 py-3 text-gray-200 focus:outline-none focus:border-blue-500 focus:ring-1 focus:ring-blue-500 transition-colors resize-none" required></textarea>
                </div>
                
                <div class="text-center pt-4">
                    <button type="submit" class="bg-blue-500 hover:bg-blue-400 text-gray-900 font-bold py-4 px-10 rounded-full shadow-[0_0_15px_rgba(59,130,246,0.4)] hover:shadow-[0_0_25px_rgba(59,130,246,0.6)] transition-all duration-300 transform hover:-translate-y-1 flex items-center justify-center mx-auto space-x-2">
                        <span>Send Secure Message</span>
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                    </button>
                </div>
            </form>
        </div>
    </div>
</section>
"""
content = contact_pattern.sub(new_contact, content)
with open('index.html', 'w') as f:
    f.write(content)
