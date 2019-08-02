import os
import tempfile

import pytest

from routes import app, db
from config import default as cfg


USER = {
	'username': 'fulano',
	'password': 123456
}


@pytest.fixture
def client():
    app.config.from_pyfile('{}/app/config/test.py'.format(cfg.BASE_DIR))
    client = app.test_client()

    with app.app_context():
   		db.create_all()

    yield client
    os.unlink(app.config['DATABASE'])


def test_registration(client):
	result = client.post('/registration', data=USER)
	assert result.status_code == 200


def test_login(client):
	result = client.post('/login', data=USER)
	assert result.status_code == 200


def test_send_image(client):
	image = '{}/test-img.jpg'.format(cfg.VENDOR_DIR)
	result = client.post('/registration', data=USER)
	result = client.post(
		'/send/image', 
		data={
			'image': (image, 'test-img.jpg')
		},
		headers={
			'Authorization': 'Bearer {}'.format(result.get_json()['access_token'])
		}
	)

	assert result.status_code == 200