from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import get_service_url, get_unique_short_id, validate_id


@app.route('/api/id/<string:short>/', methods=['GET'])
def get_opinion(short):
    url_map = URLMap.query.filter_by(short=short).first()
    if url_map is None:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    return jsonify({'url': url_map.original}), 200


@app.route('/api/id/', methods=['POST'])
def add_url_map():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    custon_id_filled = 'custom_id' in data and data['custom_id']
    if custon_id_filled:
        if len(data['custom_id']) > 16:
            raise InvalidAPIUsage(
                'Указано недопустимое имя для короткой ссылки'
            )
        if not validate_id(data['custom_id']):
            raise InvalidAPIUsage(
                'Указано недопустимое имя для короткой ссылки'
            )
        if URLMap.query.filter_by(short=data['custom_id']).first() is not None:
            raise InvalidAPIUsage(f"Имя \"{data['custom_id']}\" уже занято.")

    url_map_data = {
        'original': data['url'],
        'short': data['custom_id']
        if custon_id_filled
        else get_unique_short_id(),
    }
    url_map = URLMap()
    url_map.from_dict(url_map_data)
    db.session.add(url_map)
    db.session.commit()
    return (
        jsonify(
            {
                'url': url_map.original,
                'short_link': get_service_url(url_map.short),
            }
        ),
        201,
    )
