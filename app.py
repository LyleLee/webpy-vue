import web
import requests
import json

urls = (
    '/', 'index',
    '/api/json/(.*)', 'APIProvider',
    '/(.*)', 'file'
)

web.config.debug = True
render = web.template.render('templates/')



def is_json(myjson):
  try:
    json.loads(myjson)
  except ValueError as e:
    return False
  return True

class index:
    def GET(self):
        return render.index()


class file:
    def GET(self, name):
        print(name)
        return "Not define this routes yet: " + name


class APIProvider:
    def GET(self, name):
        print('APIProvider get api:', name)
        res = requests.get('https://www3.nhk.or.jp/news/easy/news-list.json').json()
        return res

#


if __name__ == "__main__":

    app = web.application(urls, globals())
    app.run()
