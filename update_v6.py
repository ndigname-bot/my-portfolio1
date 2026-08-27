import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Update Projects: AWS project image -> aws_cloud.jpg
# 2. Update Projects: Project 4 -> Full Stack Web Developer (using webdev proj.png)
content = content.replace("images/webdev proj.png\" alt=\"Cloud Architect Proof\"", "images/aws_cloud.jpg\" alt=\"Cloud Architect Proof\"")
content = content.replace("'images/webdev proj.png')", "'images/aws_cloud.jpg')")

project4_old = """<p class="text-blue-400 font-mono text-sm mb-2">Freelancer / Designer</p>
                    <h3 class="text-2xl font-bold text-gray-100 mb-4 hover:text-blue-400 transition-colors cursor-pointer">Digital Web Experiences</h3>
                    <div class="bg-gray-800 p-6 rounded-lg shadow-xl text-gray-400 mb-4 border border-gray-700/50 hover:shadow-blue-500/20 transition duration-300">
                        Crafted beautiful, responsive, and high-performance digital experiences. Specializing in UI/UX wireframing, branding, and technical content creation that converts visitors into active users.
                    </div>
                    <div class="flex flex-wrap gap-3 text-sm font-mono text-gray-300 mb-4">
                        <span>Figma</span> <span>Tailwind CSS</span> <span>Content Strategy</span>
                    </div>"""
project4_new = """<p class="text-blue-400 font-mono text-sm mb-2">Full Stack Web Developer</p>
                    <h3 class="text-2xl font-bold text-gray-100 mb-4 hover:text-blue-400 transition-colors cursor-pointer">Dynamic Web Applications</h3>
                    <div class="bg-gray-800 p-6 rounded-lg shadow-xl text-gray-400 mb-4 border border-gray-700/50 hover:shadow-blue-500/20 transition duration-300">
                        Engineered responsive, high-performance full-stack web applications. Bridging the gap between sleek frontend user interfaces and robust, scalable backend database architectures.
                    </div>
                    <div class="flex flex-wrap gap-3 text-sm font-mono text-gray-300 mb-4">
                        <span>React</span> <span>Node.js</span> <span>MongoDB</span> <span>Tailwind</span>
                    </div>"""

content = content.replace(project4_old, project4_new)
content = content.replace("images/freelance_design.jpg\" alt=\"Freelance Designer Proof\"", "images/webdev proj.png\" alt=\"Full Stack Web Developer Proof\"")
content = content.replace("'images/freelance_design.jpg')", "'images/webdev proj.png')")
content = content.replace("'Freelance Web Design'", "'Full Stack Web Development'")
content = content.replace("'Designed high-converting landing pages, implemented brand identities, and managed digital content strategies for freelance clients.'", "'Built complete, responsive full-stack applications with robust backend databases and highly interactive user interfaces.'")


