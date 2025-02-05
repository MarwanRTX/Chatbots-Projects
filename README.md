# ChatBot :sparkles:

![NeonShopBot Demo](https://raw.githubusercontent.com/MarwanRTX/Chatbots-Projects/main/chatbotgif.gif)
*A dynamic chatbot interface for modern businesses*

## 🚀 Features
- **Neon Cyberpunk UI** with animated elements
- **JSON-powered menu system** for easy updates
- Real-time conversation interface
- Multi-type response handling (lists, key-value, text)
- Floating chat widget with smooth animations
- Mobile-responsive design
- Easy integration with external APIs

## 📸 Screenshots
| Menu Interface | Response Display |
|----------------|------------------|
| ![Menu](https://raw.githubusercontent.com/MarwanRTX/Chatbots-Projects/main/chat.png) | ![Response](https://raw.githubusercontent.com/MarwanRTX/Chatbots-Projects/main/chat3.png) |

## ⚙️ Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/NeonShopBot.git
cd NeonShopBot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Flask application:
```bash
python app.py
```

## 🔧 Configuration
1. Edit `app.py` to modify the JSON data source:
```python
url = "https://your-json-data-source.json"
```

2. Customize the UI in `templates/index.html`:
```css
:root {
    --neon-blue: #00f3ff;  /* Change accent colors */
    --neon-purple: #bc13fe;
    --dark-bg: #0a0e17;
}
```

## 📋 Usage
1. Access the chatbot at `http://localhost:5000`
2. Click the floating neon button 💬
3. Select menu options:
   - **Fruits Menu**: Displays available fruits and prices
   - **Available Places**: Shows store locations
   - **Special Offers**: Lists current promotions
   - **Contact Info**: Provides contact details

## 🌐 JSON Data Structure
```json
{
    "Category Name": ["Item 1", "Item 2"],
    "Contact Info": {
        "Phone": "123-456-7890",
        "Email": "contact@store.com"
    },
    "Special Offers": ["Offer 1", "Offer 2"]
}
```

## 📚 Documentation
| Component       | Purpose                          | File                 |
|-----------------|----------------------------------|----------------------|
| Flask Backend   | Data handling and routing        | `app.py`             |
| Neon UI         | Chat interface and animations    | `templates/index.html` |
| Style Config    | Color schemes and layout         | `<style>` in HTML    |

## 🤝 Contributing
1. Fork the project
2. Create your feature branch:
```bash
git checkout -b feature/AmazingFeature
```
3. Commit your changes:
```bash
git commit -m 'Add some AmazingFeature'
```
4. Push to the branch:
```bash
git push origin feature/AmazingFeature
```
5. Open a Pull Request

## ✉️ Contact
Marwan - (https://www.linkedin.com/in/marwan-mostafa-712192212/) - marwan.d.2008@gmail.com

Project Link: [https://github.com/MarwanRTX/Chatbots-Projects](https://github.com/yourusername/NeonShopBot)
