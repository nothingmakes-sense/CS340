## CS 340 Project Two Reflection  
**Grazioso Salvare Dashboard**  

### How do you write programs that are maintainable, readable, and adaptable?

I write maintainable, readable, and adaptable programs by following the principles of **separation of concerns** and **modular design**. In Project One I created a dedicated `AnimalShelter` class that encapsulated all MongoDB connection logic, create/read/update/delete operations, and error handling. This module was then imported and reused in Project Two without any changes.

**Advantages of this approach:**
- The dashboard code stayed clean and focused only on the user interface (Dash layout and callbacks).
- Any future changes to the database (new fields, different queries, or even switching to a different NoSQL database) only require updates in one file (`animal_shelter.py`).
- The code is highly readable because each component has a single responsibility.
- It is easily adaptable — the same CRUD module could be reused for a mobile app, a command-line tool, or another client dashboard.

In the future I could use this CRUD module for any application that needs to interact with the Austin Animal Center data, such as a mobile search-and-rescue app, an automated reporting system, or even a machine-learning model that predicts optimal training candidates.

### How do you approach a problem as a computer scientist?

As a computer scientist I approach every problem by first **understanding the client’s requirements** and then breaking the solution into manageable, testable pieces. For this project I started by carefully reading the Dashboard Specifications Document, paying special attention to the required widgets, the exact filter criteria (rescue type, preferred breeds, sex, and age range in weeks), and the branding requirements.

I used an **MVC** pattern:
- **Model** — MongoDB + the CRUD module from Project One
- **View** — Dash layout (logo, radio buttons, data table, pie chart, geolocation map)
- **Controller** — callback functions that respond to user filter selections and update the widgets in real time

This project differed from previous assignments because it was truly **full-stack**: I had to integrate a database, write secure queries, build an interactive web interface, and ensure everything updated dynamically. Earlier courses often focused on only one layer (just Python scripts or just database design).  

In the future, when creating databases for other clients, I will continue to:
1. Gather precise requirements first (especially any business rules like the rescue-type table).
2. Design modular, reusable components (CRUD classes).
3. Use frameworks like Dash/Plotly for rapid interactive visualization.
4. Test each filter and widget individually before combining them.

### What do computer scientists do, and why does it matter?

Computer scientists solve real-world problems by turning raw data into actionable information. In this project I built a dashboard that allows Grazioso Salvare staff to instantly filter thousands of shelter records and visualize only the dogs that match their exact search-and-rescue criteria (breed, sex, age, location).  

Instead of manually scanning spreadsheets, staff can now:
- Click one button to see all suitable Water Rescue dogs
- View a pie chart of breed distribution
- Click any row to see the dog’s location on an interactive map

This directly helps Grazioso Salvare **save time, reduce errors, and rescue more animals** faster. The work matters because it demonstrates how software can turn data into life-saving decisions — exactly the kind of meaningful impact I want my career in computer science to have.

---

**Repository Link:** (https://github.com/nothingmakes-sense/CS340)
**Artifacts Included:** `ProjectTwoDashboard.ipynb`, `CRUD_Python_Module.py`, Dashboard Video
