from flask import Flask


def create_app():
    app = Flask(__name__)
    # def testing():
    #     print("hi hello")
    #     return 'testing'
    @app.route('/')
    def home():
        print("inside home function")
        return 'GFGGGGGG123'
    @app.route('/test')
    def test():
        return 'test'

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=80, debug=True)
