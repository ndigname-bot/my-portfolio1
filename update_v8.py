import re

with open('index.html', 'r') as f:
    content = f.read()

contact_pattern = re.compile(r'<section id="contact".*?</section>', re.DOTALL)
new_contact = """
<section id="contact" class="py-24 bg-gray-900 relative z-20">
    <div class="container mx-auto px-4 max-w-3xl" data-aos="fade-up">
        <h2 class="text-3xl font-bold text-center text-blue-400 mb-12 font-mono glow-text-subtle">>>> Initiate_Connection()</h2>
        
        <div class="bg-[#0D1117] rounded-lg shadow-2xl border border-gray-700 overflow-hidden font-mono text-sm relative">
            <!-- Terminal Header -->
            <div class="bg-gray-800 px-4 py-3 flex items-center border-b border-gray-700">
                <div class="flex space-x-2 absolute">
                    <div class="w-3 h-3 rounded-full bg-red-500"></div>
                    <div class="w-3 h-3 rounded-full bg-yellow-500"></div>
                    <div class="w-3 h-3 rounded-full bg-green-500"></div>
                </div>
                <div class="mx-auto text-gray-400 text-xs text-center flex-grow font-bold tracking-widest">nelimo@devops:~</div>
            </div>
            
            <!-- Terminal Body -->
            <div class="p-6 text-green-400 md:p-8">
                <p class="mb-2">Welcome to Emmanuel's Secure Channel.</p>
                <p class="mb-8 text-gray-400">Please provide credentials to establish a secure transmission.</p>
                
                <form action="https://formspree.io/f/mdalbrll" method="POST" class="space-y-6">
                    <div class="flex flex-col md:flex-row md:items-end">
                        <span class="text-blue-400 mr-2 mb-1 md:mb-0">guest@secure:~$</span>
                        <span class="text-gray-400 mr-2 mb-1 md:mb-0">export NAME=</span>
                        <input type="text" name="name" class="bg-transparent border-b border-gray-700 focus:border-green-400 text-green-300 outline-none flex-grow py-1" required>
                    </div>
                    
                    <div class="flex flex-col md:flex-row md:items-end">
                        <span class="text-blue-400 mr-2 mb-1 md:mb-0">guest@secure:~$</span>
                        <span class="text-gray-400 mr-2 mb-1 md:mb-0">export EMAIL=</span>
                        <input type="email" name="email" class="bg-transparent border-b border-gray-700 focus:border-green-400 text-green-300 outline-none flex-grow py-1" required>
                    </div>
                    
                    <div class="flex flex-col mt-6">
                        <span class="text-blue-400 mb-2">guest@secure:~$ <span class="text-gray-400">cat &lt;&lt; 'EOF' &gt; transmission.txt</span></span>
                        <textarea name="message" class="bg-gray-900/50 border border-gray-700 focus:border-green-400 rounded text-green-300 p-4 h-32 outline-none resize-none shadow-inner" required></textarea>
                        <span class="text-gray-400 mt-2">EOF</span>
                    </div>
                    
                    <div class="mt-8 flex items-center pt-4">
                        <span class="text-blue-400 mr-4">guest@secure:~$</span>
                        <button type="submit" class="bg-green-500/10 text-green-400 font-bold hover:text-gray-900 hover:bg-green-400 px-6 py-2 border border-green-500 rounded transition-all duration-300 shadow-[0_0_10px_rgba(74,222,128,0.2)] hover:shadow-[0_0_20px_rgba(74,222,128,0.6)]">
                            ./send_transmission.sh
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</section>
"""
content = contact_pattern.sub(new_contact, content)
with open('index.html', 'w') as f:
    f.write(content)
