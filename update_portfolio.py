import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Add spotlight div right after body
content = content.replace('<body class="bg-gray-900 text-gray-300 font-sans antialiased overflow-x-hidden">',
                          '<body class="bg-gray-900 text-gray-300 font-sans antialiased overflow-x-hidden">\n    <div id="spotlight"></div>')

# 2. Add Resume Button to desktop navbar
resume_btn = '<li><a href="#" class="bg-blue-500/10 text-blue-400 border border-blue-500 hover:bg-blue-500 hover:text-white px-4 py-2 rounded transition-colors duration-300">View Résumé</a></li>'
content = content.replace('<li><a href="#contact" class="text-gray-300 hover:text-blue-400 transition-colors">Contact</a></li>',
                          f'<li><a href="#contact" class="text-gray-300 hover:text-blue-400 transition-colors">Contact</a></li>\n            {resume_btn}')

# 3. Add Resume Button to mobile menu
mobile_resume = '<a href="#" class="bg-blue-500/10 text-blue-400 border border-blue-500 hover:bg-blue-500 hover:text-white text-lg transition-colors py-2 px-4 rounded">View Résumé</a>'
content = content.replace('<a href="#contact" class="text-gray-300 hover:text-blue-400 text-lg transition-colors">Contact</a>',
                          f'<a href="#contact" class="text-gray-300 hover:text-blue-400 text-lg transition-colors">Contact</a>\n            {mobile_resume}')

# 4. Modify images in Hero section
# Replace background
content = re.sub(r'src="images/profile.jpeg"(\s*alt="Background")', r'src="images/port1.jpeg"\1', content)
# Replace avatar
content = re.sub(r'src="images/profile.jpeg"(\s*alt="Your Profile Image")', r'src="images/port2.jpeg"\1', content)

