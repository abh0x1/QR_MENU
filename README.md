# QR Code Generator for Menu 📱🍽️

This Django-based web app allows restaurants, cafes, or individuals to generate QR codes for menus, URLs, or any custom input. Users can enter their restaurant name or menu URL, and the app will generate a downloadable QR code.

---

## 🔧 Features

- ✅ Clean, responsive UI using Tailwind CSS
- ⚙️ Dynamic QR Code generation with high-quality images
- 📸 Instant QR preview
- 📥 Download QR as PNG
- 📂 Django-based form handling and templating
- 💾 Optionally stores generated QR codes (if configured)

---

## 🚀 Getting Started

Clone the repository and move into the folder:

```bash
git clone https://github.com/abh0x1/qr_menu.git
cd qr_menu

# Create and activate virtual environment
python -m venv env
env\Scripts\activate       # On Windows
# source env/bin/activate  # On Mac/Linux

# Install required packages
pip install -r requirements.txt

# Run migrations (even if not using models, keep it ready)
python manage.py makemigrations
python manage.py migrate

# Start the development server
python manage.py runserver
```

Now open your browser and go to : http://127.0.0.1:8000/
