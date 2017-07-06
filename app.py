from flask import Flask, render_template, redirect, url_for, abort
import models
from models import Entry
import forms

app = Flask(__name__)
app.secret_key = '&#@!)89vhcknvi3409>ijmcn-_9_-=cxuoenczniqe'


@app.route('/')
@app.route('/entries')
def index():
    entries = Entry.select()
    for entry in entries:
        for tag in entry.tags:
            print(tag)
    return render_template('index.html', entries=entries)


@app.route('/entries/<int:id>')
def details(id):
    try:
        entry = Entry.get(Entry.id == id)
    except models.DoesNotExist:
        abort(404)
    return render_template('detail.html', entry=entry)


@app.route('/entries/edit/<int:id>', methods=('GET', 'POST'))
def edit_entry(id):
    form = forms.EntryForm()
    try:
        entry = Entry.get(Entry.id == id)
    except models.DoesNotExist:
        abort(404)
    if form.validate_on_submit():
        entry.title = form.title.data
        entry.date = form.date.data
        entry.time_spent = form.time_spent.data
        entry.learned = form.learned.data
        entry.resources = form.resources.data
        entry.save()
        return redirect(url_for('details', id=entry.id))
    return render_template('edit.html', entry=entry, form=form)


@app.route('/entries/delete/<id>')
def delete_entry(id):
    try:
        entry = Entry.get(Entry.id == id)
    except models.DoesNotExist:
        abort(404)
    entry.delete_instance()
    return redirect(url_for('index'))


@app.route('/entry', methods=('GET', 'POST'))
def new_entry():
    form = forms.EntryForm()
    if form.validate_on_submit():
        Entry.create(**dict(form.data.items()))
        return redirect(url_for('index'))
    return render_template('new.html', form=form)


if __name__ == '__main__':
    models.initialize()
    app.run(debug=True, port=8000, host='0.0.0.0')