# 3. Upgrade Skills Section
skills_pattern = re.compile(r'<section id="skills".*?</section>', re.DOTALL)
new_skills = """
<section id="skills" class="py-20 bg-gray-900 relative z-20">
    <div class="container mx-auto px-4 max-w-6xl" data-aos="fade-up" data-aos-duration="1000">
        <h2 class="text-3xl md:text-5xl font-bold text-center text-gray-100 mb-16 glow-text-subtle">Technical <span class="text-blue-400">Arsenal</span></h2>
        
        <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
            <!-- Skill 1 -->
            <div class="bg-gray-800/50 border border-gray-700 rounded-xl p-6 text-center transform transition duration-300 hover:scale-105 hover:border-blue-500/50 hover:shadow-lg hover:shadow-blue-500/20 group">
                <div class="text-blue-400 mb-4 group-hover:text-blue-300 transition-colors">
                    <svg class="w-12 h-12 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg>
                </div>
                <h3 class="text-xl font-bold text-gray-200">AWS Cloud</h3>
                <p class="text-sm text-gray-400 mt-2">EC2, S3, RDS, VPC</p>
            </div>
            
            <!-- Skill 2 -->
            <div class="bg-gray-800/50 border border-gray-700 rounded-xl p-6 text-center transform transition duration-300 hover:scale-105 hover:border-blue-500/50 hover:shadow-lg hover:shadow-blue-500/20 group">
                <div class="text-blue-400 mb-4 group-hover:text-blue-300 transition-colors">
                    <svg class="w-12 h-12 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"></path></svg>
                </div>
                <h3 class="text-xl font-bold text-gray-200">Docker & K8s</h3>
                <p class="text-sm text-gray-400 mt-2">Containerization</p>
            </div>
            
            <!-- Skill 3 -->
            <div class="bg-gray-800/50 border border-gray-700 rounded-xl p-6 text-center transform transition duration-300 hover:scale-105 hover:border-blue-500/50 hover:shadow-lg hover:shadow-blue-500/20 group">
                <div class="text-blue-400 mb-4 group-hover:text-blue-300 transition-colors">
                    <svg class="w-12 h-12 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path></svg>
                </div>
                <h3 class="text-xl font-bold text-gray-200">Cybersecurity</h3>
                <p class="text-sm text-gray-400 mt-2">Pen-Testing, Firewalls</p>
            </div>
            
            <!-- Skill 4 -->
            <div class="bg-gray-800/50 border border-gray-700 rounded-xl p-6 text-center transform transition duration-300 hover:scale-105 hover:border-blue-500/50 hover:shadow-lg hover:shadow-blue-500/20 group">
                <div class="text-blue-400 mb-4 group-hover:text-blue-300 transition-colors">
                    <svg class="w-12 h-12 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M8 9l3 3-3 3m5 0h3M5 20h14a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
                </div>
                <h3 class="text-xl font-bold text-gray-200">Linux / Bash</h3>
                <p class="text-sm text-gray-400 mt-2">Server Administration</p>
            </div>
            
            <!-- Skill 5 -->
            <div class="bg-gray-800/50 border border-gray-700 rounded-xl p-6 text-center transform transition duration-300 hover:scale-105 hover:border-blue-500/50 hover:shadow-lg hover:shadow-blue-500/20 group">
                <div class="text-blue-400 mb-4 group-hover:text-blue-300 transition-colors">
                    <svg class="w-12 h-12 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"></path></svg>
                </div>
                <h3 class="text-xl font-bold text-gray-200">Backend APIs</h3>
                <p class="text-sm text-gray-400 mt-2">Node.js, Express, Python</p>
            </div>
            
            <!-- Skill 6 -->
            <div class="bg-gray-800/50 border border-gray-700 rounded-xl p-6 text-center transform transition duration-300 hover:scale-105 hover:border-blue-500/50 hover:shadow-lg hover:shadow-blue-500/20 group">
                <div class="text-blue-400 mb-4 group-hover:text-blue-300 transition-colors">
                    <svg class="w-12 h-12 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M4 7v10c0 2.21 3.582 4 8 4s8-1.79 8-4V7M4 7c0 2.21 3.582 4 8 4s8-1.79 8-4M4 7c0-2.21 3.582-4 8-4s8 1.79 8 4m0 5c0 2.21-3.582 4-8 4s-8-1.79-8-4"></path></svg>
                </div>
                <h3 class="text-xl font-bold text-gray-200">Databases</h3>
                <p class="text-sm text-gray-400 mt-2">MongoDB, PostgreSQL</p>
            </div>
            
            <!-- Skill 7 -->
            <div class="bg-gray-800/50 border border-gray-700 rounded-xl p-6 text-center transform transition duration-300 hover:scale-105 hover:border-blue-500/50 hover:shadow-lg hover:shadow-blue-500/20 group">
                <div class="text-blue-400 mb-4 group-hover:text-blue-300 transition-colors">
                    <svg class="w-12 h-12 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
                </div>
                <h3 class="text-xl font-bold text-gray-200">Frontend UI</h3>
                <p class="text-sm text-gray-400 mt-2">React, Tailwind CSS</p>
            </div>
            
            <!-- Skill 8 -->
            <div class="bg-gray-800/50 border border-gray-700 rounded-xl p-6 text-center transform transition duration-300 hover:scale-105 hover:border-blue-500/50 hover:shadow-lg hover:shadow-blue-500/20 group">
                <div class="text-blue-400 mb-4 group-hover:text-blue-300 transition-colors">
                    <svg class="w-12 h-12 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                </div>
                <h3 class="text-xl font-bold text-gray-200">CI / CD</h3>
                <p class="text-sm text-gray-400 mt-2">GitHub Actions, Terraform</p>
            </div>
        </div>
    </div>
</section>
"""
content = skills_pattern.sub(new_skills, content)

with open('index.html', 'w') as f:
    f.write(content)
