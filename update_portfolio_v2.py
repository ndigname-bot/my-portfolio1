import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Fix mobile picture size and add floating animation
old_img_class = 'class="w-32 h-32 md:w-48 md:h-48 rounded-full mb-8 object-cover shadow-2xl shadow-blue-500/30 relative z-10"'
new_img_class = 'class="w-24 h-24 md:w-48 md:h-48 rounded-full mb-8 object-cover shadow-2xl shadow-blue-500/30 relative z-10 floating-avatar"'
content = content.replace(old_img_class, new_img_class)

# 2. Add an animation to the About section (we can add a pulse to an image or just a subtle tilt to the container)
# Let's see if there is an About section
about_header = '<h2 class="text-3xl md:text-5xl font-bold text-gray-100 mb-8"'
about_header_new = '<h2 class="text-3xl md:text-5xl font-bold text-gray-100 mb-8 glow-text-subtle"'
content = content.replace(about_header, about_header_new)

# 3. Add Project Proof Images & Detail buttons to the Projects Section
projects_new = """
<section id="projects" class="py-20 bg-gray-900 relative z-20 max-w-full overflow-hidden">
    <div class="container mx-auto px-4">
        <h2 class="text-3xl md:text-5xl font-bold text-center text-white mb-16" data-aos="fade-up">Featured <span class="text-blue-400">Works</span></h2>
        
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-10">
            <!-- Project 1: AWS / DevOps -->
            <div class="project-card bg-gray-800 rounded-xl overflow-hidden shadow-lg border border-gray-700 flex flex-col" data-aos="fade-up" data-aos-delay="100">
                <img src="images/Devops practice1.png" alt="AWS Automation Proof" class="w-full h-48 object-cover border-b border-gray-700">
                <div class="p-8 flex-grow flex flex-col">
                    <h3 class="text-2xl font-bold text-blue-400 mb-3">AWS Infrastructure Automation</h3>
                    <p class="text-gray-400 mb-6 flex-grow">Designed and deployed a highly available, fault-tolerant infrastructure on AWS. Integrated CI/CD pipelines using GitHub Actions for seamless backend deployments.</p>
                    <div class="flex flex-wrap gap-2 mb-6">
                        <span class="px-3 py-1 bg-gray-900 border border-gray-600 rounded-full text-xs font-semibold text-blue-300">AWS (EC2, S3, RDS)</span>
                        <span class="px-3 py-1 bg-gray-900 border border-gray-600 rounded-full text-xs font-semibold text-blue-300">Terraform</span>
                        <span class="px-3 py-1 bg-gray-900 border border-gray-600 rounded-full text-xs font-semibold text-blue-300">Docker</span>
                    </div>
                    <button onclick="openModal('AWS Infrastructure Automation', 'Deployed an autoscaling AWS environment spanning multiple availability zones. Handled load balancers, EC2 instances, and managed RDS databases securely within private subnets. Complete infrastructure as code using Terraform.', 'images/Devops practice1.png')" class="w-full text-center bg-blue-500/10 text-blue-400 border border-blue-500 hover:bg-blue-500 hover:text-white px-4 py-2 rounded transition-colors duration-300 font-bold">
                        View Details / Proof
                    </button>
                </div>
            </div>

            <!-- Project 2: Backend Security -->
            <div class="project-card bg-gray-800 rounded-xl overflow-hidden shadow-lg border border-gray-700 flex flex-col" data-aos="fade-up" data-aos-delay="200">
                <img src="images/Devops practice2.png" alt="Backend Security Proof" class="w-full h-48 object-cover border-b border-gray-700">
                <div class="p-8 flex-grow flex flex-col">
                    <h3 class="text-2xl font-bold text-blue-400 mb-3">Backend Security & API Defense</h3>
                    <p class="text-gray-400 mb-6 flex-grow">Developed a secure RESTful API backend focusing on preventing OWASP Top 10 vulnerabilities. Implemented rate limiting, JWT authentication, and automated security scanning.</p>
                    <div class="flex flex-wrap gap-2 mb-6">
                        <span class="px-3 py-1 bg-gray-900 border border-gray-600 rounded-full text-xs font-semibold text-blue-300">Node.js / Express</span>
                        <span class="px-3 py-1 bg-gray-900 border border-gray-600 rounded-full text-xs font-semibold text-blue-300">Python</span>
                        <span class="px-3 py-1 bg-gray-900 border border-gray-600 rounded-full text-xs font-semibold text-blue-300">OWASP</span>
                    </div>
                    <button onclick="openModal('Backend Security & API Defense', 'Secured the entire backend architecture against SQL injection, XSS, and DDoS attacks. Implemented robust JWT auth flow and encrypted payload transmissions.', 'images/Devops practice2.png')" class="w-full text-center bg-blue-500/10 text-blue-400 border border-blue-500 hover:bg-blue-500 hover:text-white px-4 py-2 rounded transition-colors duration-300 font-bold">
                        View Details / Proof
                    </button>
                </div>
            </div>
            
            <!-- Project 3: Identity Repo -->
            <div class="project-card bg-gray-800 rounded-xl overflow-hidden shadow-lg border border-gray-700 flex flex-col" data-aos="fade-up" data-aos-delay="300">
                <img src="images/devops error.png" alt="Identity Repo Proof" class="w-full h-48 object-cover border-b border-gray-700">
                <div class="p-8 flex-grow flex flex-col">
                    <h3 class="text-2xl font-bold text-blue-400 mb-3">DevOps Identity Bot</h3>
                    <p class="text-gray-400 mb-6 flex-grow">Built and configured an identity repository mapping cloud resources and establishing an automated footprint for professional DevOps networking.</p>
                    <div class="flex flex-wrap gap-2 mb-6">
                        <span class="px-3 py-1 bg-gray-900 border border-gray-600 rounded-full text-xs font-semibold text-blue-300">Git</span>
                        <span class="px-3 py-1 bg-gray-900 border border-gray-600 rounded-full text-xs font-semibold text-blue-300">Markdown</span>
                        <span class="px-3 py-1 bg-gray-900 border border-gray-600 rounded-full text-xs font-semibold text-blue-300">GitHub Actions</span>
                    </div>
                    <button onclick="openModal('DevOps Identity Bot', 'Configured an automated GitHub identity repository to act as a central hub for professional branding and automation metrics.', 'images/devops error.png')" class="w-full text-center bg-blue-500/10 text-blue-400 border border-blue-500 hover:bg-blue-500 hover:text-white px-4 py-2 rounded transition-colors duration-300 font-bold">
                        View Details / Proof
                    </button>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Project Details Modal -->
<div id="projectModal" class="fixed inset-0 bg-black/80 flex items-center justify-center z-50 hidden opacity-0 transition-opacity duration-300 px-4">
    <div class="bg-gray-800 rounded-xl border border-gray-700 shadow-2xl max-w-2xl w-full overflow-hidden transform scale-95 transition-transform duration-300" id="modalContentBlock">
        <div class="p-4 border-b border-gray-700 flex justify-between items-center bg-gray-900">
            <h3 id="modalTitle" class="text-2xl font-bold text-blue-400">Project Title</h3>
            <button onclick="closeModal()" class="text-gray-400 hover:text-white focus:outline-none">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
            </button>
        </div>
        <div class="p-6">
            <img id="modalImage" src="" alt="Project Proof" class="w-full h-auto max-h-64 object-contain mb-6 rounded border border-gray-700 bg-gray-900">
            <p id="modalDesc" class="text-gray-300 leading-relaxed">Project Details Here</p>
        </div>
        <div class="p-4 bg-gray-900 border-t border-gray-700 text-right">
            <button onclick="closeModal()" class="bg-blue-500 text-white px-6 py-2 rounded font-bold hover:bg-blue-600 transition-colors">Close</button>
        </div>
    </div>
</div>
"""
content = re.sub(r'<section id="projects".*?</section>', projects_new, content, flags=re.DOTALL)

# 4. Add parallax background overlay fixes
# Find background image and add bg-fixed class and make overlay darker
content = re.sub(r'<img\s+src="images/port1.jpeg"\s+alt="Background"\s+class="(.*?)"', r'<img src="images/port1.jpeg" alt="Background" class="\1 fixed object-cover h-screen w-screen z-0"', content)
# Make overlay completely cover
content = content.replace('bg-gradient-to-b from-gray-900/70 via-gray-900/60 to-gray-900/80', 'bg-gradient-to-b from-gray-900/90 via-gray-900/80 to-gray-900/95 fixed inset-0 z-0')

# Also fix the `overflow-x-hidden` which might be bypassed on mobile.
# We will wrap the main content in a div with overflow-hidden max-w-full.
content = content.replace('<body class="bg-gray-900 text-gray-300 font-sans antialiased overflow-x-hidden">', 
                          '<body class="bg-gray-900 text-gray-300 font-sans antialiased overflow-x-hidden w-full m-0 p-0">\n    <div class="max-w-full overflow-hidden relative">')
content = content.replace('</body>', '    </div>\n</body>')

with open('index.html', 'w') as f:
    f.write(content)
