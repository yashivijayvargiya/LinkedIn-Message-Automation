# LinkedIn Automation with Selenium


This project automates the process of logging into LinkedIn and sending personalized messages to connections using Selenium WebDriver.

## Features

- Automates LinkedIn login using credentials from a parameter file.
- Iterates through a list of LinkedIn profile URLs from an Excel file.
- Sends personalized messages to each profile.

## Prerequisites

- Python 3.x
- `selenium` package
- `webdriver-manager` package
- `openpyxl` package
- Google Chrome browser

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yashivijayvargiya/LinkedIn-Message-Automation
    cd LinkedIn-Message-Automation
    ```

2. Install the required Python packages:
    ```bash
    pip install selenium webdriver-manager openpyxl
    ```

3. Download and install Google Chrome from [here](https://www.google.com/chrome/).

## Configuration

1. Create a `parameters.py` file in the project directory with the following content:
    ```python
    username = 'your_email@example.com'
    password = 'your_password'
    message = "Came across your profile and realized your interest in sports and supporting young talent"
    ```

2. Prepare an Excel file named `test.xlsx` in the same directory with the following structure:
    | Column A | Column B | Column C           |
    |----------|----------|--------------------|
    | Name     | Surname  | URL                |
    | John     | Doe      | https://linkedin.com/in/johndoe |

## Usage

1. Run the script:
    ```bash
    python linkedin_automation.py
    ```

## Script Overview

The script performs the following steps:

1. Launches a Chrome browser and maximizes the window.
2. Opens the LinkedIn login page and signs in using the provided credentials.
3. Reads the list of LinkedIn profile URLs from the Excel file.
4. Iterates through each profile, sends a personalized message, and logs out.

## Notes

- Ensure that the LinkedIn URLs in the Excel file are correct and accessible.
- Handle LinkedIn's rate limiting and CAPTCHA challenges, as excessive automation might trigger these.

## Contributing

Contributions are welcome! Please create a pull request with your changes or open an issue to discuss improvements.


## Acknowledgements

- [Selenium WebDriver](https://www.selenium.dev/)
- [webdriver-manager](https://pypi.org/project/webdriver-manager/)
- [openpyxl](https://openpyxl.readthedocs.io/en/stable/)

