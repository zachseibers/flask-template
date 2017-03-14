from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, \
                  abort, jsonify
from app.core.repository import *
import requests

mod = Blueprint('core', __name__)

@mod.route('/')
def index():
  repository = Repository()
  return (render_template('core/index.html', resources=repository.getResources()))


@mod.route('/cover')
def cover():
  return (render_template('core/cover.html'))


@mod.route('/signin')
def signin():
  return (render_template('core/signin.html'))


@mod.route('/jumbo')
def jumbo():
  return (render_template('core/jumbo.html'))
