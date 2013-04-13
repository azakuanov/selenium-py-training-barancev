from model.user import User
from selenium import webdriver
from selenium.common.exceptions import *
from selenium_fixture import app


def test_login_with_valid_credentials(app):
    app.go_to_home_page()
    app.login(User.Admin())
    app.logout()


def test_login_with_invalid_credentials(app):
    app.go_to_home_page()
    app.login(User.random())
