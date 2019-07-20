import pytest
from model.group import Group
from fixture.application import Application




def test_delete_first_group(app):
    app.session.login(username="admin",password="secret")
    app.group.delete_first_group()
    app.session.logout()

