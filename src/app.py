import connexion

app = connexion.App(__name__, specification_dir='./')

app.add_api('api_v1.yaml')
