import connexion

app = connexion.App(__name__, specification_dir='./')

app.add_api('api_v1.yaml')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
