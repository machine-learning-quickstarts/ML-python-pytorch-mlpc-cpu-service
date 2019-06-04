import falcon

from service import MNIST, Intro

api = application = falcon.API()

intro = Intro()
mnist = MNIST()

api.add_route('/mnist', intro)
api.add_route('/mnist/{index:int(min=0)}', mnist)
