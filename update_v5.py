import re

with open('index.html', 'r') as f:
    content = f.read()

# Replace the entire projects section
projects_pattern = re.compile(r'<section id="projects".*?</section>', re.DOTALL)
new_projects = """
<section id="projects" class="py-20 bg-gray-900 relative z-20 max-w-full overflow-hidden">
    <div class="container mx-auto px-4 max-w-5xl">
        <h2 class="text-3xl md:text-5xl font-bold text-center text-gray-100 mb-20 glow-text-subtle" data-aos="fade-up">Featured <span class="text-blue-400">Works</span></h2>
        
        <div class="flex flex-col space-y-24">
            
            <!-- Project 1: Cloud & DevOps (AWS Capstone) -->
            <div class="flex flex-col md:flex-row items-center relative" data-aos="fade-up">
                <div class="w-full md:w-7/12 relative group cursor-pointer z-10" onclick="openModal('AWS Infrastructure Capstone', 'Architected a highly scalable static and dynamic backend environment using AWS. Configured EC2, S3, and load balancing for high availability.', 'images/webdev proj.png')">
                    <div class="absolute inset-0 bg-blue-500/20 group-hover:bg-transparent transition duration-300 rounded-lg"></div>
                    <img src="images/webdev proj.png" alt="Cloud Architect Proof" class="w-full h-auto rounded-lg shadow-2xl filter brightness-90 group-hover:brightness-100 transition duration-300 border border-gray-700">
                </div>
                <div class="w-full md:w-6/12 md:-ml-12 mt-8 md:mt-0 relative z-20 md:text-right">
                    <p class="text-blue-400 font-mono text-sm mb-2">Cloud Architect / DevOps Engineer</p>
                    <h3 class="text-2xl font-bold text-gray-100 mb-4 hover:text-blue-400 transition-colors cursor-pointer">AWS Cloud Infrastructure</h3>
                    <div class="bg-gray-800 p-6 rounded-lg shadow-xl text-gray-400 mb-4 border border-gray-700/50 hover:shadow-blue-500/20 transition duration-300">
                        Designed and deployed a highly available infrastructure on AWS. Integrated seamless backend pipelines and web deployment architectures for the final capstone project.
                    </div>
                    <div class="flex flex-wrap md:justify-end gap-3 text-sm font-mono text-gray-300 mb-4">
                        <span>AWS</span> <span>Terraform</span> <span>Nginx</span>
                    </div>
                    <div class="flex md:justify-end space-x-4">
                        <button onclick="openModal('AWS Infrastructure Capstone', 'Architected a highly scalable static and dynamic backend environment using AWS. Configured EC2, S3, and load balancing for high availability.', 'images/webdev proj.png')" class="text-gray-400 hover:text-blue-400 transition-colors"><svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg></button>
                    </div>
                </div>
            </div>

            <!-- Project 2: Backend Developer (API Defense) -->
            <div class="flex flex-col md:flex-row-reverse items-center relative" data-aos="fade-up">
                <div class="w-full md:w-7/12 relative group cursor-pointer z-10" onclick="openModal('Backend Security & API Defense', 'Secured the entire backend architecture against SQL injection, XSS, and DDoS attacks. Implemented robust JWT auth flow.', 'images/backend_api_defense.jpg')">
                    <div class="absolute inset-0 bg-blue-500/20 group-hover:bg-transparent transition duration-300 rounded-lg"></div>
                    <img src="images/backend_api_defense.jpg" alt="Backend Developer Proof" class="w-full h-auto rounded-lg shadow-2xl filter brightness-90 group-hover:brightness-100 transition duration-300 border border-gray-700">
                </div>
                <div class="w-full md:w-6/12 md:-mr-12 mt-8 md:mt-0 relative z-20">
                    <p class="text-blue-400 font-mono text-sm mb-2">Backend Developer</p>
                    <h3 class="text-2xl font-bold text-gray-100 mb-4 hover:text-blue-400 transition-colors cursor-pointer">Backend API Defense</h3>
                    <div class="bg-gray-800 p-6 rounded-lg shadow-xl text-gray-400 mb-4 border border-gray-700/50 hover:shadow-blue-500/20 transition duration-300">
                        Developed a secure RESTful API backend focusing on mitigating OWASP Top 10 vulnerabilities. Implemented rate limiting, custom JWT authentication logic, and automated security scans.
                    </div>
                    <div class="flex flex-wrap gap-3 text-sm font-mono text-gray-300 mb-4">
                        <span>Node.js</span> <span>Express</span> <span>MongoDB</span> <span>OWASP</span>
                    </div>
                    <div class="flex space-x-4">
                        <button onclick="openModal('Backend Security & API Defense', 'Secured the entire backend architecture against SQL injection, XSS, and DDoS attacks. Implemented robust JWT auth flow.', 'images/backend_api_defense.jpg')" class="text-gray-400 hover:text-blue-400 transition-colors"><svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg></button>
                    </div>
                </div>
            </div>

            <!-- Project 3: Cybersecurity Specialist -->
            <div class="flex flex-col md:flex-row items-center relative" data-aos="fade-up">
                <div class="w-full md:w-7/12 relative group cursor-pointer z-10" onclick="openModal('Cybersecurity Infrastructure', 'Established robust intrusion detection systems, performed advanced penetration testing, and hardened enterprise network defenses.', 'images/cybersecurity.jpg')">
                    <div class="absolute inset-0 bg-blue-500/20 group-hover:bg-transparent transition duration-300 rounded-lg"></div>
                    <img src="images/cybersecurity.jpg" alt="Cybersecurity Specialist Proof" class="w-full h-auto rounded-lg shadow-2xl filter brightness-90 group-hover:brightness-100 transition duration-300 border border-gray-700">
                </div>
                <div class="w-full md:w-6/12 md:-ml-12 mt-8 md:mt-0 relative z-20 md:text-right">
                    <p class="text-blue-400 font-mono text-sm mb-2">Cybersecurity Specialist</p>
                    <h3 class="text-2xl font-bold text-gray-100 mb-4 hover:text-blue-400 transition-colors cursor-pointer">Network Threat Mitigation</h3>
                    <div class="bg-gray-800 p-6 rounded-lg shadow-xl text-gray-400 mb-4 border border-gray-700/50 hover:shadow-blue-500/20 transition duration-300">
                        Engineered comprehensive network defense mechanisms. Configured SIEM tools to monitor zero-day vulnerabilities and mitigated severe network threats through strict firewall protocols.
                    </div>
                    <div class="flex flex-wrap md:justify-end gap-3 text-sm font-mono text-gray-300 mb-4">
                        <span>Pen-Testing</span> <span>SIEM</span> <span>Firewalls</span>
                    </div>
                    <div class="flex md:justify-end space-x-4">
                        <button onclick="openModal('Cybersecurity Infrastructure', 'Established robust intrusion detection systems, performed advanced penetration testing, and hardened enterprise network defenses.', 'images/cybersecurity.jpg')" class="text-gray-400 hover:text-blue-400 transition-colors"><svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg></button>
                    </div>
                </div>
            </div>

            <!-- Project 4: Freelance Designer & Content Creator -->
            <div class="flex flex-col md:flex-row-reverse items-center relative" data-aos="fade-up">
                <div class="w-full md:w-7/12 relative group cursor-pointer z-10" onclick="openModal('Freelance Web Design', 'Designed high-converting landing pages, implemented brand identities, and managed digital content strategies for freelance clients.', 'images/freelance_design.jpg')">
                    <div class="absolute inset-0 bg-blue-500/20 group-hover:bg-transparent transition duration-300 rounded-lg"></div>
                    <img src="images/freelance_design.jpg" alt="Freelance Designer Proof" class="w-full h-auto rounded-lg shadow-2xl filter brightness-90 group-hover:brightness-100 transition duration-300 border border-gray-700">
                </div>
                <div class="w-full md:w-6/12 md:-mr-12 mt-8 md:mt-0 relative z-20">
                    <p class="text-blue-400 font-mono text-sm mb-2">Freelancer / Designer</p>
                    <h3 class="text-2xl font-bold text-gray-100 mb-4 hover:text-blue-400 transition-colors cursor-pointer">Digital Web Experiences</h3>
                    <div class="bg-gray-800 p-6 rounded-lg shadow-xl text-gray-400 mb-4 border border-gray-700/50 hover:shadow-blue-500/20 transition duration-300">
                        Crafted beautiful, responsive, and high-performance digital experiences. Specializing in UI/UX wireframing, branding, and technical content creation that converts visitors into active users.
                    </div>
                    <div class="flex flex-wrap gap-3 text-sm font-mono text-gray-300 mb-4">
                        <span>Figma</span> <span>Tailwind CSS</span> <span>Content Strategy</span>
                    </div>
                    <div class="flex space-x-4">
                        <button onclick="openModal('Freelance Web Design', 'Designed high-converting landing pages, implemented brand identities, and managed digital content strategies for freelance clients.', 'images/freelance_design.jpg')" class="text-gray-400 hover:text-blue-400 transition-colors"><svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg></button>
                    </div>
                </div>
            </div>

        </div>
    </div>
</section>
"""

content = projects_pattern.sub(new_projects, content)

with open('index.html', 'w') as f:
    f.write(content)
