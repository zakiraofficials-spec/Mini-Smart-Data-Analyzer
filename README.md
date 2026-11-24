# Mini Smart Data Analyzer

Mini Smart Data Analyzer is a beginner-friendly web application that uses **NumPy** to analyze a list of numbers and **Groq AI** to explain the results in simple English.

## Features

- Accepts 10 or more comma-separated numbers.
- Calculates mean, median, maximum, minimum, and sum.
- Shows the numbers in sorted order.
- Finds all values that are greater than the mean.
- Uses Groq AI model `openai/gpt-oss-20b` to explain the statistics.
- Shows helpful messages when input is invalid or the AI service is unavailable.
- Responsive Flask website.

## Technologies

- Python
- NumPy
- Flask
- Groq Python SDK
- python-dotenv
- HTML and CSS

## Project structure

```text
Mini-Smart-Data-Analyzer/
├── app.py
├── main.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
└── templates/
    └── index.html
```

## 1. Install Python

Install Python 3 from [python.org](https://www.python.org/downloads/). During installation on Windows, enable **Add Python to PATH**.

## 2. Open the project

Extract the ZIP file. Open the `Mini-Smart-Data-Analyzer` folder in Visual Studio Code.

In VS Code, select **Terminal → New Terminal**.

## 3. Create a virtual environment

On Windows PowerShell:

```powershell
py -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can skip activation and run the project's Python directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

If activation worked, install packages with:

```powershell
python -m pip install -r requirements.txt
```

## 4. Configure your Groq API key

1. Create or sign in to your Groq account and obtain an API key from the Groq Console.
2. In the project folder, make a copy of `.env.example`.
3. Rename the copy to `.env`.
4. Open `.env` and replace the example value:

```env
GROQ_API_KEY=put_your_real_groq_api_key_here
```

Keep the key private. Do not paste it into Python code, HTML, screenshots, or GitHub. The `.gitignore` file excludes `.env` from Git.

**Without an API key:** the numerical analysis still works. The website displays a message explaining that AI analysis needs a key.

## 5. Run the application

With the virtual environment activated:

```powershell
python app.py
```

Or, if you skipped activation:

```powershell
.\.venv\Scripts\python.exe app.py
```

Open this address in your browser:

http://127.0.0.1:5000

To stop the server, click the terminal and press `Ctrl + C`.

## Example input

Copy these 10 numbers into the website:

```text
12, 15, 18, 20, 22, 25, 28, 30, 32, 40
```

The app calculates the statistics and, when Groq is configured correctly, asks the AI to explain them.

## Run the calculation test

You can test the NumPy calculation module without starting Flask:

```powershell
python main.py
```

## Upload the project to GitHub

First, create a new empty repository on GitHub. Do not upload your `.env` file.

In the VS Code terminal, run these commands one by one from inside the project folder:

```powershell
git init
git add .
git status
git commit -m "Create Mini Smart Data Analyzer"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/Mini-Smart-Data-Analyzer.git
git push -u origin main
```

Replace the URL with your own GitHub repository URL. Before committing, check `git status` and confirm that `.env` is not listed.

If Git is not installed, install Git for Windows first, then close and reopen VS Code.

## Troubleshooting

- **`python` is not recognized:** try using `py` or the full virtual-environment Python path.
- **PowerShell activation is blocked:** use `.\.venv\Scripts\python.exe` for commands instead.
- **`ModuleNotFoundError`:** install packages using `python -m pip install -r requirements.txt` (or the full `.venv` Python path).
- **AI explanation does not appear:** check the `.env` filename, API key, internet connection, Groq account access, and model availability.
- **Port 5000 is busy:** close the other application using it, then run this project again.

## Learning note

The mean is the average. The median is the middle value after sorting. The maximum is the largest value, the minimum is the smallest value, and the sum is the total of all values.
