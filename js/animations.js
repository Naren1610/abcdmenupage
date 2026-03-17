/**
 * Realistic Wok-Hay Background Animation
 * Renders flames, smoke, sparks, and simulates heat distortion on an HTML5 Canvas.
 * Optimized for mobile touch devices and subtle parallax.
 */

document.addEventListener("DOMContentLoaded", () => {
    const canvas = document.getElementById("wok-hay-canvas");
    const ctx = canvas.getContext("2d", { alpha: false });

    let width, height;
    let particles = [];
    let smokeParticles = [];
    let isMobile = window.innerWidth < 768;

    // Parallax mouse variables
    let mouseX = 0;
    let mouseY = 0;
    let targetMouseX = 0;
    let targetMouseY = 0;

    // Configurations
    let PARTICLE_COUNT = isMobile ? 40 : 80;
    let SMOKE_COUNT = isMobile ? 15 : 30;

    function resize() {
        width = window.innerWidth;
        height = window.innerHeight;
        isMobile = width < 768;

        PARTICLE_COUNT = isMobile ? 40 : 80;
        SMOKE_COUNT = isMobile ? 15 : 30;

        // Handle high DPI displays for crispness
        const dpr = window.devicePixelRatio || 1;
        canvas.width = width * dpr;
        canvas.height = height * dpr;
        ctx.scale(dpr, dpr);

        initParticles();
    }

    window.addEventListener("resize", resize);

    // Parallax tracking
    window.addEventListener("mousemove", (e) => {
        targetMouseX = (e.clientX / width - 0.5) * 2; // -1 to 1
        targetMouseY = (e.clientY / height - 0.5) * 2; // -1 to 1
    });

    // Touch equivalent for subtle gyro/movement if desired, but touchmove handles layout
    window.addEventListener("touchmove", (e) => {
        if (e.touches.length > 0) {
            targetMouseX = (e.touches[0].clientX / width - 0.5) * 2;
            targetMouseY = (e.touches[0].clientY / height - 0.5) * 2;
        }
    }, { passive: true });

    // Utility
    const random = (min, max) => Math.random() * (max - min) + min;

    // --- Spark Elements (Ember Fire) ---
    class Spark {
        constructor() {
            this.reset(true);
        }

        reset(initial = false) {
            this.x = random(0, width);
            // Spawn near bottom
            this.y = initial ? random(height * 0.5, height + 100) : height + random(10, 100);
            this.baseX = this.x;
            this.size = random(0.5, 3);
            this.speedY = random(-1, -4);
            this.speedX = random(-0.5, 0.5);
            this.life = random(0.5, 1);
            this.decay = random(0.005, 0.015);

            // Ember colors
            const hues = [15, 25, 35, 45]; // Deep orange to bright gold
            this.hue = hues[Math.floor(random(0, hues.length))];

            this.sinValue = random(0, Math.PI * 2);
            this.sinSpeed = random(0.02, 0.06);
            this.sinAmplitude = random(0.5, 3);

            // Parallax depth multiplier
            this.z = random(0.2, 1);
        }

        update() {
            this.life -= this.decay;

            // Wavy upward movement + heat turbulence
            this.sinValue += this.sinSpeed;
            this.baseX += this.speedX + Math.sin(this.sinValue) * this.sinAmplitude;
            this.y += this.speedY;

            // Apply Parallax offset
            this.x = this.baseX + (mouseX * 50 * this.z);

            // Speed up slightly as they rise (draft effect)
            this.speedY *= 1.02;

            if (this.life <= 0 || this.y < -10) {
                this.reset();
            }
        }

        draw() {
            const opacity = Math.max(0, this.life);
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);

            // Replaced expensive shadowBlur with pure fill to maintain 60FPS on mobile
            ctx.fillStyle = `hsla(${this.hue}, 100%, 70%, ${opacity})`;
            ctx.fill();
        }
    }

    // --- Smoke/Flame Elements ---
    class Smoke {
        constructor() {
            this.reset(true);
        }

        reset(initial = false) {
            this.x = random(width * 0.2, width * 0.8); // Concentrate towards center
            this.y = initial ? random(height * 0.2, height) : height + random(50, 150);
            this.baseX = this.x;
            this.size = random(50, 200);
            this.speedY = random(-0.5, -2);
            this.speedX = random(-0.5, 0.5);
            this.life = random(0.1, 0.5);
            this.decay = random(0.002, 0.005);
            this.angle = random(0, Math.PI * 2);
            this.spin = random(-0.01, 0.01);

            this.z = random(0.5, 1.5);
            this.isFlame = Math.random() > 0.6; // 40% are flame bursts, 60% smoke
        }

        update() {
            this.life -= this.decay;
            this.baseX += this.speedX;
            this.y += this.speedY;
            this.x = this.baseX + (mouseX * 30 * this.z);

            this.size += 0.5; // Expand as it rises
            this.angle += this.spin;

            if (this.life <= 0 || this.y < -this.size) {
                this.reset();
            }
        }

        draw() {
            const opacity = Math.max(0, this.life);
            ctx.save();
            ctx.translate(this.x, this.y);
            ctx.rotate(this.angle);

            // Flame/Smoke gradient mix
            const grad = ctx.createRadialGradient(0, 0, 0, 0, 0, this.size);

            if (this.isFlame) {
                // Flame colors
                grad.addColorStop(0, `rgba(255, 100, 0, ${opacity * 0.15})`);
                grad.addColorStop(0.4, `rgba(200, 40, 0, ${opacity * 0.05})`);
                grad.addColorStop(1, `rgba(0, 0, 0, 0)`);
                ctx.globalCompositeOperation = 'screen';
            } else {
                // Smoke colors - adds depth
                grad.addColorStop(0, `rgba(20, 10, 5, ${opacity * 0.4})`);
                grad.addColorStop(1, `rgba(0, 0, 0, 0)`);
                ctx.globalCompositeOperation = 'multiply'; // Darken the scene slightly
            }

            ctx.fillStyle = grad;
            ctx.beginPath();
            ctx.arc(0, 0, this.size, 0, Math.PI * 2);
            ctx.fill();

            ctx.restore();
        }
    }

    function initParticles() {
        particles = [];
        smokeParticles = [];
        for (let i = 0; i < SMOKE_COUNT; i++) smokeParticles.push(new Smoke());
        for (let i = 0; i < PARTICLE_COUNT; i++) particles.push(new Spark());
    }

    // Initialize layout
    resize();

    // Main animation loop
    function animate() {
        // Smooth mouse target interpolation for parallax
        mouseX += (targetMouseX - mouseX) * 0.05;
        mouseY += (targetMouseY - mouseY) * 0.05;

        // Base static background - dark cinematic gradient
        const bgGrad = ctx.createRadialGradient(
            width / 2 + (mouseX * 20), height, height * 0.2,
            width / 2, height, height * 1.5
        );
        bgGrad.addColorStop(0, '#2a0a00'); // Hot core at bottom center
        bgGrad.addColorStop(0.4, '#150500');
        bgGrad.addColorStop(1, '#050505'); // Outer dark

        ctx.fillStyle = bgGrad;
        ctx.globalCompositeOperation = 'source-over';
        ctx.fillRect(0, 0, width, height);

        // Heat distortion effect (simulated via subtle shifting curves at the base)
        ctx.beginPath();
        ctx.moveTo(0, height);
        for (let i = 0; i < width; i += 40) {
            let offset = Math.sin((Date.now() * 0.002) + (i * 0.02)) * 15;
            ctx.lineTo(i, height - 50 + offset);
        }
        ctx.lineTo(width, height);
        ctx.fillStyle = 'rgba(255, 50, 0, 0.02)';
        ctx.globalCompositeOperation = 'screen';
        ctx.fill();

        // Batch rendering by grouping composite operations
        // 1. Draw all smoke (multiply)
        ctx.globalCompositeOperation = 'multiply';
        smokeParticles.forEach(p => {
            if (!p.isFlame) p.draw();
        });

        // 2. Draw all flames and sparks (screen)
        ctx.globalCompositeOperation = 'screen';
        smokeParticles.forEach(p => {
            if (p.isFlame) p.draw();
        });

        particles.forEach(p => {
            p.update();
            p.draw();
        });

        // update smoke after drawing to avoid mixed state
        smokeParticles.forEach(p => p.update());

        requestAnimationFrame(animate);
    }

    // Start loop
    animate();

    // =========================================
    // Sequential Letter Glow Animation
    // =========================================
    const abcdNav = document.querySelector('.abcd-navigation');
    const abcdLetters = Array.from(document.querySelectorAll('.abcd-letter'));
    const activeLetters = abcdLetters.filter(l => !l.disabled);
    
    if (activeLetters.length > 0 && abcdNav) {
        let currentIdx = 0;
        
        // Add the global class to allow dimming of inactive peers
        abcdNav.classList.add('is-sequencing');
        
        const cycleGlow = () => {
            activeLetters.forEach(l => l.classList.remove('seq-active'));
            activeLetters[currentIdx].classList.add('seq-active');
            currentIdx = (currentIdx + 1) % activeLetters.length;
        };
        cycleGlow(); // Initialize first letter immediately
        setInterval(cycleGlow, 1500); // Cycle every 1.5 seconds
    }

    // =========================================
    // Intersection Observer for Menu Items
    // =========================================
    const observerOptions = {
        root: null, // Viewport
        rootMargin: '0px 0px -50px 0px', // Trigger slightly before the bottom
        threshold: 0.1 // 10% of the item must be visible
    };

    const scrollObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                // Optional: Stop observing once it's visible if we don't want it to hide again
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Initial check for all elements with .scroll-reveal
    const revealElements = document.querySelectorAll('.scroll-reveal');
    revealElements.forEach(el => scrollObserver.observe(el));
});
