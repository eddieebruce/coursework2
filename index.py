from flask import Flask, render_template, url_for, abort
app = Flask(__name__)

@app.route('/')
def root():
  return render_template('base.html'), 200

@app.route('/Videogames/')
def root_Videogames():
  return render_template('Videogames.html'), 200

@app.route('/XboxOne/')
def root_XboxOne():
  return render_template('Xboxone.html'), 200

@app.route('/WiiU/')
def root_WiiU():
  return render_template('Wiiu.html'), 200

@app.route('/Signuplogin/')
def root_Signuplogin():
  return render_template('Signuplogin.html'), 200

@app.route('/uncharted4/')
def root_uncharted4():
  return render_template('uncharted4.html'), 200

@app.route('/Playstation4/uncharted4/')
def root_Playstation4_uncharted4():
  return render_template('uncharted4.html'), 200

@app.route('/halo5/')
def root_halo5():
  return render_template('halo5.html'), 200

@app.route('/XboxOne/halo5/')
def root_XboxOne_halo5():
  return render_template('halo5.html'), 200

@app.route('/smashbrosu/')
def root_smashbrosu():
  return render_template('smashbrosu.html'), 200

@app.route('/WiiU/smashbrosu/')
def root_WiiU_smashbrosu():
  return render_template('smashbrosu.html'), 200

@app.route('/thelastofus/')
def root_thelastofus():
  return render_template('thelastofus.html'), 200

@app.route('/Playstation4/thelastofus/')
def root_Playstation4_thelastofus():
  return render_template('thelastofus.html'), 200

@app.route('/rarereplay/')
def root_rarereplay():
  return render_template('rarereplay.html'), 200

@app.route('/XboxOne/rarereplay/')
def root_XboxOne_rarereplay():
  return render_template('rarereplay.html'), 200

@app.route('/mariokart8/')
def root_mariokart8():
  return render_template('mariokart8.html'), 200

@app.route('/WiiU/mariokart8/')
def root_WiiU_mariokart8():
  return render_template('mariokart8.html'), 200

@app.route('/infamous/')
def root_infamous():
  return render_template('infamousss.html'), 200

@app.route('/Playstation4/infamous/')
def root_Playstation4_infamous():
  return render_template('infamousss.html'), 200

@app.route('/deadrising3/')
def root_deadrising3():
  return render_template('deadrising3.html'), 200

@app.route('/XboxOne/deadrising3/')
def root_XboxOne_deadrising3():
  return render_template('deadrising3.html'), 200

@app.route('/supermariomaker/')
def root_supermariomaker():
  return render_template('supermariomaker.html'), 200

@app.route('/WiiU/supermariomaker/')
def root_WiiU_supermariomaker():
  return render_template('supermariomaker.html'), 200

@app.route('/bioshock/')
def root_bioshock():
  return render_template('bioshock.html'), 200

@app.route('/Playstation4/bioshock/')
def root_Playstation4_bioshock():
  return render_template('bioshock.html'), 200

@app.route('/XboxOne/bioshock/')
def root_XboxOne_bioshock():
  return render_template('bioshock.html'), 200

@app.route('/tombraider/')
def root_tombraider():
  return render_template('tombraider.html'), 200

@app.route('/Playstation4/tombraider/')
def root_Playstation4_tombraider():
  return render_template('tombraider.html'), 200

@app.route('/XboxOne/tombraider/')
def root_XboxOne_tombraider():
  return render_template('tombraider.html'), 200

@app.route('/supermario3dworld/')
def root_supermario3dworld():
  return render_template('supermario3dworld.html'), 200

@app.route('/WiiU/supermario3dworld/')
def root_WiiU_supermario3dworld():
  return render_template('supermario3dworld.html'), 200

@app.route('/raymanlegends/')
def root_raymanlegends():
  return render_template('raymanlegends.html'), 200

@app.route('/Playstation4/raymanlegends/')
def root_Playstation4_raymanlegends():
  return render_template('raymanlegends.html'), 200

@app.route('/XboxOne/raymanlegends/')
def root_XboxOne_raymanlegends():
  return render_template('raymanlegends.html'), 200

@app.route('/WiiU/raymanlegends/')
def root_WiiU_raymanlegends():
  return render_template('raymanlegends.html'), 200

@app.route('/dyinglight/')
def root_dyinglight():
  return render_template('dyinglight.html'), 200

@app.route('/Playstation4/dyinglight/')
def root_Playstation4_dyinglight():
  return render_template('dyinglight.html'), 200

