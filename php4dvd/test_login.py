from model.user import User
from selenium import webdriver
from selenium.common.exceptions import *
from selenium_fixture import app


def test_login(app):
    app.go_to_home_page()
    app.login(User.Admin())
    app.logout()