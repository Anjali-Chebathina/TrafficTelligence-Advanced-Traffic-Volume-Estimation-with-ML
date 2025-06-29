## 📝 Frontend Templates

This project uses **Flask Jinja templates** for its frontend UI, consisting of two main HTML files:

---

### 📄 `index.html`

- **Purpose:**  
  Serves as the home page with a clean, user-friendly form for entering input features required by the traffic volume prediction model.

- **Features:**  
  - Dropdowns for categorical inputs (e.g. holiday, weather)
  - Numeric input fields with validation limits (e.g. temperature, rain, snow, date, time)
  - Styled layout with background image (`bg.png`)
  - Submit button to POST data to `/predict` route

- **Sample Code Snippet:**

### output.html
 -**Purpose:**
    Displays the predicted traffic volume output in an attractive, animated format to enhance user experience.

-**Features:**

   -Uses Jinja templating to insert the prediction_text returned by Flask
  -Includes CSS animations for smooth result display
   -Consistent styling with index.html for visual continuity

