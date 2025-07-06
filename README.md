# 🌍 LinguaFlow - Modern Language Translator

A beautiful, modern language translation web application built with Flask and advanced AI translation APIs.

## ✨ Features

- **Modern Dark UI**: Sleek dark blue theme with glassmorphism effects
- **13 Languages**: Support for English, Spanish, French, German, Italian, Portuguese, Russian, Japanese, Korean, Chinese, Hindi, Tamil, and Arabic
- **Real-time Translation**: Powered by Google Translate and LibreTranslate APIs
- **Responsive Design**: Works perfectly on desktop and mobile devices
- **Smart Features**: 
  - Character counter with visual feedback
  - Language swap functionality
  - Copy translation to clipboard
  - Loading animations and notifications
  - Keyboard shortcuts (Ctrl+Enter to translate)

## 🚀 Live Demo

[Deploy your own instance on Render](#deployment)

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Translation APIs**: Google Translate, LibreTranslate
- **Styling**: Modern CSS with animations and transitions
- **Icons**: Font Awesome
- **Fonts**: Inter (Google Fonts)

## 📦 Installation

### Prerequisites
- Python 3.7+
- pip

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/language-translator.git
   cd language-translator
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:5000`

## 🌐 Deployment

### Render (Recommended)

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy on Render**
   - Go to [render.com](https://render.com)
   - Sign up/Login with GitHub
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Configure:
     - **Name**: `language-translator`
     - **Environment**: `Python 3`
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:app`
   - Click "Create Web Service"

3. **Your app will be live at**: `https://your-app-name.onrender.com`

## 📁 Project Structure

```
language_translator_flask/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Procfile              # Heroku deployment config
├── .gitignore           # Git ignore rules
├── README.md            # Project documentation
├── static/
│   └── style.css        # Modern CSS styles
└── templates/
    └── index.html       # Main HTML template
```

## 🎨 Customization

### Adding New Languages

1. **Update HTML**: Add language options in `templates/index.html`
2. **Update Backend**: Add language codes in `app.py`

### Changing Theme

Modify colors in `static/style.css`:
- Primary blue: `#3b82f6`
- Background: `#0f172a` to `#64748b`
- Text: `#f1f5f9`

## 🔧 API Configuration

The app uses two translation services:
- **Primary**: Google Translate (free tier)
- **Fallback**: LibreTranslate

No API keys required - both services are free to use.

## 📱 Browser Support

- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Google Translate API
- LibreTranslate
- Font Awesome for icons
- Inter font family

---

**Made with ❤️ using Flask and modern web technologies**
