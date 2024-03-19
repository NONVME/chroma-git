# Chroma Git

Chroma git is a Python tool for colorising your GitHub commit heatmap. This tool generates random commits within specified date ranges, adding color highlights to your GitHub contribution map.

## Features

- Generates random commits within specified date ranges
- Allows customization of commit frequency and color intensity
- Supports testing mode to preview generated commits without pushing to GitHub

## Installation

1. Clone the repository:

    ```
    git clone git@github.com:NONVME/chroma-git.git
    ```

2. Navigate to the project directory:

    ```
    cd chroma-git
    ```

3. Run the script:

    ```
    python3 main.py -h
    ```

## Usage

Chroma git provides a command-line interface with several options:

```bash
python3 main.py [-h] [-s START] [-e END] [-w WEEK_DEPTH] [--color-depth COLOR_DEPTH] [-c] [-p PATH]
-s, --start: Set the start date for commit generation (format: 'Y-m-d').
-e, --end: Set the end date for commit generation (format: 'Y-m-d').
-w, --week-depth: Set the level of randomness for commit frequency within weeks.
--color-depth: Set the level of color intensity for commits in one day.
-c, --check: Run in test mode to preview commits without pushing to GitHub.
-p, --path: Set the path to the GitHub project.
```

Example usage with --check args do nothing, only print:

```bash
python main.py -s 2024-01-01 -e 2024-03-31 --week-depth 6 --color-depth 3 --check -p /path/to/your/github/fake-private-project
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.
