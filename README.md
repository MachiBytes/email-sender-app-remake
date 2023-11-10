## Email Sender App Remake 
---

### Directory Structure
1. email-assets/    <-- Contains the email assets used for the email template
2. src/  <-- Contains the whole app functionality and logic
3. templates/  <-- Contains the base.csv and email-template.html


### How to run the email sender app remake

1. Create a Python Virtual Environment and Activate it

```bash
python -m venv .venv

source .venv/Scripts/activate
```

2. Install required packages
```bash
pip install -r requirements.txt
```

3. Run the App
```bash
python -B main.py
```

### Email Sender Preview
Before sending emails to a large audience, you can test the email sender to ensure everything works smoothly. Simply follow these steps:

1. Open `email_processing.py` located at `src/logic/email_processing.py`.

2. Navigate to line 34 in the script.

3. Modify the value of "recipient" from `data['email']` to your own email address.

   ```python
   # Before
   "recipient": data['email']

   # After
   "recipient": 'your_email@example.com'
   ```

Sending Emails since Alf 
૮꒰˶ᵔ ᗜ ᵔ˶ ꒱ა