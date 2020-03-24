# -*- coding: utf-8 -*-

from wtforms import Form, StringField, SelectField, PasswordField, validators


class LoginForm(Form):
    username = StringField('User', [
        validators.InputRequired(
            message="You must enter a user"),
        validators.Length(
            max=16,
            message=u"The user cannot be longer than 16 characters")])
    password = PasswordField('Password', [
        validators.InputRequired(
            message="You must enter a password"),
        validators.Length(
            min=4,
            max=16,
            message=u"Password must be between 4 and 16 characters long")])


class ApplicationSiteGroupForm(Form):
    name = StringField('First Name', [
        validators.InputRequired(
            message="You must enter a name"),
        validators.Length(
            max=20,
            message=u'Name cannot be longer than 20 characters')])


class ApplicationSiteForm(Form):
    name = StringField('First Name', [
        validators.InputRequired(
            message="You must enter a name"),
        validators.Length(
            max=35,
            message=u'Name cannot be longer than 35 letters')])
    url_list = StringField(u'URL', [
        validators.InputRequired(
            message=u"You must enter a URL"),
        validators.Length(
            max=35,
            message=u'URL cannot be longer than 35 characters')])


class ApplicationSelectForm(Form):
    name = SelectField('First Name', [
        validators.InputRequired(
            message="You must enter a name")])


class HostForm(Form):
    name = StringField('First Name', [
        validators.InputRequired(
            message=u"You must enter a name for the computer"),
        validators.Length(
            max=35,
            message=u"Your team name cannot be longer than 35 characters")])
    ipv4_address = StringField(u'IPv4 address', [
        validators.InputRequired(
            message=u"You must enter an IPv4 address"),
        validators.IPAddress(
            ipv4=True,
            ipv6=False,
            message=u"You must enter a valid IPv4 address")])


class HostSelectForm(Form):
    name = SelectField('First Name', [
        validators.InputRequired(
            message="You must enter a name")])


class GroupForm(Form):
    name = StringField('First Name', [
        validators.InputRequired(
            message="You must enter a name"),
        validators.Length(
            max=25,
            message=u'Name cannot be longer than 25 characters')])


class EntityForm(Form):
    entity_code = StringField('Code', [
        validators.InputRequired(
            message="You must enter a code"),
        validators.Length(
            max=4,
            message=u'Name cannot be longer than 4 characters')])