@app.route('/XboxOne/dyinglight/')
def root_XboxOne_dyinglight():
  return render_template('dyinglight.html'), 200

@app.route('/windwaker/')
def root_windwaker():
  return render_template('windwakerhd.html'), 200

@app.route('/WiiU/windwaker/')
def root_WiiU_windwaker():
  return render_template('windwakerhd.html'), 200

@app.route('/batman/')
def root_batman():
  return render_template('batman.html'), 200

@app.route('/XboxOne/batman/')
def root_XboxOne_batman():
  return render_template('batman.html'), 200

@app.route('/Playstation4/batman/')
def root_Playstation4_batman():
  return render_template('batman.html'), 200

@app.route('/starfoxzero/')
def root_starfoxzero():
  return render_template('starfoxzero.html'), 200

@app.route('/WiiU/starfoxzero/')
def root_WiiU_starfoxzero():
  return render_template('starfoxzero.html'), 200

@app.route('/metalgearsolidv/')
def root_metalgearsolidv():
  return render_template('metalgearsolidv.html'), 200

@app.route('/Playstation4/metalgearsolidv/')
def root_Playstation4_metalgearsolidv():
  return render_template('metalgearsolidv.html'), 200

@app.route('/XboxOne/metalgearsolidv/')
def root_XboxOne_metalgearsolidv():
  return render_template('metalgearsolidv.html'), 200

@app.route('/twilightprincesshd/')
def root_twilightprincess():
  return render_template('twilightprincesshd.html'), 200

@app.route('/WiiU/twilightprincesshd/')
def root_WiiU_twilightprincess():
  return render_template('twilightprincesshd.html'), 200

@app.route('/fallout4/')
def root_fallout4():
  return render_template('fallout4.html'), 200

@app.route('/XboxOne/fallout4/')
def root_XboxOne_fallout4():
  return render_template('fallout4.html'), 200

@app.route('/Playstation4/fallout4/')
def root_Playstation4_fallout4():
  return render_template('fallout4.html'), 200

@app.route('/pikmin3/')
def root_pikmin3():
  return render_template('pikmin3.html'), 200

@app.route('/WiiU/pikmin3/')
def root_WiiU_pikmin3():
  return render_template('pikmin3.html'), 200

@app.route('/bloodborne/')
def root_bloodborne():
  return render_template('bloodborne.html'), 200

@app.route('/Playstation4/bloodborne/')
def root_Playstation4_bloodborne():
  return render_template('bloodborne.html'), 200

@app.route('/killerinstinct/')
def root_killerinstinct():
  return render_template('killerinstinct.html'), 200

@app.route('/XboxOne/killerinstinct/')
def root_XboxOne_killerinstinct():
  return render_template('killerinstinct.html'), 200

@app.route('/splatoon/')
def root_splatoon():
  return render_template('splatoon.html'), 200

@app.route('/WiiU/splatoon/')
def root_WiiU_splatoon():
  return render_template('splatoon.html'), 200

@app.route('/codghosts/')
def root_codghosts():
  return render_template('codghosts.html'), 200

@app.route('/XboxOne/codghosts/')
def root_XboxOne_codghosts():
  return render_template('codghosts.html'), 200

@app.route('/WiiU/codghosts/')
def root_WiiU_codghosts():
  return render_template('codghosts.html'), 200

@app.route('/Playstation4/codghosts/')
def root_Playstation4_codghosts():
  return render_template('codghosts.html'), 200

@app.route('/Playstation4/untildawn/')
def root_Playstation4_untildawn():
  return render_template('untildawn.html'), 200

@app.route('/Playstation4/godofwar3/')
def root_Playstation4_godofwar3():
  return render_template('godofwar3.html'), 200

@app.route('/Playstation4/unchartedtndc/')
def root_Playstation4_unchartedtndc():
  return render_template('unchartedtndc.html'), 200

@app.route('/Playstation4/ratchetandclank/')
def root_Playstation4_ratchetandclank():
  return render_template('ratchetandclank.html'), 200

@app.route('/Playstation4/driveclub/')
def root_Playstation4_driveclub():
  return render_template('driveclub.html'), 200

@app.route('/Playstation4/nomanssky/')
def root_Playstation4_nomanssky():
  return render_template('nomanssky.html'), 200

@app.route('/XboxOne/gtav/')
def root_XboxOne_gtav():
  return render_template('gtav.html'), 200

@app.route('/Playstation4/gtav/')
def root_Playstation4_gtav():
  return render_template('gtav.html'), 200

