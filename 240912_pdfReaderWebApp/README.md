# PDF Reader

A simple PDF reader web application built with Flask. This project demonstrates how to serve and display PDF files using a Python web application.

## Features

- Serve PDF files from a directory.
- Display PDF files in a web browser using an `<iframe>`.

## Prerequisites

- Python 3.x
- Flask

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/pdf_reader.git
   cd pdf_reader
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**

   ```bash
   pip install Flask
   ```

## Project Structure

- `app.py` – The main Flask application file.
- `templates/` – Directory containing HTML templates.
  - `index.html` – The main template file for displaying PDFs.
- `pdfs/` – Directory where PDF files are stored. Place your PDF files here.
- `README.md` – This README file.

## Usage

1. **Place your PDF files in the `pdfs/` directory.**

2. **Run the Flask application:**

   ```bash
   python app.py
   ```

   The application will start a development server at `http://127.0.0.1:5000/`.

3. **Open a web browser and navigate to `http://127.0.0.1:5000/` to view the PDF.**

## Configuration

- Modify `app.py` to change the directory or filename for serving PDFs.
- Update `index.html` to change the layout or add more functionality.

## Browser Compatibility

The application is designed to work with modern web browsers. Internet Explorer may have limited support for some features.

## Contributing

Feel free to open issues or submit pull requests if you find bugs or have improvements to suggest.

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or support, please contact [your-email@example.com](mailto:your-email@example.com).


### Tips for Customization

- Replace `your-username` in the clone URL with your GitHub username.
- Customize the email address and license information as needed.
- Add any additional sections or instructions specific to your project.

This README provides a clear and concise guide to setting up, running, and using your Flask-based PDF reader application.
