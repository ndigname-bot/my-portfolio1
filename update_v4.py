import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Link Resume
content = content.replace('href="#" class="bg-blue-500/10 text-blue-400 border border-blue-500 hover:bg-blue-500 hover:text-white px-4 py-2 rounded transition-colors duration-300">View Résumé', 
                          'href="resume.pdf" target="_blank" class="bg-blue-500/10 text-blue-400 border border-blue-500 hover:bg-blue-500 hover:text-white px-4 py-2 rounded transition-colors duration-300">View Résumé')

content = content.replace('href="#" class="bg-blue-500/10 text-blue-400 border border-blue-500 hover:bg-blue-500 hover:text-white text-lg transition-colors py-2 px-4 rounded">View Résumé', 
                          'href="resume.pdf" target="_blank" class="bg-blue-500/10 text-blue-400 border border-blue-500 hover:bg-blue-500 hover:text-white text-lg transition-colors py-2 px-4 rounded">View Résumé')

# 2. Update Project Images with the AI generated ones
content = content.replace('images/Devops practice2.png', 'images/backend_api_defense.jpg')
content = content.replace('images/devops error.png', 'images/identity_bot.jpg')

# 3. Replace Reviews with Tech Stack Marquee
reviews_pattern = re.compile(r'<section id="reviews".*?</section>', re.DOTALL)
tech_stack_marquee = """
<section id="tech-stack" class="py-16 bg-gray-900 border-t border-gray-800 relative z-20 overflow-hidden">
    <div class="container mx-auto px-4 mb-10">
        <h2 class="text-3xl font-bold text-center text-gray-100 glow-text-subtle">Core <span class="text-blue-400">Technologies</span></h2>
    </div>
    
    <div class="marquee-container relative w-full overflow-hidden flex items-center h-24 bg-gray-800/50 shadow-inner">
        <!-- Fading edges -->
        <div class="absolute left-0 top-0 w-24 h-full bg-gradient-to-r from-gray-900 to-transparent z-10"></div>
        <div class="absolute right-0 top-0 w-24 h-full bg-gradient-to-l from-gray-900 to-transparent z-10"></div>
        
        <!-- Marquee content -->
        <div class="marquee-content flex space-x-12 px-12 text-2xl md:text-4xl font-mono text-gray-500 font-bold items-center">
            <span class="hover:text-blue-400 transition-colors">AWS</span>
            <span>•</span>
            <span class="hover:text-blue-400 transition-colors">DOCKER</span>
            <span>•</span>
            <span class="hover:text-blue-400 transition-colors">KUBERNETES</span>
            <span>•</span>
            <span class="hover:text-blue-400 transition-colors">TERRAFORM</span>
            <span>•</span>
            <span class="hover:text-blue-400 transition-colors">NODE.JS</span>
            <span>•</span>
            <span class="hover:text-blue-400 transition-colors">PYTHON</span>
            <span>•</span>
            <span class="hover:text-blue-400 transition-colors">LINUX</span>
            <span>•</span>
            <span class="hover:text-blue-400 transition-colors">GITHUB ACTIONS</span>
            <span>•</span>
            <span class="hover:text-blue-400 transition-colors">AWS</span>
            <span>•</span>
            <span class="hover:text-blue-400 transition-colors">DOCKER</span>
            <span>•</span>
            <span class="hover:text-blue-400 transition-colors">KUBERNETES</span>
            <span>•</span>
            <span class="hover:text-blue-400 transition-colors">TERRAFORM</span>
        </div>
    </div>
</section>
"""
content = reviews_pattern.sub(tech_stack_marquee, content)

with open('index.html', 'w') as f:
    f.write(content)
