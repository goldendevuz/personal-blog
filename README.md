# PersonalBlog

PersonalBlog is a Django-based web application designed for creating and managing blog posts.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Diagram](#diagram)
- [Idea Source](#idea-source)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/under-script/personalblog.git
    cd personalblog
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    make i
    ```

4. Apply migrations:

    ```bash
    make mig
    ```

5. Create a superuser to access the admin panel:

    ```bash
    make cru
    ```

6. Run the development server:

    ```bash
    make run
    ```

## Usage

- Access the admin interface at `http://127.0.0.1:8000/admin/`
- Visit the homepage at `http://127.0.0.1:8000/`

## Features

- User authentication and authorization
- Article creation, editing, and deletion
- Viewing detailed articles
- Responsive design using Bootstrap 5
- Django Crispy Forms integration

## Idea Source

The idea for PersonalBlog was inspired by [roadmap.sh](https://roadmap.sh) as outlined on the [roadmap.sh's Personal Blog project](https://roadmap.sh/projects/personal-blog) page, focusing on creating a simple and customizable blog system for personal use.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Commit your changes.
4. Push to the branch.
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact [goldendevuz@gmail.com].

---

Happy blogging!