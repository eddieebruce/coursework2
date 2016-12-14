import bcrypt
from functools import wraps
from flask import Flask,session, redirect, flash,  render_template, request, url_for, abort 
app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

valid_email = '40115101@live.napier.ac.uk'
valid_pwhash = bcrypt.hashpw('secretpass', bcrypt.gensalt())

def check_auth(email, password):
    if(email == valid_email and
        valid_pwhash == bcrypt.hashpw(password.encode('utf-8'), valid_pwhash)):
            return True
    return False

def requires_login(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        status = session.get('logged_in', False)
        if not status:
            return redirect(url_for('.root'))
        return f(*args, **kwargs)
    return decorated

@app.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/")
@requires_login
def secret():
    return render_template("base.html"), 200

@app.route("/Signuplogin/", methods=['GET', 'POST'])
def root_Signuplogin():
    if request.method == 'POST':
        user = request.form['email']
        pw = request.form['password']

        if check_auth(request.form['email'], request.form['password']):
            session['logged_in'] = True
            return redirect(url_for('.secret'))
    return render_template('Signuplogin.html')

@app.route('/')
def root():
  return render_template('base.html'), 200

@app.errorhandler(404)
def page_not_found(error):
  return render_template('error.html'), 404

@app.route('/Videogames/')
def root_Videogames():
  return render_template('Videogames.html'), 200

@app.route('/Movies/')
def root_Movies():
  return render_template('Movies.html'), 200

@app.route('/Music/')
def root_Music():
  return render_template('Music.html'), 200

@app.route('/uncharted4/')
def root_uncharted4():
  return render_template('uncharted4.html'), 200

@app.route('/Videogames/uncharted4/')
def root_Videogames__uncharted4():
  return render_template('uncharted.html'), 200

@app.route('/halo5/')
def root_halo5():
  return render_template('halo5.html'), 200

@app.route('/Videogames/halo5/')
def root_Videogames_halo5():
  return render_template('halo5.html'), 200

@app.route('/smashbrosu/')
def root_smashbrosu():
  return render_template('smashbrosu.html'), 200

@app.route('/Videogames/smashbrosu/')
def root_Videogames_smashbrosu():
  return render_template('smashbrosu.html'), 200

@app.route('/thelastofus/')
def root_thelastofus():
  return render_template('thelastofus.html'), 200

@app.route('/Videogames/thelastofus/')
def root_Videogames_thelastofus():
  return render_template('thelastofus.html'), 200

@app.route('/rarereplay/')
def root_rarereplay():
  return render_template('rarereplay.html'), 200

@app.route('/Videogames/rarereplay/')
def root_Videogames_rarereplay():
  return render_template('rarereplay.html'), 200

@app.route('/mariokart8/')
def root_mariokart8():
  return render_template('mariokart8.html'), 200

@app.route('/Videogames/mariokart8/')
def root_WiiU_mariokart8():
  return render_template('mariokart8.html'), 200

@app.route('/infamous/')
def root_infamous():
  return render_template('infamousss.html'), 200

@app.route('/Videogames/infamous/')
def root_Videogames_infamous():
  return render_template('infamousss.html'), 200

@app.route('/deadrising3/')
def root_deadrising3():
  return render_template('deadrising3.html'), 200

@app.route('/Videogames/deadrising3/')
def root_Videogames_deadrising3():
  return render_template('deadrising3.html'), 200

@app.route('/supermariomaker/')
def root_supermariomaker():
  return render_template('supermariomaker.html'), 200

@app.route('/Videogames/supermariomaker/')
def root_Videogames_supermariomaker():
  return render_template('supermariomaker.html'), 200

@app.route('/bioshock/')
def root_bioshock():
  return render_template('bioshock.html'), 200

@app.route('/Videogames/bioshock/')
def root_Videogames_bioshock():
  return render_template('bioshock.html'), 200

@app.route('/tombraider/')
def root_tombraider():
  return render_template('tombraider.html'), 200

@app.route('/Videogames/tombraider/')
def root_Videogames_tombraider():
  return render_template('tombraider.html'), 200

@app.route('/supermario3dworld/')
def root_supermario3dworld():
  return render_template('supermario3dworld.html'), 200

@app.route('/Videogames/supermario3dworld/')
def root_Videogames_supermario3dworld():
  return render_template('supermario3dworld.html'), 200

@app.route('/raymanlegends/')
def root_raymanlegends():
  return render_template('raymanlegends.html'), 200

@app.route('/Videogames/raymanlegends/')
def root_Videogames_raymanlegends():
  return render_template('raymanlegends.html'), 200

@app.route('/dyinglight/')
def root_dyinglight():
  return render_template('dyinglight.html'), 200

@app.route('/Videogames/dyinglight/')
def root_Videogames_dyinglight():
  return render_template('dyinglight.html'), 200

@app.route('/windwaker/')
def root_windwaker():
  return render_template('windwakerhd.html'), 200

@app.route('/videogames/windwaker/')
def root_videogames_windwaker():
  return render_template('windwakerhd.html'), 200

@app.route('/videogames/gta5/')
def root_videogames_gta5():
  return render_template('gtav.html'), 200

@app.route('/Movies/avengers')
def root_Movie_avengers():
  return render_template('avengers.html'), 200

@app.route('/Movies/godfather/')
def root_Movies_godfather():
  return render_template('godfather.html'), 200

@app.route('/Movies/batmanvsuperman/')
def root_Movies_batmanvsuperman():
  return render_template('batmanvsuperman.html'), 200

@app.route('/Movies/shawshank')
def root_Movies_shawshank():
  return render_template('shawshank.html'), 200

@app.route('/Movies/toystory')
def root_Movies_toystory():
  return render_template('toystory.html'), 200

@app.route('/Movies/guardians')
def root_Movies_guardians():
  return render_template('guardians.html'), 200

@app.route('/Movies/inception/')
def root_Movies_inception():
  return render_template('inception.html'), 200

@app.route('/Movies/suicidesquad/')
def root_Movies_suicidesquad():
  return render_template('suicidesquad.html'), 200

@app.route('/Movies/scream/')
def root_Movies_scream():
  return render_template('scream.html'), 200

@app.route('/Movies/exmachina/')
def root_Movies_exmachina():
  return render_template('exmachina.html'), 200

@app.route('/Movies/matrix/')
def root_Movies_matrix():
  return render_template('matrix.html'), 200

@app.route('/Movies/skyfall/')
def root_Movies_skyfall():
  return render_template('skyfall.html'), 200

@app.route('/Movies/whiplash/')
def root_Movies_whiplash():
  return render_template('whiplash.html'), 200

@app.route('/Movies/spiderman/')
def root_Movies_spiderman():
  return render_template('spiderman.html'), 200

@app.route('/Music/foofighters/')
def root_Music_foofighters():
  return render_template('foofighters.html'), 200

@app.route('/Music/nirvana/')
def root_Music_nirvana():
  return render_template('nirvana.html'), 200

@app.route('/Music/redhot')
def root_Music_redhot():
  return render_template('redhot.html'), 200

@app.route('/Music/adele/')
def root_Music_adele():
  return render_template('adele.html'), 200

@app.route('/Music/beatles/')
def root_Music_beatles():
  return render_template('beatles.html'), 200

@app.route('/Music/gunsandroses/')
def root_Music_gunsandroses():
  return render_template('gunsandroses.html'), 200

@app.route('/Music/michaeljackson')
def root_Music_michaeljackson():
  return render_template('michaeljackson.html'), 200

@app.route('/Music/oasis/')
def root_Music_oasis():
  return render_template('oasis.html'), 200

@app.route('/Music/u2')
def root_Music_u2():
  return render_template('u2.html'), 200

@app.route('/Music/queen/')
def root_Music_queen():
  return render_template('queen.html'), 200

@app.route('/Music/sum41/')
def root_Music_sum41():
  return render_template('sum41.html'), 200

@app.route('/Music/meatloaf/')
def root_Music_meatloaf():
  return render_template('meatloaf.html'), 200

@app.route('/Music/bobmarley/')
def root_Music_bobmarley():
  return render_template('bobmarley.html'), 200

@app.route('/Music/blink/')
def root_Music_blink():
  return render_template('blink.html'), 200

@app.route('/Music/bonjovi/')
def root_Music_bonjovi():
  return render_template('bonjovi.html'), 200

@app.route('/Music/falloutboy/')
def root_Music_falloutboy():
  return render_template('falloutboy.html'), 200

@app.route('/Movies/darkknight/')
def root_Movies_darkknight():
  return render_template('darkknight.html'), 200

@app.route('/Movies/starwars/')
def root_Movies_starwars():
  return render_template('starwars.html'), 200

@app.route('/avengers')
def root_avengers():
  return render_template('avengers.html'), 200

@app.route('/godfather/')
def root_godfather():
  return render_template('godfather.html'), 200

@app.route('/batmanvsuperman/')
def root_batmanvsuperman():
  return render_template('batmanvsuperman.html'), 200

@app.route('/shawshank')
def root_shawshank():
  return render_template('shawshank.html'), 200

@app.route('/toystory')
def root_toystory():
  return render_template('toystory.html'), 200

@app.route('/guardians')
def root_guardians():
  return render_template('guardians.html'), 200

@app.route('/inception/')
def root_inception():
  return render_template('inception.html'), 200

@app.route('/suicidesquad/')
def root_suicidesquad():
  return render_template('suicidesquad.html'), 200

@app.route('/scream/')
def root_scream():
  return render_template('scream.html'), 200

@app.route('/exmachina/')
def root_exmachina():
  return render_template('exmachina.html'), 200

@app.route('/matrix/')
def root_matrix():
  return render_template('matrix.html'), 200

@app.route('/skyfall/')
def root_skyfall():
  return render_template('skyfall.html'), 200

@app.route('/whiplash/')
def root_whiplash():
  return render_template('whiplash.html'), 200

@app.route('/foofighters/')
def root_foofighters():
  return render_template('foofighters.html'), 200

@app.route('/nirvana/')
def root_nirvana():
  return render_template('nirvana.html'), 200

@app.route('/redhot/')
def root_redhot():
  return render_template('redhot.html'), 200

@app.route('/adele/')
def root_adele():
  return render_template('adele.html'), 200

@app.route('/beatles/')
def root_beatles():
  return render_template('beatles.html'), 200

@app.route('/gunsandroses/')
def root_gunsandroses():
  return render_template('gunsandroses.html'), 200

@app.route('/michaeljackson')
def root_michaeljackson():
  return render_template('michaeljackson.html'), 200

@app.route('/oasis/')
def root_oasis():
  return render_template('oasis.html'), 200

@app.route('/u2/')
def root_u2():
  return render_template('u2.html'), 200

@app.route('/queen/')
def root_queen():
  return render_template('queen.html'), 200

@app.route('/sum41/')
def root_sum41():
  return render_template('sum41.html'), 200

@app.route('/meatloaf/')
def root_meatloaf():
  return render_template('meatloaf.html'), 200

@app.route('/blink/')
def root_blink():
  return render_template('blink.html'), 200

@app.route('/bonjovi/')
def root_bonjovi():
  return render_template('bonjovi.html'), 200

@app.route('/darkknight/')
def root_darkknight():
  return render_template('darkknight.html'), 200

@app.route('/starwars/')
def root_starwars():
  return render_template('starwars.html'), 200

@app.route('/bobmarley/')
def root_bobmarley():
  return render_template('bobmarley.html'), 200

if __name__ == ("__main__"):
  app.run(host='0.0.0.0', debug=True)