# 5. Overhaul Projects Section
projects_new = """
<section id="projects" class="py-20 bg-gray-900 relative z-20">
    <div class="container mx-auto px-4">
        <h2 class="text-3xl md:text-5xl font-bold text-center text-white mb-16" data-aos="fade-up">Featured <span class="text-blue-400">Works</span></h2>
        
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-10">
            <!-- Project 1: AWS / DevOps -->
            <div class="project-card bg-gray-800 rounded-xl overflow-hidden shadow-lg border border-gray-700" data-aos="fade-up" data-aos-delay="100">
                <div class="p-8">
                    <h3 class="text-2xl font-bold text-blue-400 mb-3">AWS Infrastructure Automation</h3>
                    <p class="text-gray-400 mb-6">Designed and deployed a highly available, fault-tolerant infrastructure on AWS. Integrated CI/CD pipelines using GitHub Actions for seamless backend deployments.</p>
                    <div class="flex flex-wrap gap-2 mb-6">
                        <span class="px-3 py-1 bg-gray-900 border border-gray-600 rounded-full text-xs font-semibold text-blue-300">AWS (EC2, S3, RDS)</span>
                        <span class="px-3 py-1 bg-gray-900 border border-gray-600 rounded-full text-xs font-semibold text-blue-300">Terraform</span>
                        <span class="px-3 py-1 bg-gray-900 border border-gray-600 rounded-full text-xs font-semibold text-blue-300">Docker</span>
                    </div>
                    <a href="#" class="text-blue-400 hover:text-blue-300 font-bold flex items-center transition-colors">
                        View Project <svg class="w-4 h-4 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
                    </a>
                </div>
            </div>

            <!-- Project 2: Backend Security -->
            <div class="project-card bg-gray-800 rounded-xl overflow-hidden shadow-lg border border-gray-700" data-aos="fade-up" data-aos-delay="200">
                <div class="p-8">
                    <h3 class="text-2xl font-bold text-blue-400 mb-3">Backend Security & API Defense</h3>
                    <p class="text-gray-400 mb-6">Developed a secure RESTful API backend focusing on preventing OWASP Top 10 vulnerabilities. Implemented rate limiting, JWT authentication, and automated security scanning.</p>
                    <div class="flex flex-wrap gap-2 mb-6">
                        <span class="px-3 py-1 bg-gray-900 border border-gray-600 rounded-full text-xs font-semibold text-blue-300">Node.js / Express</span>
                        <span class="px-3 py-1 bg-gray-900 border border-gray-600 rounded-full text-xs font-semibold text-blue-300">Python</span>
                        <span class="px-3 py-1 bg-gray-900 border border-gray-600 rounded-full text-xs font-semibold text-blue-300">OWASP</span>
                    </div>
                    <a href="#" class="text-blue-400 hover:text-blue-300 font-bold flex items-center transition-colors">
                        View Code <svg class="w-4 h-4 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
                    </a>
                </div>
            </div>
            
            <!-- Project 3: Identity Repo -->
            <div class="project-card bg-gray-800 rounded-xl overflow-hidden shadow-lg border border-gray-700" data-aos="fade-up" data-aos-delay="300">
                <div class="p-8">
                    <h3 class="text-2xl font-bold text-blue-400 mb-3">DevOps Identity Bot</h3>
                    <p class="text-gray-400 mb-6">Built and configured an identity repository mapping cloud resources and establishing an automated footprint for professional DevOps networking.</p>
                    <div class="flex flex-wrap gap-2 mb-6">
                        <span class="px-3 py-1 bg-gray-900 border border-gray-600 rounded-full text-xs font-semibold text-blue-300">Git</span>
                        <span class="px-3 py-1 bg-gray-900 border border-gray-600 rounded-full text-xs font-semibold text-blue-300">Markdown</span>
                        <span class="px-3 py-1 bg-gray-900 border border-gray-600 rounded-full text-xs font-semibold text-blue-300">GitHub Actions</span>
                    </div>
                    <a href="https://github.com/ndigname-bot/ndigname-bot" target="_blank" class="text-blue-400 hover:text-blue-300 font-bold flex items-center transition-colors">
                        View Repository <svg class="w-4 h-4 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
                    </a>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Client Reviews Section (Stars) -->
<section id="reviews" class="py-20 bg-gray-800 relative z-20">
    <div class="container mx-auto px-4">
        <h2 class="text-3xl md:text-5xl font-bold text-center text-white mb-16" data-aos="fade-up">Client <span class="text-blue-400">Reviews</span></h2>
        
        <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8">
            <div class="bg-gray-900 p-8 rounded-xl border border-gray-700 shadow-xl" data-aos="fade-right">
                <div class="flex space-x-1 mb-4">
                    <svg class="star-icon" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg>
                    <svg class="star-icon" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg>
                    <svg class="star-icon" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg>
                    <svg class="star-icon" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg>
                    <svg class="star-icon" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg>
                </div>
                <p class="text-gray-300 italic mb-4">"Exceptional DevOps work! Delivered our AWS infrastructure perfectly and locked down our backend API. Highly recommended."</p>
                <p class="text-blue-400 font-semibold">- Tech Startup CTO</p>
            </div>
            <div class="bg-gray-900 p-8 rounded-xl border border-gray-700 shadow-xl" data-aos="fade-left" data-aos-delay="100">
                <div class="flex space-x-1 mb-4">
                    <svg class="star-icon" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg>
                    <svg class="star-icon" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg>
                    <svg class="star-icon" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg>
                    <svg class="star-icon" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg>
                    <svg class="star-icon" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg>
                </div>
                <p class="text-gray-300 italic mb-4">"Super fast communication, incredibly secure code, and flawlessly handled our cloud migration. Will hire again!"</p>
                <p class="text-blue-400 font-semibold">- E-Commerce Owner on Fiverr</p>
            </div>
        </div>
    </div>
</section>
"""
# Need to replace the old projects section with the new one.
# First, find the <section id="projects"> and its closing tag, then substitute.
# Looking at typical structure, it ends with </section>.
# Instead of complex regex, let's just replace a known snippet or regex block
content = re.sub(r'<section id="projects".*?</section>', projects_new, content, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(content)

print("HTML transformations completed.")
