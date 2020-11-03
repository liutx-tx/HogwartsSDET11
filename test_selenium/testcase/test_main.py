from test_selenium.page.main import Main


class TsetMain:
    def test_add_member(self):
        main=Main()
        main.add_member().add_member("xxx")
        main.import_user().get_massage()