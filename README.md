# ADVANCED-PORTFOLIO-INTERFACE
🚀 Interactive portfolio builder with Next.js, Flask &amp; SQLite — features live admin dashboard, JWT auth, AI chatbot, custom cursor, neon animations, and full content management (projects, skills, bio, uploads). Dark/light themes + recruiter mode.

✦ Interactive Portfolio — Full Stack
A cinematic, fully customizable developer portfolio with neon cursor effects, animated sections, an AI chatbot, and a complete admin panel to manage all content without touching code.

✨ Features

Neon Cursor System — 12 elastic strands with spring physics, mouse attraction, fading trails, and color-burst on click
Hero Section — typewriter effect, staggered fade-up animations, particle + gradient background
About, Projects, Skills, Contact — scroll-triggered animations, project preview modals, animated skill bars
Settings Panel — switch accent colors, dark/light mode, recruiter/showcase mode, animation speed
AI Chatbot — powered by Claude (Anthropic), answers questions about your skills and projects
Admin Dashboard — full CRUD for profile, projects, skills, stats, and traits — no code changes needed
Animated Login Page — JWT auth, matches the portfolio's theme and animations
SQLite Database — zero-config, file-based storage; swap to PostgreSQL for production

## 🛠️ Tech Stack

| Layer            | Technologies Used |
|------------------|------------------|
| **Frontend**     | Next.js 14, TypeScript, Tailwind CSS |
| **Animations**   | Canvas API, requestAnimationFrame, CSS Transitions |
| **Backend**      | Flask (Python), SQLAlchemy, Flask-Bcrypt |
| **Database**     | SQLite (Development), PostgreSQL (Production) |
| **Authentication** | JWT (PyJWT) |
| **AI Integration** | Anthropic Claude API |
| **Deployment**   | Vercel (Frontend), Railway / Render (Backend) |

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/portfolio-app.git
cd portfolio-app
```

---

## 💻 Frontend Setup

```bash
cd frontend
npm install
```

Create a `.env.local` file inside `frontend/`:

```env
ANTHROPIC_API_KEY=sk-ant-your-key-here
NEXT_PUBLIC_API_URL=http://localhost:5000
```

Run the development server:

```bash
npm run dev
```

Frontend runs on:

```txt
http://localhost:3000
```

---

## ⚙️ Backend Setup

```bash
cd backend
python -m venv venv
```

Activate virtual environment:

### Windows
```bash
venv\Scripts\activate
```

### macOS / Linux
```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file inside `backend/`:

```env
JWT_SECRET=your-random-secret-string
ADMIN_PASSWORD=your-secure-password
```

Start the Flask server:

```bash
python app.py
```

Backend runs on:

```txt
http://localhost:5000
```

---

# 🌐 Application Routes

| URL | Purpose |
|---|---|
| `http://localhost:3000` | Public Portfolio |
| `http://localhost:3000/admin/login` | Admin Login |
| `http://localhost:3000/admin/dashboard` | Admin Dashboard |
| `http://localhost:5000` | Flask API |

### 🔐 Default Admin Credentials

```txt
Username: admin
Password: admin123
```

> Change credentials immediately inside the `.env` file for security.

---

# ✨ Features

- 🎨 Interactive neon cursor animation
- ⚡ Smooth motion physics & magnetic hover effects
- 🤖 AI-powered chatbot using Claude API
- 🔐 JWT Authentication System
- 📁 Dynamic admin dashboard CMS
- 🌙 Dark / Light / Custom themes
- 📱 Fully responsive modern UI
- 🧠 Real-time portfolio content updates
- 🚀 Recruiter Mode for minimal distraction
- 📂 Resume upload & project image management

---

# 🎨 Customization

Everything is editable directly from the Admin Dashboard:

## 👤 Profile
- Name
- Title
- Bio
- Tagline
- Availability
- Resume
- Profile Photo

## 📂 Projects
- Add / Edit / Delete Projects
- GitHub & Live Links
- Tags & Technologies
- Custom Accent Colors
- Project Images

## 🛠 Skills
- Dynamic proficiency sliders
- Skill grouping & ordering

