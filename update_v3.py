import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Update Title
content = re.sub(r'<title>.*?</title>', '<title>Emmanuel Nelimo | DevOps Engineer</title>', content)

# 2. LinkedIn Style Hero Section & Update typing animation roles
# Extract from `<section id="home"` to `</section>` using regex.
home_pattern = re.compile(r'<section id="home".*?</section>', re.DOTALL)
new_home = """
<section id="home" class="relative bg-gray-900 pb-16">
    <!-- Cover Banner (port1.jpeg horizontally at top) -->
    <div class="relative w-full h-48 md:h-72 overflow-hidden bg-gray-800">
        <img src="images/port1.jpeg" alt="Cover Banner" class="w-full h-full object-cover opacity-80" data-aos="fade-in" data-aos-duration="1500">
    </div>
    
    <!-- Profile Info Area (port2.jpeg attached in middle/overlapping) -->
    <div class="container mx-auto px-4 relative flex flex-col items-center -mt-20 md:-mt-32">
        <img 
            src="images/port2.jpeg" 
            alt="Your Profile Image" 
            class="w-32 h-32 md:w-56 md:h-56 rounded-full border-8 border-gray-900 object-cover shadow-2xl relative z-10 floating-avatar bg-gray-900" 
            data-aos="fade-up" 
            data-aos-duration="1000"
        >
        
        <div class="text-center z-10 mt-6" data-aos="fade-up" data-aos-duration="1000" data-aos-delay="200">
            <h1 class="text-4xl md:text-6xl font-bold text-gray-100 mb-3">Emmanuel Ndignam Nelimo</h1>
            
            <p class="text-xl md:text-3xl text-gray-400 mb-8">
                I am <span id="typed-skills" class="text-blue-400 font-semibold relative inline-block min-w-[200px] text-left"></span>
                <span class="typed-cursor animate-blink" aria-hidden="true">|</span>
            </p>
            
            <a href="#projects" class="bg-blue-500/10 text-blue-400 border border-blue-500 hover:bg-blue-500 hover:text-white px-8 py-3 rounded-full font-semibold transition-all duration-300 transform hover:scale-105">Explore My Work</a>
        </div>
    </div>
    
<style>
.animate-blink { animation: blink 0.7s step-end infinite; }
@keyframes blink { 50% { opacity: 0; } }
#typed-skills { display: inline-flex; white-space: nowrap; overflow: hidden; }
</style>
<script>
document.addEventListener('DOMContentLoaded', () => {
    const typedElement = document.getElementById('typed-skills');
    if (!typedElement) return;

    const roles = [
        "a DevOps engineer",
        "a Backend Developer",
        "an aspiring cybersecurity specialist",
        "a cloud architect",
        "a freelancer"
    ];

    let roleIndex = 0; let charIndex = 0; let isDeleting = false;
    let typingDelay = 80; let deletingDelay = 50; let pauseAfterComplete = 1800;

    function type() {
        const currentRole = roles[roleIndex];
        if (!isDeleting && charIndex <= currentRole.length) {
            typedElement.textContent = currentRole.substring(0, charIndex);
            charIndex++;
            setTimeout(type, typingDelay);
        } else if (!isDeleting && charIndex > currentRole.length) {
            setTimeout(() => { isDeleting = true; type(); }, pauseAfterComplete);
        } else if (isDeleting && charIndex > 0) {
            typedElement.textContent = currentRole.substring(0, charIndex - 1);
            charIndex--;
            setTimeout(type, deletingDelay);
        } else if (isDeleting && charIndex === 0) {
            isDeleting = false;
            roleIndex = (roleIndex + 1) % roles.length;
            setTimeout(type, 500);
        }
    }

    const observer = new IntersectionObserver((entries) => {
        if (entries[0].isIntersecting) { type(); observer.disconnect(); }
    }, { threshold: 0.3 });
    observer.observe(typedElement.parentElement);
});
</script>
</section>
"""
content = home_pattern.sub(new_home, content)

# 3. Update About Me
about_old = "With over 1 year in studying cybersecurity and DevOps, I specialize in securing cloud infrastructures, automating deployments, and mitigating threats. Based in Buduburam, Ghana, I've worked on projects involving AWS, Kubernetes, and ethical hacking. Passionate about building resilient systems in the futrure."
about_new = "With around 3 years of experience in Backend Development, Cybersecurity, and DevOps, I specialize in architecting secure cloud infrastructures, automating complex deployments, and developing robust backend APIs. Based in Buduburam, Ghana, I've delivered robust solutions involving AWS, CI/CD pipelines, and advanced threat mitigation. Passionate about building resilient, highly-scalable systems for the future."
content = content.replace(about_old, about_new)

