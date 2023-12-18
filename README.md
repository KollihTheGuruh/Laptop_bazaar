<h1><strong>Laptop Bazaar</strong></h1>
<p>Laptop Bazaar is a web application designed to provide users with a seamless and personalized experience in finding, comparing, and purchasing laptops. Whether you are a tech-savvy shopper looking for specific specifications or a comparative buyer wanting to make an informed decision, Laptop Bazaar has you covered.</p>

<h2>Table of Contents</h2>
1. Features
2. Technology Stack
3. Installation
4. Usage
5. API Documentation
6. User Stories
7. Mockups
8. Contributing
9. License

<h2>Features</h2>
<h3>Laptop Selection:

Filter laptops by specifications such as RAM, processor type, and price.
Real-time updates as filter options are changed.
Intuitive and easily accessible filtering process.
Product Comparisons:

Select multiple laptops and compare their specs side by side.
Easy removal or addition of laptops from the comparison view.
Secure Checkout:

Encrypted checkout process complying with PCI-DSS standards.
Multiple payment options, including M-Pesa and PayPal.
Confirmation message with order details after payment processing.
Account Creation and Management:

User account creation for order management, order history, and preferences.
Save payment methods and addresses for faster future purchases.
Product Reviews and Ratings:

Read reviews and see ratings from other buyers.
Submit reviews with a rating out of five stars.
Technology Stack
Backend:

Django: Web framework for building robust web applications.
Django Rest Framework: Powerful toolkit for building Web APIs.
Frontend:

HTML, CSS, JavaScript: Frontend technologies for a responsive user interface.
Database:

SQLite: Lightweight and efficient relational database.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/KollihTheGuruh/laptop_bazaar.git
Navigate to the project directory:

bash
Copy code
cd laptop_bazaar
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run migrations:

bash
Copy code
python manage.py migrate
Create a superuser (for admin access):

bash
Copy code
python manage.py createsuperuser
Run the development server:

bash
Copy code
python manage.py runserver
Access the application at http://localhost:8000.

Usage
Access the admin panel at http://localhost:8000/admin using the superuser credentials created.
Explore the API documentation at http://localhost:8000/swagger for detailed information on available API routes and methods.
API Documentation
Explore the API Documentation for detailed information on available routes and methods.

User Stories
Laptop Selection
Product Comparisons
Secure Checkout
Account Creation and Management
Product Reviews and Ratings
Mockups
View the Mockups to get a visual representation of the user interface.

Contributing
Contributions are welcome! Please follow the Contributing Guidelines for a smooth collaboration.

License
This project is licensed under the MIT License.