## 📊 Stats
- Experience
- Projects Count
- Certifications
- Achievements

## 💫 Traits
- Personality pills
- Developer specialties
- Interests

Changes appear instantly without redeployment.

---

# 🌈 Cursor & Theme System

### 🎆 Interactive Cursor Effects
- Click anywhere to trigger neon color bursts
- Physics-based cursor trails
- Dynamic strand rendering using Canvas API

### ⚙️ Theme Controls
Users can customize:

- Accent Colors
- Fonts
- Background Style
- Animation Speed
- Cursor Intensity
- UI Themes

### 🧹 Recruiter Mode
A distraction-free experience that:
- Removes heavy animations
- Simplifies UI
- Improves readability & performance

---

# 🧠 AI Chatbot

Integrated Claude AI assistant capable of:

- Answering recruiter questions
- Explaining projects
- Discussing skills & experience
- Providing resume information
- Interactive portfolio navigation

Powered by the Anthropic Claude API.

---

# 📁 Project Structure

```txt
portfolio-app/
├── frontend/
│   ├── app/
│   │   ├── page.tsx
│   │   ├── admin/
│   │   │   ├── login/page.tsx
│   │   │   └── dashboard/page.tsx
│   │   └── api/chat/route.ts
│   │
│   ├── components/
│   │   ├── cursor/
│   │   ├── sections/
│   │   ├── ui/
│   │   └── chatbot/
│   │
│   ├── context/
│   │   ├── ThemeContext.tsx
│   │
│   ├── hooks/
│   │   └── useCursor.ts
│   │
│   ├── lib/
│   │   └── auth.ts
│   │
│   └── middleware.ts
│
└── backend/
    ├── app.py
    ├── database.py
    │
    ├── models/
    │   ├── user.py
    │   └── portfolio_db.py
    │
    └── routes/
        ├── auth.py
        ├── admin.py
        ├── portfolio.py
        ├── upload.py
        └── contact.py
```

---

# 🛠️ Tech Stack

| Category | Stack |
|---|---|
| **Frontend** | Next.js 14 • TypeScript • Tailwind CSS |
| **Animations** | Canvas API • requestAnimationFrame • CSS Transitions |
| **Backend** | Flask • SQLAlchemy • Flask-Bcrypt |
| **Database** | SQLite (Dev) • PostgreSQL (Prod) |
| **Authentication** | JWT (PyJWT) |
| **AI** | Anthropic Claude API |
| **Deployment** | Vercel • Railway / Render |

---

# 🚢 Deployment

## Frontend Deployment — Vercel

Deploy the Next.js frontend using Vercel:

```bash
cd frontend
vercel --prod
```

### Required Environment Variables

Add the following variables in the Vercel dashboard:

```env
ANTHROPIC_API_KEY=your-api-key
NEXT_PUBLIC_API_URL=https://your-backend-url.com
```

---

## Backend Deployment — Railway / Render

### Steps

1. Push the project to GitHub
2. Connect the repository to Railway or Render
3. Add environment variables
4. Deploy the Flask backend

### Required Environment Variables

```env
JWT_SECRET=your-secret-key
ADMIN_PASSWORD=your-secure-password
DATABASE_URL=your-production-database-url
```

Railway / Render will automatically detect Python and start the Flask application.

---

# 🗄️ Production Database Setup

For development, SQLite is used by default.

For production deployment, switch to PostgreSQL.

Update `database.py`:

```python
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL",
    "sqlite:///portfolio.db"
)
```

This allows:
- SQLite for local development
- PostgreSQL automatically in production

---

# ✅ Recommended Production Stack

| Service | Platform |
|---|---|
| Frontend | Vercel |
| Backend API | Railway / Render |
| Database | PostgreSQL |
| File Hosting | Cloudinary / UploadThing (Optional) |

---

# 🔐 Production Checklist

- Change default admin credentials
- Use strong JWT secrets
- Enable HTTPS
- Add CORS restrictions
- Store secrets in environment variables only
- Enable PostgreSQL backups
- Optimize image uploads

---

# ⚡ Recommended Build Commands

## Frontend

```bash
npm run build
```

## Backend

```bash
pip install -r requirements.txt
python app.py
```