# 4. Update Projects to Brittany style + Capstone Evidence
projects_pattern = re.compile(r'<section id="projects".*?</section>', re.DOTALL)
new_projects = """
<section id="projects" class="py-20 bg-gray-900 relative z-20 max-w-full overflow-hidden">
    <div class="container mx-auto px-4 max-w-5xl">
        <h2 class="text-3xl md:text-5xl font-bold text-center text-gray-100 mb-20 glow-text-subtle" data-aos="fade-up">Featured <span class="text-blue-400">Works</span></h2>
        
        <div class="flex flex-col space-y-24">
            <!-- Project 1: AWS Capstone -->
            <div class="flex flex-col md:flex-row items-center relative" data-aos="fade-up">
                <div class="w-full md:w-7/12 relative group cursor-pointer z-10" onclick="openModal('AWS Infrastructure Capstone', 'Architected a highly scalable static and dynamic backend environment using AWS. Configured EC2, S3, and load balancing for high availability.', 'images/webdev proj.png')">
                    <div class="absolute inset-0 bg-blue-500/20 group-hover:bg-transparent transition duration-300 rounded-lg"></div>
                    <img src="images/webdev proj.png" alt="AWS Capstone Proof" class="w-full h-auto rounded-lg shadow-2xl filter brightness-90 group-hover:brightness-100 transition duration-300 border border-gray-700">
                </div>
                <div class="w-full md:w-6/12 md:-ml-12 mt-8 md:mt-0 relative z-20 md:text-right">
                    <p class="text-blue-400 font-mono text-sm mb-2">Capstone Project</p>
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

            <!-- Project 2: Backend Security (Reversed) -->
            <div class="flex flex-col md:flex-row-reverse items-center relative" data-aos="fade-up">
                <div class="w-full md:w-7/12 relative group cursor-pointer z-10" onclick="openModal('Backend Security & API Defense', 'Secured the entire backend architecture against SQL injection, XSS, and DDoS attacks. Implemented robust JWT auth flow.', 'images/Devops practice2.png')">
                    <div class="absolute inset-0 bg-blue-500/20 group-hover:bg-transparent transition duration-300 rounded-lg"></div>
                    <img src="images/Devops practice2.png" alt="Backend Security Proof" class="w-full h-auto rounded-lg shadow-2xl filter brightness-90 group-hover:brightness-100 transition duration-300 border border-gray-700">
                </div>
                <div class="w-full md:w-6/12 md:-mr-12 mt-8 md:mt-0 relative z-20">
                    <p class="text-blue-400 font-mono text-sm mb-2">Featured Project</p>
                    <h3 class="text-2xl font-bold text-gray-100 mb-4 hover:text-blue-400 transition-colors cursor-pointer">Backend API Defense</h3>
                    <div class="bg-gray-800 p-6 rounded-lg shadow-xl text-gray-400 mb-4 border border-gray-700/50 hover:shadow-blue-500/20 transition duration-300">
                        Developed a secure RESTful API backend focusing on mitigating OWASP Top 10 vulnerabilities. Implemented rate limiting, custom JWT authentication logic, and automated security scans.
                    </div>
                    <div class="flex flex-wrap gap-3 text-sm font-mono text-gray-300 mb-4">
                        <span>Node.js</span> <span>Express</span> <span>MongoDB</span> <span>OWASP</span>
                    </div>
                    <div class="flex space-x-4">
                        <button onclick="openModal('Backend Security & API Defense', 'Secured the entire backend architecture against SQL injection, XSS, and DDoS attacks. Implemented robust JWT auth flow.', 'images/Devops practice2.png')" class="text-gray-400 hover:text-blue-400 transition-colors"><svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg></button>
                    </div>
                </div>
            </div>

            <!-- Project 3: Identity Repo -->
            <div class="flex flex-col md:flex-row items-center relative" data-aos="fade-up">
                <div class="w-full md:w-7/12 relative group cursor-pointer z-10" onclick="openModal('DevOps Identity Bot', 'Configured an automated GitHub identity repository to act as a central hub for professional branding and automation metrics.', 'images/devops error.png')">
                    <div class="absolute inset-0 bg-blue-500/20 group-hover:bg-transparent transition duration-300 rounded-lg"></div>
                    <img src="images/devops error.png" alt="Identity Repo Proof" class="w-full h-auto rounded-lg shadow-2xl filter brightness-90 group-hover:brightness-100 transition duration-300 border border-gray-700">
                </div>
                <div class="w-full md:w-6/12 md:-ml-12 mt-8 md:mt-0 relative z-20 md:text-right">
                    <p class="text-blue-400 font-mono text-sm mb-2">Automation Initiative</p>
                    <h3 class="text-2xl font-bold text-gray-100 mb-4 hover:text-blue-400 transition-colors cursor-pointer">DevOps Identity Bot</h3>
                    <div class="bg-gray-800 p-6 rounded-lg shadow-xl text-gray-400 mb-4 border border-gray-700/50 hover:shadow-blue-500/20 transition duration-300">
                        Built and configured an identity repository mapping cloud resources and establishing an automated footprint for professional DevOps networking and GitHub Action deployments.
                    </div>
                    <div class="flex flex-wrap md:justify-end gap-3 text-sm font-mono text-gray-300 mb-4">
                        <span>Git</span> <span>Actions</span> <span>Markdown</span>
                    </div>
                    <div class="flex md:justify-end space-x-4">
                        <button onclick="openModal('DevOps Identity Bot', 'Configured an automated GitHub identity repository to act as a central hub for professional branding and automation metrics.', 'images/devops error.png')" class="text-gray-400 hover:text-blue-400 transition-colors"><svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg></button>
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
