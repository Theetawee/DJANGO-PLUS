# DjangoPlus

**DjangoPlus** is a robust, production-ready starter template for Django projects. It comes pre-configured with essential utilities, configurations, and features aimed at accelerating the development process. Whether you're working on a small web application or a large-scale platform, DjangoPlus streamlines your workflow from development to deployment.

## Key Features

- **Django 5.x Compatibility**: Built on the latest version of Django for cutting-edge functionality.
- **Security-First Approach**: Best practices for security, including HSTS, CSRF protection, and secure cookie settings.
- **Logging Configuration**: Advanced logging for error and warning notifications, sent directly to admins.
- **Minification Tools**: HTML, CSS, and JS minification for optimized performance.
- **SEO Optimization**: Pre-configured meta tags, Open Graph support, robots.txt, and sitemap.xml for better search engine visibility.
- **User Preferences**: Cookie consent management and theme toggle with smooth dark mode transitions.
- **Database Flexibility**: PostgreSQL for production and SQLite for local development.
- **Customizable Admin Interface**: Easily configure your admin panel's URL and secure it for production use.
- **Internationalization**: Multilingual support with easy configuration for international projects.
- **Ready for Deployment**: Comes with production settings for cloud environments like AWS, Heroku, and DigitalOcean.

## About the Creator

**DjangoPlus** was crafted by **Pattawee Drake Khaotungkulmethee**, a skilled software engineer at **Waanverse Labs**, specializing in developing scalable web solutions. DjangoPlus reflects his commitment to reducing boilerplate setup time and enhancing development efficiency. Pattawee brings expertise in web architecture, cloud services, and deployment to make DjangoPlus an ideal foundation for both new and experienced developers.

Feel free to connect for collaborations or discussions:

- **X (formerly Twitter)**: [@theetawee](https://x.com/theetawee)
- **LinkedIn**: [Pattawee Drake Khaotungkulmethee](https://www.linkedin.com/in/theetawee)
- **Email**: [tawee@waanverse.com](mailto:tawee@waanverse.com)

## Getting Started

To start using **DjangoPlus**, clone the repository and follow the setup steps:

### 1. Clone the Repository

```bash
git clone https://github.com/Theetawee/DJANGO-PLUS.git
cd djangoplus-boilerplate
```

### 2. Install Dependencies

For fixed versions:

```bash
pip install -r requirements.txt
```

For the latest versions of dependencies:

```bash
pip install -r requirements.dev.txt
```

### 3. Apply Database Migrations

```bash
python manage.py migrate
```

### 4. Run the Development Server

```bash
python manage.py runserver
```

## Configuration

1. **Environment Variables**:  
   Configure a `.env` file for sensitive settings such as database credentials, secret keys, etc. Make sure the `.env` file is added to `.gitignore` to avoid exposing sensitive information.

2. **Admin Access**:  
   Enable Django’s admin panel by setting `ADMIN_ENABLED=True` in your environment variables and customize the admin URL via `ADMIN_URL` for security.

3. **Logging**:  
   For production, ensure that warnings and errors are sent to admins using the `ADMINS` configuration in the settings.

## Deployment

DjangoPlus comes pre-configured for smooth deployment. A separate production settings file (`production.py`) is included with:

- Secure SSL/HTTPS configuration.
- Hardened security settings like `SECURE_HSTS_SECONDS`, `SECURE_SSL_REDIRECT`, and others.
- Settings for deploying on popular platforms (Heroku, AWS, DigitalOcean).

Ensure you follow these additional steps during deployment:

- Set environment variables (such as `DEBUG=False` and `ALLOWED_HOSTS`).
- Use a production-grade database like PostgreSQL.
- Apply your preferred web server and WSGI/ASGI server (e.g., Gunicorn, Daphne).

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests. Help us make DjangoPlus even better by adding features, improving documentation, or fixing bugs.

## License

This project is licensed under the MIT License. For more details, see the [LICENSE](LICENSE) file.
