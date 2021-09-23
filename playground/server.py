from flask import Flask
from flask import render_template

app = Flask( __name__ )


@app.route( '/play', methods=['GET'] )
def boxeplay():
    times = int(3)
    return render_template( "index.html",times=times)


@app.route( '/play/<int:times>', methods=['GET'] )
def boxestime(times):
    return render_template( "index.html",  times=times)

@app.route( '/play/<int:times>/<color>', methods=['GET'] )
def boxescolor(times,color):
    return render_template( "index.html",  times=times,color=color)




if __name__ == "__main__":
    app.run( debug = True )
str

