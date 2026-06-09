╔══════════════════════════════════════════════════════╗
║           YOUR PORTFOLIO — SETUP GUIDE               ║
╚══════════════════════════════════════════════════════╝

📁 FOLDER STRUCTURE
───────────────────
portfolio/
├── index.html        ← Your main portfolio file (open this!)
├── images/           ← Put all your images here
│   ├── profile.jpg       → Your profile / headshot photo
│   ├── about.jpg         → Casual or ID photo for About section
│   ├── project1.png      → Screenshot of Smart Home Monitor
│   ├── project2.png      → Screenshot of Campus Network Setup
│   ├── project3.png      → Screenshot of Student Portal System
│   └── project4.png      → Screenshot of PC Maintenance Tracker
└── README.txt        ← This file


📸 HOW TO ADD IMAGES (2 ways)
───────────────────────────────

OPTION A — Click to Upload (easiest, no code needed):
  1. Open index.html in your browser
  2. Click any green dashed box (the image placeholders)
  3. Pick your photo from your computer
  4. Done! The image shows up instantly.
  NOTE: This only works while the browser is open.
        Images won't save permanently this way.

OPTION B — Edit the HTML (permanent, recommended):
  1. Put your images in the /images/ folder
  2. Open index.html in VS Code
  3. Find the placeholder you want to replace, e.g.:

     <!-- 📸 PROFILE PHOTO -->
     <div class="img-placeholder" ...>
       ...
     </div>

  4. Replace the whole <div class="img-placeholder">...</div>
     with a simple image tag:

     <img src="images/profile.jpg"
          alt="Your Name"
          style="width:220px;height:220px;object-fit:cover;border-radius:50%;border:2px solid rgba(0,255,180,0.4);" />

  5. For project screenshots use:

     <img src="images/project1.png"
          alt="Smart Home Monitor"
          style="width:100%;height:180px;object-fit:cover;" />


✏️  WHAT TO CUSTOMIZE
───────────────────────
  - "Your Name"          → Replace with your real name
  - yourname@email.com   → Your real email
  - github.com/yourname  → Your GitHub profile URL
  - linkedin.com/in/...  → Your LinkedIn URL
  - Project names/desc   → Update with your real projects
  - Skills               → Add or remove skill tags


🌐 HOW TO HOST IT FREE
────────────────────────
  GitHub Pages (recommended):
  1. Create a GitHub account
  2. New repo → name it: yourusername.github.io
  3. Upload the whole portfolio/ folder
  4. Go to Settings → Pages → Deploy from branch: main
  5. Your site is live at: https://yourusername.github.io

  Netlify (drag & drop):
  1. Go to netlify.com
  2. Drag the portfolio/ folder onto the page
  3. Done — live in 30 seconds!


💬 NEED HELP?
──────────────
  Ask Claude for any changes — adding sections,
  changing colors, updating content, etc.

══════════════════════════════════════════════════════
