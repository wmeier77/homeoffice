import routing


def main():
    """Startet den Web Server
    :return:
    """
    app = routing.create_app()
    app.run(debug=True)


if __name__ == "__main__":
    main()
