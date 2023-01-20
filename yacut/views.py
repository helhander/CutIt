from flask import flash, redirect, render_template

from . import app, db
from .forms import URLMapForm
from .models import URLMap
from .utils import get_service_url, get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def add_url_map_view():
    form = URLMapForm()
    if form.validate_on_submit():
        custom_id = form.custom_id.data
        if URLMap.query.filter_by(short=custom_id).first():
            flash(f'Имя {custom_id} уже занято!')
            return render_template('add_url_map.html', form=form)
        if not custom_id:
            custom_id = get_unique_short_id()

        url_map = URLMap(original=form.original_link.data, short=custom_id)
        db.session.add(url_map)
        db.session.commit()
        flash('Ваша новая ссылка готова:')
        flash(get_service_url(custom_id), 'link')
        return render_template('add_url_map.html', form=form)
    return render_template('add_url_map.html', form=form)


@app.route('/<string:short>')
def opinion_view(short):
    url = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(url.original)
