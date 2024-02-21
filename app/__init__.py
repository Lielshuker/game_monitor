import connexion
import config
from app import encoder
from app.services.celery_beat import celery_init_app


def create_app():
    app = connexion.App(__name__, specification_dir='./swagger/', host=config.Config.FLASK_RUN_HOST)
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'mobile monitor'}, pythonic_params=True)
    return app


app = create_app()
celery_app = celery_init_app()
