# RC Medical Test Center

RC Medical Test Center has adeptly designed a Django web application, providing users with a versatile platform to explore the tests conducted within the center, discover information about the biologists overseeing them, and streamline the management of patient information for secretaries.


## Installation

Follow these steps to set up the RC Medical Test Center on your local machine:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/medical_test_center.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd medical_test_center
    ```

3. **Create a virtual environment using Anaconda:**

    ```bash
    conda create --name medical_test_env python=3.10.13
    ```

4. **Activate the virtual environment:**

    ```bash
    conda activate --name medical_test_env 
    ```

5. **Install project dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

6. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

7. **Run the development server:**

    ```bash
    python manage.py runserver
    ```
The `pip install -r requirements.txt` command installs all the dependencies listed in the `requirements.txt` file, which includes Django and other necessary libraries.

Visit `http://127.0.0.1:8000/` in your web browser to access the Medical Test Center.

## Usage

#### Homepage

Visit the homepage for a small description of the center, its precise location, and contact information.

#### Test Browser

Users can explore the tests performed in the center by navigating through the site.

#### Biologist Directory

Information about biologists is available for users to learn more about the professionals in the center.

#### Medical Patient Form (Secretary Access)

Secretaries can access the Medical Patient Form to add patient information to the center's record, and they can then view a list of all patients and their information.

#### Secretary Access (Login Credentials)

To access the secretary-only features, use the following login credentials:

- **cristel:** secretary_username
- **cris2001:** secretary_password


- **rafi:** secretary_username
- **Rafi.ch2000:** secretary_password


## License

This project is licensed under the [MIT License](LICENSE.md).

## Project Status

Development is ongoing. Feel free to contribute and help us improve!