@app.route('/XboxOne/destiny/')
def root_XboxOne_destiny():
  return render_template('destiny.html'), 200

@app.route('/Playstation4/destiny/')
def root_Playstation4_destiny():
  return render_template('destiny.html'), 200

@app.route('/Playstation4/guitarherolive/')
def root_Playstation4_guitarherolive():
  return render_template('guitarherolive.html'), 200

@app.route('/XboxOne/guitarherolive/')
def root_XboxOne_guitarherolive():
  return render_template('guitarherolive.html'), 200

@app.route('/XboxOne/codbo2/')
def root_XboxOne_codbo2():
  return render_template('codbo2.html'), 200

@app.route('/Playstation4/codbo2/')
def root_Playstation4_codbo2():
  return render_template('codbo2.html'), 200

@app.route('/WiiU/codbo2/')
def root_WiiU_codbo2():
  return render_template('codbo2.html'), 200

@app.route('/Playstation4/nba2k16/')
def root_Playstation4_nba2k16():
  return render_template('nba2k16.html'), 200

@app.route('/XboxOne/nba2k16/')
def root_XboxOne_nba2k16():
  return render_template('nba2k16.html'), 200

@app.route('/XboxOne/darksouls3/')
def root_XboxOne_darksouls3():
  return render_template('darksouls3.html'), 200

@app.route('/Playstation4/darksouls3/')
def root_Playstation4_darksouls3():
  return render_template('darksouls3.html'), 200

@app.route('/Playstation4/thewitcher/')
def root_Playstation4_thewitcher():
  return render_template('thewitcher.html'), 200

@app.route('/XboxOne/thewitcher/')
def root_XboxOne_thewitcher():
  return render_template('thewitcher.html'), 200

@app.route('/XboxOne/quantumbreak/')
def root_XboxOne_quantumbreak():
  return render_template('quantumbreak.html'), 200

@app.route('/XboxOne/forza5/')
def root_XboxOne_forza5():
  return render_template('forza5.html'), 200

@app.route('/XboxOne/sunsetoverdrive/')
def root_XboxOne_sunsetoverdrive():
  return render_template('sunsetoverdrive.html'), 200

@app.route('/XboxOne/gearsofwar4/')
def root_XboxOne_gearsofwar4():
  return render_template('gearsofwar4.html'), 200

@app.route('/XboxOne/halotmcc/')
def root_XboxOne_halotmcc():
  return render_template('halotmcc.html'), 200

@app.route('/XboxOne/titanfall/')
def root_XboxOne_titanfall():
  return render_template('titanfall.html'), 200

@app.route('/WiiU/hyrulewarriors/')
def root_WiiU_hyrulewarriors():
  return render_template('hyrulewarriors.html'), 200

@app.route('/WiiU/bayonetta2/')
def root_WiiU_bayonetta2():
  return render_template('bayonetta2.html'), 200

@app.route('/WiiU/donkeykongcountry/')
def root_WiiU_donkeykongcountry():
  return render_template('donkeykongcountry.html'), 200

@app.route('/WiiU/supermariobrosu/')
def root_WiiU_supermariobrosu():
  return render_template('newsupermariobrosu.html'), 200

@app.route('/WiiU/nintendoland/')
def root_WiiU_nintendoland():
  return render_template('nintendoland.html'), 200

@app.route('/WiiU/yoshiswoollyworld/')
def root_WiiU_yoshiswoollyworld():
  return render_template('yoshiswoollyworld.html'), 200

@app.route('/WiiU/pokkentournament/')
def root_WiiU_pokkentournament():
  return render_template('pokkentournament.html'), 200

@app.route('/WiiU/xenobladechroniclesx/')
def root_WiiU_xenobladechroniclesx():
  return render_template('xenobladechroniclesx.html'), 200

@app.route('/WiiU/thewonderful101/')
def root_WiiU_thewonderful101():
  return render_template('thewonderful101.html'), 200

@app.route('/WiiU/marioandsonic/')
def root_WiiU_marioandsonic():
  return render_template('marioandsonic.html'), 200

@app.route('/WiiU/captaintoad/')
def root_WiiU_captaintoad():
  return render_template('captaintoad.html'), 200

@app.route('/WiiU/gameandwario/')
def root_WiiU_gameandwario():
  return render_template('gameandwario.html'), 200

@app.route('/WiiU/soniclostworld/')
def root_WiiU_soniclostworld():
  return render_template('soniclostworld.html'), 200

if __name__ == ("__main__"):
  app.run(host='0.0.0.0', debug=True)

