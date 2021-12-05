import web

urls = (
    '/','index',
    '/(.*)', 'file'
)

web.config.debug = True
render = web.template.render('templates/')

class index:
    def GET(self):
        return render.index()

class file:
    def GET(self,name):
        print(name)
        return "Not define this routes yet: " + name


if __name__ == "__main__":


    app = web.application(urls, globals())
    app.run()