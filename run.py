import api.app as app

run = app.create_app()
print(run.url_map)
run.run()