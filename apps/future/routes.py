from flask import Flask, render_template, Blueprint, redirect, url_for

future = Blueprint('future', __name__)

@future.route('/announcement', methods=['GET', 'POST'])
def announcement():
    return render_template('Announcement.html', title='Announcement')