# Google Cloud Day 2026 Conference Website

A premium, glassmorphism-styled informational website for the Google Cloud Day 2026 technical conference. Built with Flask and vanilla HTML/CSS/JS.

## Features
- **Responsive Design**: Premium glassmorphism aesthetic that works on all devices.
- **Dynamic Schedule**: View the day's agenda including talks, speakers, and breaks.
- **Real-time Search**: Filter talks by title, speaker, or category instantly.
- **Speaker Highlights**: Detailed speaker cards with LinkedIn integration.

## Project Structure
- `app.py`: Flask application server.
- `data.py`: Dummy data for speakers and events.
- `templates/index.html`: Main HTML template.
- `static/css/style.css`: Custom CSS with glassmorphism effects and animations.
- `static/js/script.js`: Client-side search logic.

## Setup & Running using Python

1.  **Install Requirements**
    Ensure you have Python installed. Install Flask if not already present:
    ```bash
    pip install flask
    ```

2.  **Run the Application**
    Execute the following command in the project root:
    ```bash
    python app.py
    ```

3.  **Access the Website**
    Open your browser and navigate to:
    [http://127.0.0.1:5000](http://127.0.0.1:5000/)

## Customization
- **Modify Data**: Edit `data.py` to change speakers, events, or conference details.
- **Styles**: Adjust colors and effects in `static/css/style.css`.
- **Search Logic**: Update filtering rules in `static/js/script.js`.
