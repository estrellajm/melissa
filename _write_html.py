html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Melissa's Pawsome Pet Care \u2014 Professional Pet Sitting Services</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #2E7D6B;
            --primary-light: #3D9B87;
            --accent: #F4845F;
            --bg: #F7F7F5;
            --surface: #FFFFFF;
            --text: #1A1A1E;
            --text-muted: #6B7280;
            --border: #E5E7EB;
            --shadow-sm: 0 1px 3px rgba(0,0,0,0.07);
            --shadow-md: 0 4px 16px rgba(0,0,0,0.08);
            --shadow-lg: 0 16px 48px rgba(0,0,0,0.12);
            --radius: 16px;
            --radius-sm: 10px;
        }
        *, *::before, *::after { margin:0; padding:0; box-sizing:border-box; }
        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background: var(--bg);
            color: var(--text);
            line-height: 1.6;
            overflow-x: hidden;
        }
        /* NAV */
        nav {
            position: sticky; top: 0; z-index: 200;
            background: rgba(255,255,255,0.92);
            backdrop-filter: blur(14px);
            -webkit-backdrop-filter: blur(14px);
            border-bottom: 1px solid var(--border);
        }
        .nav-inner {
            max-width: 1100px; margin: 0 auto; padding: 0 24px;
            height: 64px; display: flex; align-items: center; justify-content: space-between;
        }
        .nav-brand { font-size: 0.95rem; font-weight: 700; color: var(--primary); }
        .nav-links { display: flex; align-items: center; gap: 28px; list-style: none; }
        .nav-links a { text-decoration: none; font-size: 0.875rem; font-weight: 500; color: var(--text-muted); transition: color 0.18s; }
        .nav-links a:hover { color: var(--primary); }
        .nav-cta { background: var(--primary) !important; color: #fff !important; padding: 8px 20px; border-radius: 50px; }
        .nav-cta:hover { background: var(--primary-light) !important; }
        /* HERO */
        header { background: var(--surface); border-bottom: 1px solid var(--border); padding: 80px 24px 72px; text-align: center; }
        header img { width: 110px; height: 110px; object-fit: cover; border-radius: 50%; border: 3px solid var(--border); margin-bottom: 24px; box-shadow: var(--shadow-md); display: block; margin-inline: auto; }
        .hero-badge { display: inline-flex; align-items: center; background: #EEF6F3; color: var(--primary); font-size: 0.72rem; font-weight: 700; padding: 5px 14px; border-radius: 50px; margin-bottom: 18px; letter-spacing: 0.08em; text-transform: uppercase; }
        h1 { font-size: clamp(1.9rem, 5vw, 2.9rem); font-weight: 700; color: var(--text); letter-spacing: -0.03em; line-height: 1.1; }
        .tagline { font-size: 1.05rem; color: var(--text-muted); margin-top: 10px; }
        /* LAYOUT */
        .container { max-width: 1100px; margin: 0 auto; padding: 72px 24px; }
        section { margin-bottom: 80px; }
        .section-label { font-size: 0.7rem; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; color: var(--primary); margin-bottom: 6px; }
        h2 { font-size: clamp(1.4rem, 3vw, 1.85rem); font-weight: 700; color: var(--text); letter-spacing: -0.02em; margin-bottom: 6px; }
        .section-desc { color: var(--text-muted); font-size: 0.975rem; margin-bottom: 36px; max-width: 500px; }
        /* ABOUT */
        .about-card { background: var(--surface); border-radius: var(--radius); border: 1px solid var(--border); padding: 40px 48px; display: grid; grid-template-columns: 1fr 1fr; gap: 48px; align-items: center; box-shadow: var(--shadow-sm); }
        .about-text p { color: var(--text-muted); font-size: 0.975rem; margin-bottom: 14px; }
        .about-text p:last-child { margin-bottom: 0; }
        .about-stats { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
        .stat { background: var(--bg); border-radius: var(--radius-sm); padding: 20px; text-align: center; }
        .stat-number { font-size: 1.7rem; font-weight: 700; color: var(--primary); line-height: 1; }
        .stat-label { font-size: 0.78rem; color: var(--text-muted); margin-top: 4px; }
        /* SERVICES */
        .services { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 16px; }
        .service-item { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 28px; cursor: pointer; transition: border-color 0.18s, box-shadow 0.18s, transform 0.18s; user-select: none; -webkit-user-select: none; }
        .service-item:hover { border-color: var(--primary); box-shadow: var(--shadow-md); transform: translateY(-3px); }
        .service-item:active { transform: translateY(0); }
        .service-chip { display: inline-flex; align-items: center; justify-content: center; width: 48px; height: 48px; background: #EEF6F3; border-radius: 12px; font-size: 1.4rem; margin-bottom: 14px; }
        .service-item h3 { font-size: 0.975rem; font-weight: 600; color: var(--text); margin-bottom: 6px; }
        .service-item p { font-size: 0.85rem; color: var(--text-muted); line-height: 1.55; }
        .service-link { display: inline-flex; align-items: center; font-size: 0.78rem; font-weight: 600; color: var(--primary); margin-top: 14px; }
        .service-link::after { content: " \\2192"; transition: transform 0.18s; }
        .service-item:hover .service-link::after { transform: translateX(3px); }
        /* NOTICE */
        .notice-card { background: #FFF8F6; border: 1px solid #FDDDD5; border-radius: var(--radius); padding: 32px 40px; }
        .notice-card h3 { font-size: 0.975rem; font-weight: 700; color: #B84530; margin-bottom: 16px; display: flex; align-items: center; gap: 8px; }
        .notice-list { list-style: none; padding: 0; }
        .notice-list li { padding: 11px 0; font-size: 0.9rem; color: #6B3B2D; border-bottom: 1px solid #FDDDD5; display: flex; align-items: flex-start; gap: 10px; }
        .notice-list li:last-child { border-bottom: none; }
        .notice-list li::before { content: "\\2192"; color: var(--accent); font-weight: 700; flex-shrink: 0; margin-top: 1px; }
        .notice-footnote { font-size: 0.82rem; color: #9B6B5A; margin-top: 18px; font-style: italic; }
        /* WHY */
        .why-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(270px, 1fr)); gap: 14px; list-style: none; padding: 0; }
        .why-grid li { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius-sm); padding: 16px 20px; font-size: 0.9rem; color: var(--text); display: flex; align-items: center; gap: 12px; }
        .why-grid li::before { content: "\\2713"; display: flex; align-items: center; justify-content: center; width: 22px; height: 22px; background: #EEF6F3; color: var(--primary); border-radius: 50%; font-size: 0.72rem; font-weight: 700; flex-shrink: 0; }
        /* CTA */
        .cta-wrap { text-align: center; margin: 16px 0 64px; }
        .cta-button { display: inline-block; background: var(--primary); color: #fff; padding: 14px 36px; border-radius: 50px; font-size: 0.925rem; font-weight: 600; text-decoration: none; transition: background 0.18s, transform 0.18s; }
        .cta-button:hover { background: var(--primary-light); transform: translateY(-2px); }
        /* CONTACT */
        .contact-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-top: 28px; }
        .contact-item { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius-sm); padding: 20px 24px; display: flex; align-items: flex-start; gap: 14px; }
        .contact-icon { font-size: 1.2rem; flex-shrink: 0; margin-top: 2px; }
        .contact-label { font-size: 0.7rem; font-weight: 700; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.07em; margin-bottom: 4px; }
        .contact-value { font-size: 0.9rem; font-weight: 500; color: var(--text); word-break: break-word; }
        /* FOOTER */
        footer { background: var(--surface); border-top: 1px solid var(--border); padding: 40px 24px; text-align: center; }
        .footer-inner { max-width: 1100px; margin: 0 auto; }
        .footer-brand { font-size: 0.9rem; font-weight: 700; color: var(--primary); margin-bottom: 6px; }
        footer p { font-size: 0.82rem; color: var(--text-muted); }
        /* MODALS */
        .modal { display: none; position: fixed; z-index: 1000; left: 0; top: 0; width: 100%; height: 100%; background: rgba(15,15,20,0.55); backdrop-filter: blur(6px); -webkit-backdrop-filter: blur(6px); }
        .modal.open { display: flex; align-items: flex-start; justify-content: center; padding-top: 48px; }
        .modal-content { background: var(--surface); border-radius: 20px; padding: 40px; width: 90%; max-width: 620px; max-height: 88vh; overflow-y: auto; box-shadow: var(--shadow-lg); position: relative; border: 1px solid var(--border); animation: slideUp 0.22s ease; }
        @keyframes slideUp { from { transform: translateY(16px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }
        .modal-content::-webkit-scrollbar { width: 5px; }
        .modal-content::-webkit-scrollbar-track { background: var(--bg); border-radius: 5px; }
        .modal-content::-webkit-scrollbar-thumb { background: var(--border); border-radius: 5px; }
        .close { position: absolute; top: 18px; right: 20px; width: 30px; height: 30px; border-radius: 50%; background: var(--bg); border: 1px solid var(--border); display: flex; align-items: center; justify-content: center; font-size: 0.9rem; cursor: pointer; color: var(--text-muted); transition: background 0.15s; user-select: none; -webkit-user-select: none; }
        .close:hover { background: var(--border); color: var(--text); }
        .modal-icon { font-size: 2.25rem; margin-bottom: 10px; }
        .modal-title { font-size: 1.3rem; font-weight: 700; color: var(--text); letter-spacing: -0.02em; margin-bottom: 6px; }
        .modal-subtitle { font-size: 0.9rem; color: var(--text-muted); margin-bottom: 24px; }
        .modal-section-title { font-size: 0.78rem; font-weight: 700; color: var(--primary); text-transform: uppercase; letter-spacing: 0.08em; margin: 22px 0 12px; }
        .modal-body ul { list-style: none; padding: 0; }
        .modal-body li { padding: 12px 14px; margin-bottom: 8px; background: var(--bg); border-radius: var(--radius-sm); font-size: 0.875rem; color: var(--text); line-height: 1.55; border-left: 3px solid var(--primary); }
        .modal-note { font-size: 0.82rem; color: var(--text-muted); font-style: italic; margin-top: 18px; padding-top: 18px; border-top: 1px solid var(--border); }
        /* RESPONSIVE */
        @media (max-width: 768px) {
            header { padding: 56px 20px 48px; }
            .container { padding: 48px 20px; }
            section { margin-bottom: 56px; }
            .about-card { grid-template-columns: 1fr; padding: 28px 24px; gap: 28px; }
            .contact-grid { grid-template-columns: 1fr; }
            .modal-content { padding: 28px 20px; }
            .nav-links li:not(:last-child) { display: none; }
        }
        @media (max-width: 480px) {
            h1 { font-size: 1.7rem; }
            .services { grid-template-columns: 1fr; }
            .why-grid { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>
    <nav>
        <div class="nav-inner">
            <span class="nav-brand">&#x1F43E; Melissa's Pawsome Pet Care</span>
            <ul class="nav-links">
                <li><a href="#services">Services</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#contact" class="nav-cta">Book Now</a></li>
            </ul>
        </div>
    </nav>

    <header>
        <img src="logo.jpg" alt="Melissa's Pawsome Pet Care Logo">
        <div class="hero-badge">Pet Sitting &amp; Wellness Services</div>
        <h1>Melissa&#x2019;s Pawsome Pet Care</h1>
        <p class="tagline">Where every pet gets the love and attention they deserve.</p>
    </header>

    <div class="container">

        <section id="about">
            <p class="section-label">About</p>
            <h2>Genuine care, right at home.</h2>
            <p class="section-desc">Professional, reliable pet sitting so your furry family members stay happy while you're away.</p>
            <div class="about-card">
                <div class="about-text">
                    <p>Welcome to Melissa's Pawsome Pet Care! With years of hands-on experience and a genuine love for animals, Melissa provides caring, reliable pet sitting across the local area.</p>
                    <p>Whether it's a weekend getaway or an extended vacation, your pets receive personalized attention, playtime, meals, and all the love they deserve &mdash; peace of mind for you, happiness for them.</p>
                </div>
                <div class="about-stats">
                    <div class="stat"><div class="stat-number">7+</div><div class="stat-label">Years of experience</div></div>
                    <div class="stat"><div class="stat-number">4</div><div class="stat-label">Pet types cared for</div></div>
                    <div class="stat"><div class="stat-number">100%</div><div class="stat-label">In-home pet sitting</div></div>
                    <div class="stat"><div class="stat-number">&#x2728;</div><div class="stat-label">Reiki certified</div></div>
                </div>
            </div>
        </section>

        <section id="services">
            <p class="section-label">Services</p>
            <h2>Everything your pet needs.</h2>
            <p class="section-desc">Click any card to see what's included.</p>
            <div class="services">
                <div class="service-item" onclick="openModal('dog')">
                    <div class="service-chip">&#x1F415;</div>
                    <h3>Dog Care</h3>
                    <p>Walks, playtime, feeding, and lots of belly rubs for your canine companion.</p>
                    <span class="service-link">Learn more</span>
                </div>
                <div class="service-item" onclick="openModal('cat')">
                    <div class="service-chip">&#x1F408;</div>
                    <h3>Cat Care</h3>
                    <p>Feeding, litter maintenance, cuddles, and playtime for your feline friend.</p>
                    <span class="service-link">Learn more</span>
                </div>
                <div class="service-item" onclick="openModal('fish')">
                    <div class="service-chip">&#x1F420;</div>
                    <h3>Fish Care</h3>
                    <p>Feeding and tank maintenance to keep your aquatic family healthy.</p>
                    <span class="service-link">Learn more</span>
                </div>
                <div class="service-item" onclick="openModal('bunny')">
                    <div class="service-chip">&#x1F430;</div>
                    <h3>Bunny Care</h3>
                    <p>Feeding, cage cleaning, and gentle care for your hopping companion.</p>
                    <span class="service-link">Learn more</span>
                </div>
                <div class="service-item" onclick="openModal('reiki')">
                    <div class="service-chip">&#x1F9D8;</div>
                    <h3>Animal Reiki</h3>
                    <p>Gentle energy healing to promote relaxation and support your pet's wellbeing.</p>
                    <span class="service-link">Learn more</span>
                </div>
                <div class="service-item" onclick="openModal('communication')">
                    <div class="service-chip">&#x1F4AC;</div>
                    <h3>Animal Communication</h3>
                    <p>Intuitive connection to understand your pet's thoughts, feelings, and needs.</p>
                    <span class="service-link">Learn more</span>
                </div>
                <div class="service-item" onclick="openModal('walking')">
                    <div class="service-chip">&#x1F6B6;</div>
                    <h3>Dog Walking</h3>
                    <p>Professional walks to keep your pup happy, healthy, and well-exercised.</p>
                    <span class="service-link">Learn more</span>
                </div>
            </div>
        </section>

        <section>
            <div class="notice-card">
                <h3>&#x26A0;&#xFE0F;&nbsp; Important Safety Requirements</h3>
                <ul class="notice-list">
                    <li>Pets must be up-to-date on all vaccinations, including rabies</li>
                    <li>Pets with contagious illnesses or diseases cannot be accepted</li>
                    <li>Dogs must be properly socialized and comfortable with strangers</li>
                </ul>
                <p class="notice-footnote">Health records may be requested to ensure the safety of all animals in our care.</p>
            </div>
        </section>

        <section>
            <p class="section-label">Why us</p>
            <h2>The care your pet deserves.</h2>
            <p class="section-desc">A few reasons families trust Melissa with their beloved pets.</p>
            <ul class="why-grid">
                <li>Experienced and trustworthy pet care professional</li>
                <li>Personalized attention for each individual pet</li>
                <li>Regular photo updates while you're away</li>
                <li>Flexible scheduling to meet your needs</li>
                <li>Transparent, affordable pricing with no hidden fees</li>
                <li>Your pets stay comfortable in their own home</li>
                <li>Certified in Animal Reiki and Communication</li>
            </ul>
        </section>

        <div class="cta-wrap">
            <a href="#contact" class="cta-button">Get in touch today</a>
        </div>

        <section id="contact">
            <p class="section-label">Contact</p>
            <h2>Ready to book?</h2>
            <p class="section-desc">Reach out and let's find the perfect care plan for your pet.</p>
            <div class="contact-grid">
                <div class="contact-item">
                    <div class="contact-icon">&#x1F4E7;</div>
                    <div>
                        <div class="contact-label">Email</div>
                        <div class="contact-value">Melissaspawsomepetcare@gmail.com</div>
                    </div>
                </div>
                <div class="contact-item">
                    <div class="contact-icon">&#x1F4F1;</div>
                    <div>
                        <div class="contact-label">Phone</div>
                        <div class="contact-value">(720) 527-9291</div>
                    </div>
                </div>
                <div class="contact-item">
                    <div class="contact-icon">&#x1F4CD;</div>
                    <div>
                        <div class="contact-label">Location</div>
                        <div class="contact-value">Serving the local area with love and care</div>
                    </div>
                </div>
                <div class="contact-item">
                    <div class="contact-icon">&#x1F310;</div>
                    <div>
                        <div class="contact-label">Website</div>
                        <div class="contact-value">www.mppc.com</div>
                    </div>
                </div>
            </div>
        </section>

    </div>

    <footer>
        <div class="footer-inner">
            <p class="footer-brand">&#x1F43E; Melissa's Pawsome Pet Care</p>
            <p>&copy; 2025 &mdash; Where pets are family.</p>
        </div>
    </footer>

    <!-- Dog Modal -->
    <div id="dogModal" class="modal" onclick="closeModalOnBackground(event,'dog')">
        <div class="modal-content" onclick="event.stopPropagation()">
            <button class="close" onclick="closeModal('dog')">&times;</button>
            <div class="modal-icon">&#x1F415;</div>
            <h2 class="modal-title">Dog Care</h2>
            <p class="modal-subtitle">Your dog deserves the best care while you're away.</p>
            <div class="modal-body">
                <p class="modal-section-title">What's included</p>
                <ul>
                    <li><strong>Daily Walks</strong> &mdash; Exercise tailored to your dog's energy level and age</li>
                    <li><strong>Interactive Playtime</strong> &mdash; Engaging activities to keep them mentally stimulated</li>
                    <li><strong>Feeding Schedule</strong> &mdash; Strict adherence to your dog's diet and meal times</li>
                    <li><strong>Medication Administration</strong> &mdash; On-time meds if needed</li>
                    <li><strong>Cuddles &amp; Companionship</strong> &mdash; Belly rubs throughout the day</li>
                    <li><strong>Photo Updates</strong> &mdash; Daily pictures so you can see them having fun</li>
                    <li><strong>Home Security</strong> &mdash; Mail collection and light adjustments</li>
                </ul>
                <p class="modal-note">Only friendly, socialized dogs without aggressive behaviors are accepted.</p>
            </div>
        </div>
    </div>

    <!-- Cat Modal -->
    <div id="catModal" class="modal" onclick="closeModalOnBackground(event,'cat')">
        <div class="modal-content" onclick="event.stopPropagation()">
            <button class="close" onclick="closeModal('cat')">&times;</button>
            <div class="modal-icon">&#x1F408;</div>
            <h2 class="modal-title">Cat Care</h2>
            <p class="modal-subtitle">Your feline friend will be purr-fectly happy.</p>
            <div class="modal-body">
                <p class="modal-section-title">What's included</p>
                <ul>
                    <li><strong>Fresh Food &amp; Water</strong> &mdash; Daily feeding per your cat's schedule</li>
                    <li><strong>Litter Box Maintenance</strong> &mdash; Daily cleaning for a fresh, hygienic space</li>
                    <li><strong>Playtime Sessions</strong> &mdash; Interactive play to keep them active</li>
                    <li><strong>Cuddles &amp; Affection</strong> &mdash; Gentle petting and lap time for social cats</li>
                    <li><strong>Plant Watering</strong> &mdash; We'll care for your plants too</li>
                    <li><strong>Photo Updates</strong> &mdash; Regular pictures of your kitty's day</li>
                    <li><strong>Home Care</strong> &mdash; Mail collection and light adjustments</li>
                </ul>
                <p class="modal-note">We respect each cat's personality, whether social butterfly or quiet observer.</p>
            </div>
        </div>
    </div>

    <!-- Fish Modal -->
    <div id="fishModal" class="modal" onclick="closeModalOnBackground(event,'fish')">
        <div class="modal-content" onclick="event.stopPropagation()">
            <button class="close" onclick="closeModal('fish')">&times;</button>
            <div class="modal-icon">&#x1F420;</div>
            <h2 class="modal-title">Fish Care</h2>
            <p class="modal-subtitle">Your aquatic world will stay healthy and vibrant.</p>
            <div class="modal-body">
                <p class="modal-section-title">What's included</p>
                <ul>
                    <li><strong>Daily Feeding</strong> &mdash; Proper portions at the right times</li>
                    <li><strong>Water Quality Checks</strong> &mdash; Monitoring temperature and conditions</li>
                    <li><strong>Tank Maintenance</strong> &mdash; Cleaning filters and removing debris</li>
                    <li><strong>Health Monitoring</strong> &mdash; Observing fish behavior and alerting you to concerns</li>
                    <li><strong>Equipment Checks</strong> &mdash; Ensuring filters, heaters, and lights work properly</li>
                    <li><strong>Detailed Reports</strong> &mdash; Notes on feeding, water quality, and activity</li>
                    <li><strong>Emergency Response</strong> &mdash; Quick action if equipment issues arise</li>
                </ul>
                <p class="modal-note">Goldfish, tropical, or saltwater reef &mdash; we follow your specific instructions.</p>
            </div>
        </div>
    </div>

    <!-- Bunny Modal -->
    <div id="bunnyModal" class="modal" onclick="closeModalOnBackground(event,'bunny')">
        <div class="modal-content" onclick="event.stopPropagation()">
            <button class="close" onclick="closeModal('bunny')">&times;</button>
            <div class="modal-icon">&#x1F430;</div>
            <h2 class="modal-title">Bunny Care</h2>
            <p class="modal-subtitle">Gentle, attentive care for your hopping companion.</p>
            <div class="modal-body">
                <p class="modal-section-title">What's included</p>
                <ul>
                    <li><strong>Fresh Food Daily</strong> &mdash; Hay, vegetables, and pellets per your bunny's diet</li>
                    <li><strong>Fresh Water</strong> &mdash; Daily water changes to keep them hydrated</li>
                    <li><strong>Cage Cleaning</strong> &mdash; Regular cleaning of living space and litter area</li>
                    <li><strong>Exercise Time</strong> &mdash; Safe supervised hopping time outside the cage</li>
                    <li><strong>Gentle Handling</strong> &mdash; Careful petting and interaction for social bunnies</li>
                    <li><strong>Health Checks</strong> &mdash; Monitoring eating habits and overall wellbeing</li>
                    <li><strong>Environmental Care</strong> &mdash; Maintaining proper temperature and safe surroundings</li>
                </ul>
                <p class="modal-note">We understand bunny behavior to provide respectful, sensitive care.</p>
            </div>
        </div>
    </div>

    <!-- Reiki Modal -->
    <div id="reikiModal" class="modal" onclick="closeModalOnBackground(event,'reiki')">
        <div class="modal-content" onclick="event.stopPropagation()">
            <button class="close" onclick="closeModal('reiki')">&times;</button>
            <div class="modal-icon">&#x1F9D8;</div>
            <h2 class="modal-title">Animal Reiki</h2>
            <p class="modal-subtitle">Gentle energy healing to calm, balance, and support your pet.</p>
            <div class="modal-body">
                <p class="modal-section-title">Benefits</p>
                <ul>
                    <li><strong>Stress &amp; Anxiety Relief</strong> &mdash; Helps calm nervous or anxious pets</li>
                    <li><strong>Recovery Support</strong> &mdash; Promotes healing after surgery or illness</li>
                    <li><strong>Pain Management</strong> &mdash; Can help ease discomfort and chronic pain</li>
                    <li><strong>Emotional Balance</strong> &mdash; Supports wellbeing and behavioral issues</li>
                    <li><strong>Enhanced Vitality</strong> &mdash; Boosts overall energy and immune function</li>
                    <li><strong>Deepened Bond</strong> &mdash; Strengthens the connection between you and your pet</li>
                    <li><strong>End-of-Life Comfort</strong> &mdash; Peace and comfort for senior or hospice pets</li>
                </ul>
                <p class="modal-section-title">What to expect</p>
                <p style="font-size:0.875rem;color:var(--text-muted);line-height:1.6;margin-bottom:0">Sessions are gentle and respect your pet's boundaries. Most animals naturally relax and may even fall asleep. Can be done hands-on or from a distance.</p>
                <p class="modal-note">Suitable for all animals &mdash; dogs, cats, horses, rabbits, birds, and more.</p>
            </div>
        </div>
    </div>

    <!-- Communication Modal -->
    <div id="communicationModal" class="modal" onclick="closeModalOnBackground(event,'communication')">
        <div class="modal-content" onclick="event.stopPropagation()">
            <button class="close" onclick="closeModal('communication')">&times;</button>
            <div class="modal-icon">&#x1F4AC;</div>
            <h2 class="modal-title">Animal Communication</h2>
            <p class="modal-subtitle">Understand what your pet is really thinking and feeling.</p>
            <div class="modal-body">
                <p class="modal-section-title">How it can help</p>
                <ul>
                    <li><strong>Behavioral Understanding</strong> &mdash; Discover the reasons behind certain behaviors</li>
                    <li><strong>Address Fears &amp; Anxieties</strong> &mdash; Learn what's troubling your pet</li>
                    <li><strong>Health Insights</strong> &mdash; Gain awareness of physical discomfort or pain</li>
                    <li><strong>Life Changes</strong> &mdash; Help pets adjust to moves or new family members</li>
                    <li><strong>Deepen Your Bond</strong> &mdash; Better understand your pet's preferences</li>
                    <li><strong>Lost Pets</strong> &mdash; Connect with lost animals to help locate them</li>
                    <li><strong>After-Life Connection</strong> &mdash; Communicate with pets who have passed</li>
                </ul>
                <p class="modal-section-title">What you'll receive</p>
                <p style="font-size:0.875rem;color:var(--text-muted);line-height:1.6;margin-bottom:0">A detailed session report including messages from your pet. Available in-person or remotely with a photo.</p>
                <p class="modal-note">Animal communication complements veterinary care but does not replace professional medical diagnosis.</p>
            </div>
        </div>
    </div>

    <!-- Walking Modal -->
    <div id="walkingModal" class="modal" onclick="closeModalOnBackground(event,'walking')">
        <div class="modal-content" onclick="event.stopPropagation()">
            <button class="close" onclick="closeModal('walking')">&times;</button>
            <div class="modal-icon">&#x1F6B6;</div>
            <h2 class="modal-title">Dog Walking</h2>
            <p class="modal-subtitle">Keep your pup happy, healthy, and well-exercised.</p>
            <div class="modal-body">
                <p class="modal-section-title">What's included</p>
                <ul>
                    <li><strong>Personalized Walks</strong> &mdash; Pacing and routes suited to your dog</li>
                    <li><strong>Flexible Scheduling</strong> &mdash; Morning, afternoon, or evening</li>
                    <li><strong>Fresh Water Breaks</strong> &mdash; Hydration during longer walks</li>
                    <li><strong>Photo Updates</strong> &mdash; Pictures during the walk</li>
                    <li><strong>Clean-Up Service</strong> &mdash; We always clean up after your dog</li>
                    <li><strong>Leash Manners Reinforcement</strong> &mdash; Positive reinforcement of good behavior</li>
                </ul>
                <p class="modal-section-title">Walk options</p>
                <ul>
                    <li><strong>Quick Potty Break</strong> &mdash; 15&ndash;20 minutes</li>
                    <li><strong>Standard Walk</strong> &mdash; 30 minutes</li>
                    <li><strong>Extended Walk</strong> &mdash; 45&ndash;60 minute adventure</li>
                    <li><strong>Regular Schedule</strong> &mdash; Daily, weekly, or custom</li>
                </ul>
                <p class="modal-note">Perfect for busy schedules, high-energy dogs, or anyone wanting to give their pup extra outdoor time.</p>
            </div>
        </div>
    </div>

    <script>
        function openModal(type) {
            document.getElementById(type + 'Modal').classList.add('open');
            document.body.style.overflow = 'hidden';
        }
        function closeModal(type) {
            document.getElementById(type + 'Modal').classList.remove('open');
            document.body.style.overflow = '';
        }
        function closeModalOnBackground(event, type) {
            if (event.target.classList.contains('modal')) closeModal(type);
        }
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') {
                document.querySelectorAll('.modal.open').forEach(function(m) {
                    m.classList.remove('open');
                });
                document.body.style.overflow = '';
            }
        });
        document.querySelectorAll('a[href^="#"]').forEach(function(a) {
            a.addEventListener('click', function(e) {
                e.preventDefault();
                var t = document.querySelector(this.getAttribute('href'));
                if (t) t.scrollIntoView({ behavior: 'smooth', block: 'start' });
            });
        });
    </script>
</body>
</html>"""

with open('/Users/jestrella/Desktop/melissa/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Written', len(html), 'bytes')
